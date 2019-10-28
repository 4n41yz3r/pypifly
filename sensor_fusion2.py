#!/usr/bin/env python3

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from madgwick_py.madgwickahrs import MadgwickAHRS
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
    mw = MadgwickAHRS(0.02)
    while True:
        a = list(imu.accel)
        g = list(map(lambda x: x*DEG2RAD, imu.gyro))
        m = list(imu.mag)
        mw.update_imu(g, a)
        #mw.update(g, a, m)
        #print('w:{:.3f} x:{:.3f} y:{:.3f} z:{:.3f}'.format(*mw.quaternion))
        a = mw.quaternion.to_euler_angles()
        print('x:{:.3f} y:{:.3f} z:{:.3f}'.format(*rad2deg(a)))
        sleep(0.02)
except KeyboardInterrupt:
    print('bye ...')
