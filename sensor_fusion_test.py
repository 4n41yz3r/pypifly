#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from ahrs.filters import Madgwick
from ahrs.common import DEG2RAD
from time import sleep
import math

try:
    imu = mpu9250()
    mw = Madgwick(frequency = 10)
    q = [1, 0, 0, 0]
    while True:
        a = list(imu.accel)
        g = list(map(lambda x: x*DEG2RAD, imu.gyro))
        m = list(imu.mag)
        q = mw.updateIMU(g, a, q)
        #q = mw.updateMARG(g, a, m, q)
        print('w:{:.3f} x:{:.3f} y:{:.3f} z:{:.3f}'.format(*(q)))
        sleep(0.1)
except KeyboardInterrupt:
    print('bye ...')
