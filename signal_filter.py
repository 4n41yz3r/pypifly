#!/usr/bin/env python

class Filter:
    _length = 1
    _raw = []
    _value = 0
    _new = True

    def __init__(self, length, fn):
        self._length = length
        self._fn = fn

    def take(self, value):
        self._raw.append(value)
        if len(self._raw) >= self._length:
            self._value = self._fn(self._raw)
            self._raw = []
            self._new = True
        else:
            self._new = False

    @property
    def value(self):
        return self._value

    @property
    def new(self):
        return self._new
    
class MedianFilter(Filter):
    def __init__(self, length):
        Filter.__init__(self, length, lambda x: MedianFilter.median(x))

    @staticmethod
    def median(lst):
        quotient, remainder = divmod(len(lst), 2)
        if remainder:
            return sorted(lst)[quotient]
        return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

class AverageFilter(Filter):
    def __init__(self, length):
        Filter.__init__(self, length, lambda x: AverageFilter.average(x))

    @staticmethod
    def average(lst):
        return sum(lst) / len(lst)

class IterableFilter():
    _filters = []

    def __init__(self, filter_type, length = 10):
        self._type = filter_type
        self._length = length

    def take(self, arr):
        if len(self._filters) < len(arr):
            self._filters = [None] * len(arr)
        for i in range(len(arr)):
            if self._filters[i] is None:
                self._filters[i] = self._type(self._length)
            self._filters[i].take(arr[i])

    @property
    def value(self):
        result = []
        for f in self._filters:
            result.append(f.value)
        return result

    @property
    def new(self):
        for f in self._filters:
            return f.new
        return False

