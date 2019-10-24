#!/usr/bin/env python3

import math

def magnitude(v):
    return math.sqrt(sum(map(lambda x: x * x, v)))

def normalize(v):
    m = magnitude(v)
    return map(lambda x: x / m, v) 
