# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_input_dialog(object):
    def setupUi(self, input_dialog):
        input_dialog.setObjectName("input_dialog")
        input_dialog.setWindowModality(QtCore.Qt.WindowModal)
        input_dialog.resize(500, 49)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        input_dialog.setFont(font)
        self.centralwidget = QtWidgets.QWidget(input_dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(8, 12, 8, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLineEdit_input_content = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLineEdit_input_content.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uiLineEdit_input_content.setObjectName("uiLineEdit_input_content")
        self.horizontalLayout.addWidget(self.uiLineEdit_input_content)
        self.uiPushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_confirm.setObjectName("uiPushButton_confirm")
        self.horizontalLayout.addWidget(self.uiPushButton_confirm)
        input_dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(input_dialog)
        QtCore.QMetaObject.connectSlotsByName(input_dialog)

    def retranslateUi(self, input_dialog):
        _translate = QtCore.QCoreApplication.translate
        input_dialog.setWindowTitle(_translate("input_dialog", "输入内容"))
        self.uiPushButton_confirm.setText(_translate("input_dialog", "确定"))