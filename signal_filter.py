#!/usr/bin/env python

class Filter:
    _length = 1
    _raw = []
    value = 0
    new = True

    def __init__(self, length, fn):
        self._length = length
        self._fn = fn

    def take(self, value):
        self._raw.append(value)
        if len(self._raw) >= self._length:
            self.value = self._fn(self._raw)
            self._raw = []
            self.new = True
        else:
            self.new = False
    
class MedianFilter(Filter):
    def __init__(self, length):
        Filter.__init__(self, length, lambda x: MedianFilter.median(x))

    @staticmethod
    def median(lst):
        quotient, remainder = divmod(len(lst), 2)
        if remainder:
            return sorted(lst)[quotient]
        return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

class IterableFilter():
    _filters = []

    def _init__(self, filter_type, length = 10):
        self._type = filter_type
        self._length = length

    def take(self, arr):
        for i in range(arr.length):
            if (self._filters[i] is None)
                self._filters[i] = self._type(self._length)
            self._filters[i].take(arr[i])

    def value(self):
        result = []
        for f in self._filters:
            result.add(f.value)
        return result

    def new(self):
        for f in self._filters:
            return f.new
        return False

