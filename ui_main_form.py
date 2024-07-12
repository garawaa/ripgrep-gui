# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_string_label = QLabel(Form)
        self.search_string_label.setObjectName(u"search_string_label")

        self.horizontalLayout.addWidget(self.search_string_label)

        self.search_string_edit = QLineEdit(Form)
        self.search_string_edit.setObjectName(u"search_string_edit")

        self.horizontalLayout.addWidget(self.search_string_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.base_path_label = QLabel(Form)
        self.base_path_label.setObjectName(u"base_path_label")

        self.horizontalLayout_2.addWidget(self.base_path_label)

        self.base_path_edit = QLineEdit(Form)
        self.base_path_edit.setObjectName(u"base_path_edit")

        self.horizontalLayout_2.addWidget(self.base_path_edit)

        self.browse_btn = QPushButton(Form)
        self.browse_btn.setObjectName(u"browse_btn")

        self.horizontalLayout_2.addWidget(self.browse_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.filefilter_label = QLabel(Form)
        self.filefilter_label.setObjectName(u"filefilter_label")

        self.horizontalLayout_5.addWidget(self.filefilter_label)

        self.filefilter_edit = QLineEdit(Form)
        self.filefilter_edit.setObjectName(u"filefilter_edit")

        self.horizontalLayout_5.addWidget(self.filefilter_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.recursive_checkbox = QCheckBox(Form)
        self.recursive_checkbox.setObjectName(u"recursive_checkbox")
        self.recursive_checkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.recursive_checkbox)

        self.ignore_case_checkbox = QCheckBox(Form)
        self.ignore_case_checkbox.setObjectName(u"ignore_case_checkbox")
        self.ignore_case_checkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.ignore_case_checkbox)

        self.skip_binary_checkbox = QCheckBox(Form)
        self.skip_binary_checkbox.setObjectName(u"skip_binary_checkbox")
        self.skip_binary_checkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.skip_binary_checkbox)

        self.regex_checkbox = QCheckBox(Form)
        self.regex_checkbox.setObjectName(u"regex_checkbox")
        self.regex_checkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.regex_checkbox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.total_label = QLabel(Form)
        self.total_label.setObjectName(u"total_label")

        self.horizontalLayout_3.addWidget(self.total_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_3.addWidget(self.search_btn)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_3.addWidget(self.reset_btn)

        self.copy_command_btn = QPushButton(Form)
        self.copy_command_btn.setObjectName(u"copy_command_btn")

        self.horizontalLayout_3.addWidget(self.copy_command_btn)

        self.about_btn = QPushButton(Form)
        self.about_btn.setObjectName(u"about_btn")

        self.horizontalLayout_3.addWidget(self.about_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.result_table = QTableWidget(Form)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.result_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.result_table)


        self.retranslateUi(Form)
        self.search_string_edit.editingFinished.connect(self.search_btn.click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Ripgrep GUI", None))
        self.search_string_label.setText(QCoreApplication.translate("Form", u"Search string: ", None))
        self.base_path_label.setText(QCoreApplication.translate("Form", u"Base path: ", None))
        self.browse_btn.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.filefilter_label.setText(QCoreApplication.translate("Form", u"File filter:   ", None))
        self.filefilter_edit.setText(QCoreApplication.translate("Form", u"*.*", None))
        self.recursive_checkbox.setText(QCoreApplication.translate("Form", u"Recursive", None))
        self.ignore_case_checkbox.setText(QCoreApplication.translate("Form", u"Ignore case", None))
        self.skip_binary_checkbox.setText(QCoreApplication.translate("Form", u"Skip binary", None))
        self.regex_checkbox.setText(QCoreApplication.translate("Form", u"Regex", None))
        self.total_label.setText(QCoreApplication.translate("Form", u"Total match: ", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.copy_command_btn.setText(QCoreApplication.translate("Form", u"Command to clipboard", None))
        self.about_btn.setText(QCoreApplication.translate("Form", u"About", None))
    # retranslateUi

