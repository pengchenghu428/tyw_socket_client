#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：tyw_socket_client -> udp
@IDE    ：PyCharm
@Author ：pengchenghu
@Date   ：2020/10/21 10:17
@Desc   ：socket udp 通信
=================================================='''

import socket
from config.read_config import SERVER_IP, SERVER_PORT


# UDP 发送数据
def udp_send_data(client, data):
    client.sendto(data, (SERVER_IP, int(SERVER_PORT)))

