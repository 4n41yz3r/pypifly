#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from madgwick_py.madgwickahrs import MadgwickAHRS
from madgwick_py.quaternion import Quaternion
from ahrs.filters import Madgwick
from ahrs.common import DEG2RAD
from ahrs.common import RAD2DEG
from ahrs.common.orientation import q2euler
from calibrator import DynamicCompassCalibrator
from time import sleep
import math

def rad2deg(a):
    return list(map(lambda x: x*RAD2DEG, a))

def show3(v):
    print('x:{:+10.5f}'.format(v[0]), end=' ')
    print('y:{:+10.5f}'.format(v[1]), end=' ')
    print('z:{:+10.5f}'.format(v[2]))

try:
    imu = mpu9250()
    mw = MadgwickAHRS(0.02, Quaternion(1, 0, 0, 0))
    dcc = DynamicCompassCalibrator()
    while True:
        a = imu.accel
        g = list(map(lambda x: x*DEG2RAD, imu.gyro))
        #m = list(imu.mag)
        #m = dcc.correct(imu.mag)
        mw.update_imu(g, a)
        #mw.update(g, a, m)
        #print('w:{:.3f} x:{:.3f} y:{:.3f} z:{:.3f}'.format(*mw.quaternion))
        ea = mw.quaternion.to_euler_angles()
        show3(rad2deg(ea))
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
