# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_files\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(786, 665)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1000000, 1000000))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(100000, 100000))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_tab.setFont(font)
        self.main_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tab.setObjectName("main_tab")
        self.active_wishes = QtWidgets.QWidget()
        self.active_wishes.setObjectName("active_wishes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.active_wishes)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 30)
        self.gridLayout_3.setSpacing(30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.active_wishes)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.wish_list = QtWidgets.QWidget()
        self.wish_list.setGeometry(QtCore.QRect(0, 0, 778, 490))
        self.wish_list.setAutoFillBackground(False)
        self.wish_list.setObjectName("wish_list")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wish_list)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.wish_list)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.add_wish_btn = QtWidgets.QPushButton(self.active_wishes)
        self.add_wish_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_wish_btn.sizePolicy().hasHeightForWidth())
        self.add_wish_btn.setSizePolicy(sizePolicy)
        self.add_wish_btn.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_wish_btn.setFont(font)
        self.add_wish_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.add_wish_btn.setWhatsThis("")
        self.add_wish_btn.setAccessibleDescription("")
        self.add_wish_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_wish_btn.setAutoFillBackground(False)
        self.add_wish_btn.setStyleSheet("QPushButton { \n"
"    background-color: #7cfc00 ;\n"
"    border-radius: 35px;\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9cff3c;\n"
"}\n"
"")
        self.add_wish_btn.setIconSize(QtCore.QSize(0, 0))
        self.add_wish_btn.setShortcut("")
        self.add_wish_btn.setAutoDefault(False)
        self.add_wish_btn.setDefault(False)
        self.add_wish_btn.setFlat(False)
        self.add_wish_btn.setObjectName("add_wish_btn")
        self.gridLayout_3.addWidget(self.add_wish_btn, 1, 1, 1, 1)
        self.main_tab.addTab(self.active_wishes, "")
        self.executed_wishes = QtWidgets.QWidget()
        self.executed_wishes.setObjectName("executed_wishes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.executed_wishes)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.executed_wishes)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.executed_wish_list = QtWidgets.QWidget()
        self.executed_wish_list.setGeometry(QtCore.QRect(0, 0, 778, 620))
        self.executed_wish_list.setObjectName("executed_wish_list")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.executed_wish_list)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2.setWidget(self.executed_wish_list)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.main_tab.addTab(self.executed_wishes, "")
        self.gridLayout_2.addWidget(self.main_tab, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(1)
        self.add_wish_btn.clicked.connect(MainWindow.open_AddWish_window)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wish List"))
        self.add_wish_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Добавить новое желание</p></body></html>"))
        self.add_wish_btn.setText(_translate("MainWindow", "Добавить"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.active_wishes), _translate("MainWindow", "Активные Желания"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.executed_wishes), _translate("MainWindow", "Исполненные Желания"))


