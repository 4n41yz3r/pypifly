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
    f = IterableFilter(MedianFilter, 10)
    clb = DynamicCompassCalibrator()
    clb.min = [-4000, -4000, -4000]
    clb.max = [4000, 4000, 4000]
    while True:
        m = imu.mag
        f.take(clb.correct(m))
        if f.new:
            print('Mag: {:.3f} {:.3f} {:.3f} mg'.format(*(f.value)))
            print(clb.min)
            print(clb.max)
            print(clb.offset)
            print(clb.scale)
        sleep(0.01)
except KeyboardInterrupt:
    print('bye ...')
