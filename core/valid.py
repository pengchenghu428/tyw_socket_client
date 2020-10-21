#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> validity
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/20 20:45
@Desc   ：检查有效性
=================================================='''

import re
import pandas as pd
from config.read_config import TABLE_HEADERS


# IP 地址有效性检测
def check_ip_valid(ip):
    res = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                   ip)
    return res


# PORT 有效性
def check_port_valid(port):
    return port.isdigit()


# 文件有效性
def filetype_valid(filepath):
    paths = filepath.split('/')

    filetype = paths[-1][paths[-1].find('.')+1:]

    return filetype == 'csv'


# 文件内容有效性
def filemeta_valid(filepath):
    df = pd.read_csv(filepath)
    columns = df.columns.tolist()

    va = True
    for col in TABLE_HEADERS:
        va = va and (col in columns)

        if not va:
            break

    return va
