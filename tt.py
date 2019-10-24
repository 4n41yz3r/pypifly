#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
from signal_filter import MedianFilter

imu = mpu9250()

try:
    f = MedianFilter(20)
    while True:
        t = imu.temp
        f.take(t)
        if f.new:
            print('Temperature: {:.3f} C'.format(f.value))
        sleep(0.005)
except KeyboardInterrupt:
    print('bye ...')
