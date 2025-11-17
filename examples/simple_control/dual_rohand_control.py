#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: control_example.py
Description:
    演示如何使用SDK控制傲意多自由度灵巧手,在后续示例代码中,使用以下默认配置,
    请根据实际情况修改对应的配置参数:
    左手hand_id: 0x02
    右手hand_id: 0x03
    通讯接口: 485
    默认端口: "/dev/ttyUSB0"
    波特率: 115200

"""

from ohand.constants import *
from ohand.interface.uart import *
from ohand.OHandSerialAPI import OHandSerialAPI

def main():
    LEFT_HAND_ID = 0x02
    RIGHT_HAND_ID = 0x03
    DEFAULT_PORT = "/dev/ttyUSB0"  # 根据实际情况修改为对应的串口号
    interface_instance = Serial_Init(port_name=DEFAULT_PORT, baudrate=115200)
    ohand_instane = OHandSerialAPI(interface_instance,
                                    HAND_PROTOCOL_UART,
                                    0x01,
                                    send_data_impl,
                                    recv_data_impl)
    ohand_instane.HAND_SetTimerFunction(get_milli_seconds_impl,delay_milli_seconds_impl)
    ohand_instane.HAND_SetCommandTimeOut(255)
    while True:
        for i in range(6):
            err = ohand_instane.HAND_SetFingerPos(LEFT_HAND_ID, i, 65535, 255, [])
            if err != HAND_RESP_SUCCESS:
                print(f"Left rohand: finger_id:{i}, HAND_SetFingerPos returned error: {err}")
            delay_milli_seconds_impl(500)
            err = ohand_instane.HAND_SetFingerPos(LEFT_HAND_ID, i, 0, 255, [])
            if err != HAND_RESP_SUCCESS:
                print(f"Left rohand: finger_id:{i}, HAND_SetFingerPos returned error: {err}")
            delay_milli_seconds_impl(500)
        delay_milli_seconds_impl(1000)

        for i in range(6):
            err = ohand_instane.HAND_SetFingerPos(RIGHT_HAND_ID, i, 65535, 255, [])
            if err != HAND_RESP_SUCCESS:
                print(f"Left rohand: finger_id:{i}, HAND_SetFingerPos returned error: {err}")
            delay_milli_seconds_impl(500)
            err = ohand_instane.HAND_SetFingerPos(RIGHT_HAND_ID, i, 0, 255, [])
            if err != HAND_RESP_SUCCESS:
                print(f"Left rohand: finger_id:{i}, HAND_SetFingerPos returned error: {err}")
            delay_milli_seconds_impl(500)
        delay_milli_seconds_impl(1000)

if __name__ == "__main__":
    main()