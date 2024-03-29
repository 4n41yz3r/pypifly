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
    while True:
        m = list(imu.mag)
        m[0] = m[0]
        m[1] = m[1]
        m[2] = m[2]
        print('Mag: {:.2f} {:.2f} {:.2f} mg'.format(*m))
        sleep(0.05)
except KeyboardInterrupt:
    print('bye ...')
