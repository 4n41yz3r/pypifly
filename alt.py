#!/usr/bin/env python3

import time
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

class Altimeter:
    def __init__(self):
        bus = SMBus(1)
        self.bmp280 = BMP280(i2c_dev=bus)
        self.baseline = 0

    def get_baseline(self, baseline_size = 100, delay = 0.01):
        print("Collecting {:d} baseline values each {:.3f} seconds. Do not move the sensor!".format(baseline_size, delay))
        baseline_values = []
        for i in range(baseline_size):
            pressure = self.bmp280.get_pressure()
            baseline_values.append(pressure)
            time.sleep(delay)
        self.baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])

    def demo(self):
        print('Calculates relative altitude from pressure. Press Ctrl+C to exit!')
        self.get_baseline()        
        while True:
            altitude = self.bmp280.get_altitude(qnh=self.baseline)
            print('Relative altitude: {:05.2f} metres'.format(altitude))
            time.sleep(0.5)

a = Altimeter()
a.demo()
