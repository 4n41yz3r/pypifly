#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
from signal_filter import MedianFilter
from signal_filter import IterableFilter

try:
    imu = mpu9250()
    f = IterableFilter(MedianFilter, 20)
    while True:
        g = imu.gyro
        #f.take(g)
        #if f.new:
        #    print('Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*(f.value)))
        print('Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*g))
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
