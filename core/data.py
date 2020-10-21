#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> data
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/20 21:29
@Desc   ：
=================================================='''

import random
import pandas as pd


# 生成虚假数据
def generate_fake_data():
    df = pd.DataFrame()
    df['体能'] = [i for i in range(100, 0, -1)]
    df['设备'] = 2
    df['状态'] = [random.randint(1, 3) for i in range(100)]
    df['经度'] = 116.407413
    df['纬度'] = 39.904214
    return df


if __name__ == '__main__':
    df = generate_fake_data()

    df.to_csv("../data/data.csv", index=False)
