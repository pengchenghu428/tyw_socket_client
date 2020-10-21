#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> interface
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/20 14:51
@Desc   ：界面相关
=================================================='''

from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QTableWidget
import config.read_config as bcfg


# 页面初始化
def init_interface(ui):
    ui.ip_lineEdit.setText(bcfg.SERVER_IP)  # 设置通信IP地址
    ui.port_lineEdit.setText(bcfg.SERVER_PORT)  # 设置通信端口号

    ui.tableWidget.horizontalHeader().setVisible(True)  # 设置水平表头可见
    ui.tableWidget.verticalHeader().setVisible(False)  # 设置垂直表头不可见
    ui.tableWidget.setHorizontalHeaderLabels(bcfg.TABLE_HEADERS)  # 设置水平表头
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动调整大小
    ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 首列
    ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
    ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选中
