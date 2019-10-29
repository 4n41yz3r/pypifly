#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
from signal_filter import MedianFilter
from signal_filter import IterableFilter
from calibrator import DynamicCompassCalibrator

imu = mpu9250()

try:
    dcc = DynamicCompassCalibrator()
    while True:
        m = imu.mag
        m = dcc.correct(m)
        print('Mag: {:.3f} {:.3f} {:.3f} mg'.format(*m))
        print(dcc.min)
        print(dcc.max)
        print(dcc.offset)
        print(dcc.scale)
        sleep(0.05)
except KeyboardInterrupt:
    print('bye ...')
