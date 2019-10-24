#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
from signal_filter import MedianFilter
from signal_filter import IterableFilter

imu = mpu9250()

try:
    f = IterableFilter(MedianFilter, 10)
    while True:
        m = imu.mag
        f.take(m)
        if f.new:
            print('Mag: {:.3f} {:.3f} {:.3f} mg'.format(*(f.value)))
        sleep(0.01)
except KeyboardInterrupt:
    print('bye ...')
