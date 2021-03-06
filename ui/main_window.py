# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_btn.setObjectName("upload_btn")
        self.gridLayout.addWidget(self.upload_btn, 1, 5, 1, 1)
        self.switch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.switch_btn.setObjectName("switch_btn")
        self.gridLayout.addWidget(self.switch_btn, 0, 4, 1, 2)
        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 0, 0, 1, 1)
        self.port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.gridLayout.addWidget(self.port_lineEdit, 0, 3, 1, 1)
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setObjectName("browse_btn")
        self.gridLayout.addWidget(self.browse_btn, 1, 4, 1, 1)
        self.ip_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.gridLayout.addWidget(self.ip_lineEdit, 0, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 0, 2, 1, 1)
        self.filepath_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath_lineEdit.setEnabled(False)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.gridLayout.addWidget(self.filepath_lineEdit, 1, 0, 1, 4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "下位机通讯客户端"))
        self.upload_btn.setText(_translate("MainWindow", "上传"))
        self.switch_btn.setText(_translate("MainWindow", "连接"))
        self.ip_label.setText(_translate("MainWindow", "IP地址："))
        self.browse_btn.setText(_translate("MainWindow", "浏览"))
        self.port_label.setText(_translate("MainWindow", "端口号："))
