'''
    BMP180 demo

    Author: shaoziyang
    Date:   2018.2

    http://www.micropython.org.cn

'''
from machine import I2C
import time

import bmp180

b = bmp180.BMP180(I2C(1))

while True:
    time.sleep_ms(500)
    b.get()
