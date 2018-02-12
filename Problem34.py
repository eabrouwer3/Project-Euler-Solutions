from math import *

a = 0
for i in xrange(10, 100000):
    sumCur = 0
    for j in str(i):
        sumCur += factorial(int(j))
    if sumCur == i:
        a += i
print a
