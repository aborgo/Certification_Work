"""
Tests the timings between making alist and a generator
"""

from timeit import Timer
import random

def lstf():
    return [random.random() for i in range(10**6)]

def genf():
    return (random.random() for i in range(10**6))

timer = Timer('[i for i in lstf()]',"from __main__ import  lstf")
print(timer.timeit(number=1))

timer = Timer('list(lstf())',"from __main__ import lstf")
print(timer.timeit(number=1))

timer = Timer('[i for i in genf()]',"from __main__ import genf")
print(timer.timeit(number=1))

timer = Timer('list(genf())',"from __main__ import genf")
print(timer.timeit(number=1))
