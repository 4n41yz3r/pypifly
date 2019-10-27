#!/usr/bin/env python3

class DynamicCompassCalibrator:
    def __init__(self):
        self.min = [0] * 3
        self.max = [0] * 3
        self.offset = [0] * 3
        self.scale = [1] * 3
        self._new_extremes = False

    def correct(self, sensor):
        self._update_extremes(sensor)
        self._calc()
        return self._adjust(sensor)

    def _update_extremes(self, sensor):
        for i in range(3):
            if sensor[i] < self.min[i]:
                self.min[i] = sensor[i]
                self._new_extremes = True
            if sensor[i] > self.max[i]:
                self.max[i] = sensor[i]
                self._new_extremes = True

    def _calc(self):
        if self._new_extremes:
            self._calc_offsets()
            self._calc_scale()
            self._new_extremes = False

    def _calc_offsets(self):
        self.offset = [ \
            (self.max[0] + self.min[0]) / 2,
            (self.max[1] + self.min[1]) / 2,
            (self.max[2] + self.min[2]) / 2 \
        ]

    def _calc_scale(self):
        avg_delta = [ \
            (self.max[0] - self.min[0]) / 2,
            (self.max[1] - self.min[1]) / 2,
            (self.max[2] - self.min[2]) / 2 \
        ]
        bal = (avg_delta[0] + avg_delta[1] + avg_delta[2]) / 3
        self.scale = [ \
            bal / avg_delta[0],
            bal / avg_delta[1],
            bal / avg_delta[2] \
        ]

    def _adjust(self, sensor):
        return [ \
            (sensor[0] - self.offset[0]) * self.scale[0],
            (sensor[1] - self.offset[1]) * self.scale[1],
            (sensor[2] - self.offset[2]) * self.scale[2] \
        ]
