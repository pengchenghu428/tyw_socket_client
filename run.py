#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> run
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/19 21:26
@Desc   ：客户端主入口
=================================================='''
import sys
import ui.main_window as umwindow
import config.read_config as bcfg
from core.interaction import set_response
from core.interface import init_interface
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    myapp = QApplication(sys.argv)  # 初始化应用实例
    myMainWindow = QMainWindow()  # 初始化对话框实例

    myMainWindow.setWindowIcon(QIcon(bcfg.ICON_PATH))  # 设置

    myUI = umwindow.Ui_MainWindow()  # 初始化界面
    myUI.setupUi(myMainWindow)  # 装载UI
    myMainWindow.show()  # 显示界面

    init_interface(myUI)  # 页面初始化
    set_response(myMainWindow, myUI)  # 设置消息响应

    sys.exit(myapp.exec_())
