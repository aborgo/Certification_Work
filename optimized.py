"""
Calculates the groffle speed of a knurl widget 
of average density given by user input.

Optimized by Adam Borgo, but not created.
""" 

from math import log 
from timeit import Timer

def groffle_slow(mass, density): 
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_fast(mass, density): 
    total = 0.0
    masslog = log(mass * density) 
    for i in range(1,10001):
        total += masslog/i

    return total

mass = 2.5 
density = 12.0 

assert(groffle_slow(mass, density)==groffle_fast(mass, density))

timer = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density")
time1 = timer.timeit(number=1000)
print("time:", time1)

timer = Timer("total = groffle_fast(mass, density)", 
 "from __main__ import groffle_fast, mass, density") 
time2 = timer.timeit(number=1000)
print("time:", time2)
time = str((time2/time1)*100)[:4]
print('Time reduced to {}%'.format(time))
