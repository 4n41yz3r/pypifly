#!/usr/bin/env python

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
        f.take(a)
        if f.new:
            print 'Accel: {:.3f} {:.3f} {:.3f} mg'.format(*(f.value))
        sleep(0.005)
except KeyboardInterrupt:
    print 'bye ...'
