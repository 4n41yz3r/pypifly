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
        a = imu.accel
        #f.take(a)
        #if f.new:
        #    print('Accel: {:.3f} {:.3f} {:.3f} mg'.format(*(f.value)))
        print('Accel: {:.3f} {:.3f} {:.3f} mg'.format(*(a)))
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
