#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> interaction
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/20 11:36
@Desc   ：UI 交互代码
=================================================='''

import socket
import pandas as pd
from functools import partial
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer

import core.valid as va
from core.file import get_desktop, update_config
from core.timer import timer_task

# 设置消息响应
def set_response(myMainWindow, myUI):
    myUI.switch_btn.clicked.connect(partial(switch_response, myUI))
    myUI.browse_btn.clicked.connect(partial(browse_response, myMainWindow, myUI))
    myUI.upload_btn.clicked.connect(partial(upload_response, myMainWindow, myUI))


# 连接、断开消息响应
def switch_response(ui):
    print("点击了连接/断开按键")
    return


# 浏览文件响应
def browse_response(window, ui):
    print("点击了浏览文件按键")
    filepath, filetype = QFileDialog.getOpenFileName(window, "选取文件", get_desktop(),
                                                     "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
    if filepath:
        if va.filetype_valid(filepath) and va.filemeta_valid(filepath):  # 检查是否是有效的CSV文件
            ui.filepath_lineEdit.setText(filepath)
        else:
            QMessageBox.warning(window, "警告", "请输入有效的CSV文件！", QMessageBox.Yes)


# 上传按键响应
def upload_response(window, ui):
    print("点击了上传按键")

    cur_ip, cur_port = ui.ip_lineEdit.text(), ui.port_lineEdit.text()

    if not va.check_ip_valid(cur_ip) or not va.check_port_valid(cur_port):
        QMessageBox.warning(window, "警告", "请输入有效的IP和端口号！", QMessageBox.Yes)
        return

    update_config(cur_ip, cur_port)  # 更新配置文件，以记录下次的地址
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议

    data_df = pd.read_csv(ui.filepath_lineEdit.text())  # 数据读取

    timer = QTimer(window)  # 初始化定时器
    timer.timeout.connect(partial(timer_task, timer, client, ui, data_df))
    timer.start(1000)  # 1s 发送一次
