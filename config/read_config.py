#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> read_config
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/19 21:30
@Desc   ：
=================================================='''

import os
import configparser

# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取config.ini的路径
config_path = os.path.join(cur_path, 'base.ini')

conf=configparser.ConfigParser()
conf.read(config_path, encoding="utf-8-sig")

# 服务器参数
SERVER_IP = conf.get('SERVER', 'IP')  # IP地址
SERVER_PORT = conf.get('SERVER', 'PORT')  # 监听端口

# 服务器参数
ICON_PATH = conf.get('UI', 'ICON_PATH')  # 图标资源文件地址
TABLE_HEADERS = conf.get('UI', 'TABLE_HEADERS').strip().split(',')
