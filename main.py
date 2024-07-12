import os
import queue
import subprocess
import sys
import threading

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QAbstractItemView, QApplication, QWidget, QFileDialog, QTableWidgetItem, QMenu, \
    QMessageBox

from ui_main_form import Ui_Form


class ResultLine:
    def __init__(self, line):
        split = line.split(':')
        if len(split) > 2:
            i = 0
            if len(line) > 1 and line[1] == ':':
                self.full_path = ':'.join(split[i:i + 2])
                i += 2
            else:
                self.full_path = split[i]
                i += 1
            self.full_path = self.full_path.replace('/', '\\')
            self.line = split[i]
            i += 1
            try:
                self.contents = split[i]
                i += 1
                while i < len(split):
                    self.contents += ':' + split[i]
                    i += 1
            except:
                self.contents = ""
                
            self.file_name = os.path.basename(self.full_path)
            self.path = os.path.dirname(self.full_path)
        else:  # Something Weird...
            self.contents = line
            self.line = ""
            self.file_name = ""
            self.path = ""

    def csv_line(self):
        return f'"{self.file_name}","{self.path}","{self.line}","{self.contents}"'


class MainWidget(QWidget):
    results_ready = Signal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.threaded_search)
        self.ui.reset_btn.clicked.connect(self.reset_fields)
        self.ui.copy_command_btn.clicked.connect(self.copy_command)
        self.ui.about_btn.clicked.connect(self.about)
        self.ui.browse_btn.clicked.connect(self.browse_directory)

        self.ui.result_table.setColumnCount(4)
        self.ui.result_table.setHorizontalHeaderLabels(
            ['Path', 'File name', 'Line', 'Contents'])
        self.ui.result_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.result_table.customContextMenuRequested.connect(self.show_context_menu)

        self.ui.result_table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.result_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        # self.ui.result_table.doubleClicked.connect(self.open_file)
        self.results_ready.connect(self.update_table)
        self.result_queue = queue.Queue()
    def browse_directory(self):
        initial_dir = self.ui.base_path_edit.text()
        dir_path = QFileDialog.getExistingDirectory(
            self, "Select Directory", initial_dir)
        if dir_path:
            dir_path = dir_path.replace('/', '\\')
            self.ui.base_path_edit.setText(dir_path)
    def generate_command_aslist(self):
        search_string = self.ui.search_string_edit.text()
        base_dir = self.ui.base_path_edit.text()
        file_filter = self.ui.filefilter_edit.text()
        recursive = self.ui.recursive_checkbox.isChecked()
        ignore_case = self.ui.ignore_case_checkbox.isChecked()
        skip_binary = self.ui.skip_binary_checkbox.isChecked()
        regex = self.ui.regex_checkbox.isChecked()

        if not search_string or not base_dir:
            QMessageBox.critical(
                self, "Error", "Please provide all necessary inputs.")
            return []

        cmd = ['rg']
        cmd.append('--line-number')
        if file_filter:
            cmd.append('-g')
            cmd.append(f'{file_filter}')
        if not recursive:
            cmd.append('--max-depth=1')
        if not skip_binary:
            cmd.append('--binary')
        if ignore_case:
            cmd.append('-i')
        if not regex:
            cmd.append('--fixed-strings')
        cmd.append(f'{search_string}')
        cmd.append(f'{base_dir}')
        return cmd
    def generate_command(self):
        search_string = self.ui.search_string_edit.text()
        base_dir = self.ui.base_path_edit.text()
        file_filter = self.ui.filefilter_edit.text()
        recursive = self.ui.recursive_checkbox.isChecked()
        ignore_case = self.ui.ignore_case_checkbox.isChecked()
        skip_binary = self.ui.skip_binary_checkbox.isChecked()
        regex = self.ui.regex_checkbox.isChecked()

        if not search_string or not base_dir:
            QMessageBox.critical(
                self, "Error", "Please provide all necessary inputs.")
            return ''

        cmd = ['rg']
        cmd.append('--line-number')
        if file_filter:
            cmd.append('-g')
            cmd.append(f'{file_filter}')
        if not recursive:
            cmd.append('--max-depth=1')
        if not skip_binary:
            cmd.append('--binary')
        if ignore_case:
            cmd.append('-i')
        if not regex:
            cmd.append('--fixed-strings')
        cmd.append(f'"{search_string}"')
        cmd.append(f'"{base_dir}"')
        return ' '.join(cmd)

    def copy_command(self):
        command = self.generate_command()
        if command == '':
            return
        QApplication.clipboard().setText(command)
        QMessageBox.information(
            self, "Copied", f"Command copied to clipboard:\n{command}")

    def search_files(self, command):
        try:
            result = subprocess.run(
                command,
                encoding='utf-8',
                text=True,
                capture_output=True,
                shell=True
            )
            if result.stdout:
                self.result_queue.put(result.stdout.splitlines())
                return
            if result.stderr:
                QMessageBox.critical(self, "Error",result.stderr)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.result_queue.put([])

    def update_table(self, results):
        self.ui.result_table.setRowCount(0)
        for line in results:
            self.insert_row_into_table(line)
        # self.ui.result_table.resizeColumnsToContents()
        self.ui.total_label.setText(f'Total match: {self.ui.result_table.rowCount()}')
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(100)

    def insert_row_into_table(self, line):
        result_line = ResultLine(line)
        row_position = self.ui.result_table.rowCount()
        self.ui.result_table.insertRow(row_position)
        pathItem = QTableWidgetItem(result_line.path)
        pathItem.setToolTip(result_line.path)
        self.ui.result_table.setItem(
            row_position, 0, pathItem)
        self.ui.result_table.setItem(
            row_position, 1, QTableWidgetItem(result_line.file_name))
        self.ui.result_table.setItem(
            row_position, 2, QTableWidgetItem(result_line.line))
        contentsItem = QTableWidgetItem(result_line.contents)
        contentsItem.setToolTip(result_line.contents)
        self.ui.result_table.setItem(
            row_position, 3, contentsItem)

    def threaded_search(self):
        command = self.generate_command_aslist()
        if command == []:
            return
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setRange(0, 0)
        self.ui.total_label.setText("")
        threading.Thread(target=self.search_thread, args=(command,)).start()

    def search_thread(self, command):
        self.search_files(command)
        results = self.result_queue.get()
        self.results_ready.emit(results)

    def open_file(self):
        current_row = self.ui.result_table.currentRow()
        if current_row > -1:
            path = self.ui.result_table.item(current_row, 0).text()
            file_name = self.ui.result_table.item(current_row, 1).text()
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                os.startfile(file_path)

    def show_in_explorer(self):
        current_row = self.ui.result_table.currentRow()
        if current_row > -1:
            path = self.ui.result_table.item(current_row, 0).text()
            file_name = self.ui.result_table.item(current_row, 1).text()
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                subprocess.run(
                    ['explorer', '/select,', file_path.replace('/', '\\')])

    def copy_file_path(self):
        current_row = self.ui.result_table.currentRow()
        if current_row > -1:
            path = self.ui.result_table.item(current_row, 0).text()
            file_name = self.ui.result_table.item(current_row, 1).text()
            file_path = os.path.join(path, file_name)
            QApplication.clipboard().setText(file_path)
            QMessageBox.information(self, "Copied", f"File path copied to clipboard:\n{file_path}")

    def show_context_menu(self, pos):
        if self.ui.result_table.rowCount()<1:
            return
        context_menu = QMenu(self)
        open_action = context_menu.addAction("Open with Default Viewer")
        explorer_action = context_menu.addAction("Show in Explorer")
        copy_action = context_menu.addAction("Copy File Path")
        action = context_menu.exec(self.ui.result_table.mapToGlobal(pos))
        if action == open_action:
            self.open_file()
        elif action == explorer_action:
            self.show_in_explorer()
        elif action == copy_action:
            self.copy_file_path()

    def reset_fields(self):
        self.ui.search_string_edit.clear()
        self.ui.filefilter_edit.setText("*.*")
        self.ui.recursive_checkbox.setChecked(True)
        self.ui.ignore_case_checkbox.setChecked(True)
        self.ui.skip_binary_checkbox.setChecked(True)
        self.ui.regex_checkbox.setChecked(True)
        self.ui.result_table.setRowCount(0)
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)
        self.ui.total_label.setText("")

    def about(self):
        QMessageBox.information(
            self, "About", "Ripgrep GUI\nVersion 1.0\nCreated by Garawaa")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec())