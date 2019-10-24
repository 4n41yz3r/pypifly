#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
import math

imu = mpu9250()

try:
    while True:
        a = imu.accel
        print('{:.3f} {:.3f} {:.3f} mg '.format(*(a)), end='')
        g = imu.gyro
        print('{:.3f} {:.3f} {:.3f} dps '.format(*(g)), end='')
        m = imu.mag
        print('{:.3f} {:.3f} {:.3f} mT '.format(*(m)), end='')
        m = imu.temp
        print('{:.3f} C'.format(m))
        sleep(0.1)
except KeyboardInterrupt:
    print('bye ...')
