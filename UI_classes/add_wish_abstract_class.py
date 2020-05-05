# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_files\add_wish.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_grid = QtWidgets.QGridLayout()
        self.main_grid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_grid.setContentsMargins(20, 20, 20, 20)
        self.main_grid.setHorizontalSpacing(6)
        self.main_grid.setVerticalSpacing(20)
        self.main_grid.setObjectName("main_grid")
        self.add_wish_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_wish_btn.sizePolicy().hasHeightForWidth())
        self.add_wish_btn.setSizePolicy(sizePolicy)
        self.add_wish_btn.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_wish_btn.setFont(font)
        self.add_wish_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_wish_btn.setStyleSheet("QPushButton { \n"
"    background-color: #7cfc00 ;\n"
"    border-radius: 25px;\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9cff3c;\n"
"}\n"
"")
        self.add_wish_btn.setIconSize(QtCore.QSize(25, 25))
        self.add_wish_btn.setObjectName("add_wish_btn")
        self.main_grid.addWidget(self.add_wish_btn, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_grid.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_grid.addItem(spacerItem1, 1, 0, 1, 1)
        self.form = QtWidgets.QGridLayout()
        self.form.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.form.setHorizontalSpacing(20)
        self.form.setVerticalSpacing(10)
        self.form.setObjectName("form")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.form.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.form.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.form.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.form.addWidget(self.label_4, 3, 0, 1, 1)
        self.wish_name = QtWidgets.QPlainTextEdit(Dialog)
        self.wish_name.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid lightgrey;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: grey;\n"
"}")
        self.wish_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wish_name.setObjectName("wish_name")
        self.form.addWidget(self.wish_name, 0, 1, 1, 1)
        self.wish_price = QtWidgets.QPlainTextEdit(Dialog)
        self.wish_price.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid lightgrey;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: grey;\n"
"}")
        self.wish_price.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wish_price.setObjectName("wish_price")
        self.form.addWidget(self.wish_price, 1, 1, 1, 1)
        self.wish_url = QtWidgets.QPlainTextEdit(Dialog)
        self.wish_url.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid lightgrey;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: grey;\n"
"}")
        self.wish_url.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wish_url.setObjectName("wish_url")
        self.form.addWidget(self.wish_url, 2, 1, 1, 1)
        self.wish_description = QtWidgets.QPlainTextEdit(Dialog)
        self.wish_description.setStyleSheet("QPlainTextEdit {\n"
"    border: 1px solid lightgrey;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: grey;\n"
"}")
        self.wish_description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wish_description.setObjectName("wish_description")
        self.form.addWidget(self.wish_description, 3, 1, 1, 1)
        self.main_grid.addLayout(self.form, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.main_grid, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        Dialog.finished['int'].connect(Dialog.enable_parent)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Wish"))
        self.add_wish_btn.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Название"))
        self.label_2.setText(_translate("Dialog", "Цена"))
        self.label_3.setText(_translate("Dialog", "Ссылка"))
        self.label_4.setText(_translate("Dialog", "Описание"))


