# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coffee(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(990, 574)
        self.showing = QtWidgets.QTableWidget(Form)
        self.showing.setGeometry(QtCore.QRect(10, 10, 971, 511))
        self.showing.setObjectName("showing")
        self.showing.setColumnCount(0)
        self.showing.setRowCount(0)
        self.showing.horizontalHeader().setDefaultSectionSize(130)
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(10, 530, 371, 41))
        self.add.setObjectName("add")
        self.edit = QtWidgets.QPushButton(Form)
        self.edit.setGeometry(QtCore.QRect(610, 530, 371, 41))
        self.edit.setObjectName("edit")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(390, 530, 211, 41))
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "Добавить"))
        self.edit.setText(_translate("Form", "Изменить"))
