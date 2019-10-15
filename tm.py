#!/usr/bin/env python

import sys
sys.path.append('./mpu9250/mpu9250')

from mpu9250 import mpu9250
from time import sleep
import math
from signal_filter import MedianFilter

imu = mpu9250()

def magnitude(v):
    return math.sqrt(sum(map(lambda x: x * x, v)))

def normalize(v):
    m = magnitude(v)
    return map(lambda x: x / m, v)

try:
    f = MedianFilter(20)
    while True:
        a = imu.accel
        f.take(a[0])
        if f.new:
            print 'Accel: {:.3f} {:.3f} {:.3f} mg'.format(*(a))
        #g = imu.gyro
        #print 'Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*(g))
        #m = imu.mag
        #print 'Magnet: {:.3f} {:.3f} {:.3f} mT'.format(*(m))
        sleep(0.005)
except KeyboardInterrupt:
    print 'bye ...'
