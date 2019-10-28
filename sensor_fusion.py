#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from ahrs.filters import Madgwick
from ahrs.common import DEG2RAD
from ahrs.common import RAD2DEG
from ahrs.common.orientation import q2euler
from time import sleep
import math

def rad2deg(a):
    return list(map(lambda x: x*RAD2DEG, a))

try:
    imu = mpu9250()
    mw = Madgwick(frequency = 50, beta = 1)
    q = [1, 0, 0, 0]
    while True:
        a = list(imu.accel)
        g = list(map(lambda x: x*DEG2RAD, imu.gyro))
        m = list(imu.mag)
        q = mw.updateIMU(g, a, q)
        #q = mw.updateMARG(g, a, m, q)
        #print('w:{:.3f} x:{:.3f} y:{:.3f} z:{:.3f}'.format(*q))
        a = q2euler(q)
        print('x:{:.3f} y:{:.3f} z:{:.3f}'.format(*rad2deg(a)))
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
