#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from ahrs.filters import Madgwick
from ahrs.common import DEG2RAD
from ahrs.common import RAD2DEG
from ahrs.common.orientation import q2euler
from calibrator import DynamicCompassCalibrator
from time import sleep
import math

def rad2deg(a):
    return list(map(lambda x: x*RAD2DEG, a))

def show_rpy(v):
    print('roll:{:+10.5f}'.format(v[0]), end=' ')
    print('pitch:{:+10.5f}'.format(v[1]), end=' ')
    print('yaw:{:+10.5f}'.format(v[2]))

def show_q(q):
    print('w:{:+10.5f} x:{:+10.5f} y:{:+10.5f} z:{:+10.5f}'.format(*q))

try:
    imu = mpu9250()
    mw = Madgwick(frequency = 50, beta = 1)
    dcc = DynamicCompassCalibrator()
    q = [1, 0, 0, 0]
    while True:
        a = list(imu.accel)
        g = list(map(lambda x: x*DEG2RAD, imu.gyro))
        m = list(imu.mag)
        #m = dcc.correct(m)
        q = mw.updateIMU(g, a, q)
        #q = mw.updateMARG(g, a, [m[1], m[0], -m[2]], q)
        #show_q(q)
        a = rad2deg(q2euler(q))
        show_rpy(a)
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
