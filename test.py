#!/usr/bin/env python

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
import math

imu = mpu9250()

def magnitude(v):
    return math.sqrt(sum(map(lambda x: x * x, v)))

def normalize(v):
    m = magnitude(v)
    return map(lambda x: x / m, v)

try:
    while True:
        a = imu.accel
        print 'Accel: {:.3f} {:.3f} {:.3f} mg'.format(*(a))
        g = imu.gyro
        print 'Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*(g))
        m = imu.mag
        print 'Magnet: {:.3f} {:.3f} {:.3f} mT'.format(*(m))
        m = imu.temp
        print 'Temperature: {:.3f} C'.format(m)
        sleep(0.1)
except KeyboardInterrupt:
    print 'bye ...'
