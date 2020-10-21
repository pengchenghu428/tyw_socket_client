#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> file
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/20 15:20
@Desc   ：关于file的工具函数
=================================================='''

import os
import pandas as pd
import config.read_config as bcfg


# 获取桌面路径
def get_desktop():
    return os.path.join(os.path.expanduser('~'),"Desktop")


# 保存有效的IP和PORT地址
def update_config(ip, port):
    bcfg.SERVER_IP = ip
    bcfg.SERVER_PORT = port

    bcfg.conf.set("SERVER", "IP", bcfg.SERVER_IP)
    bcfg.conf.set("SERVER", "PORT", bcfg.SERVER_PORT)
    bcfg.conf.write(open('./config/base.ini', 'w', encoding='utf-8-sig'))
