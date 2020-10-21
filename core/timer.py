#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> timer
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/21 10:48
@Desc   ：定时任务模块
=================================================='''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from core.encode import encode_data
from core.udp import udp_send_data


def timer_task(timer, client, ui, df):
    cur_len = ui.tableWidget.rowCount()  # 获取当前长度

    if cur_len >= len(df):
        timer.stop()
        return

    data = df.iloc[cur_len]  # 获取数据
    endata = encode_data(data)  # 编码数据
    udp_send_data(client, endata)

    # 更新数据
    ui.tableWidget.setRowCount(cur_len + 1)
    newItem1 = QTableWidgetItem(str(int(data['设备'])))
    newItem1.setTextAlignment(Qt.AlignCenter)
    ui.tableWidget.setItem(cur_len, 0, newItem1)
    newItem2 = QTableWidgetItem(str(int(data['体能'])))
    newItem2.setTextAlignment(Qt.AlignCenter)
    ui.tableWidget.setItem(cur_len, 1, newItem2)
    newItem3 = QTableWidgetItem(str(int(data['状态'])))
    newItem3.setTextAlignment(Qt.AlignCenter)
    ui.tableWidget.setItem(cur_len, 2, newItem3)
    newItem4 = QTableWidgetItem('{:.6f}'.format(data['经度']))
    newItem4.setTextAlignment(Qt.AlignCenter)
    ui.tableWidget.setItem(cur_len, 3, newItem4)
    newItem5 = QTableWidgetItem('{:.6f}'.format(data['纬度']))
    newItem5.setTextAlignment(Qt.AlignCenter)
    ui.tableWidget.setItem(cur_len, 4, newItem5)

    ui.tableWidget.scrollToItem(newItem5)