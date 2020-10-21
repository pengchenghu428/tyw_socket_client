#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> encode
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/21 10:49
@Desc   ：
=================================================='''

import math


# 数据编码
def encode_data(data):
    res = []
    res.append(254)  # 起始
    res.append(241)
    res.append(int(data['设备']))  # 具体日期
    res.append(int(data['体能']))
    res.append(int(data['状态']))

    longitude, latitude = round(data['经度'], 6), round(data['纬度'], 6)
    long_integer, long_decimal = int(longitude), int(math.modf(longitude)[0] * 1e6)
    res.append(long_integer)  # 整数部分
    res.append(long_decimal >> 16)  # 小数部分-高字节
    res.append((long_decimal >> 8) & 0xFF)  # 小数部分-中字节
    res.append(long_decimal & 0xFF)  # 小数部分-低字节

    lat_integer, lat_decimal = int(latitude), int(math.modf(latitude)[0] * 1e6)
    res.append(lat_integer)
    res.append(lat_decimal >> 16)
    res.append((lat_decimal >> 8) & 0xFF)  # 小数部分-中字节
    res.append(lat_decimal & 0xFF)

    bres = bytes(res)
    return bres
