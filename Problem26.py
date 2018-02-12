from decimal import *
from operator import itemgetter
import sys
sys.setrecursionlimit(10004)
getcontext().prec = 10004

def findRepeating(num, denominator):
    string = str(num)[2:]
    end = 0
    i = 0
    repeated = ''
    while end == 0:
        i += 1
        if string[:i] == string[i+1:i+i+1]:
            repeated = string[:i]
            end = 1
        elif i > 10000:
            end = 1
            repeated = '0'
            i = 0
    return [i, denominator]

def findRepeated(num, denominator, i):
    string = str(num)[2:]
    if string[:i] == string[i+1:i+i+1]:
        print [i, denominator]
        return [i, denominator]
    elif i > 10000:
        return 0
    else:
        return findRepeated(num, denominator, i + 1)

bits = []
for j in xrange(1, 1001):
    number = Decimal(1)/Decimal(j)
    bits.append(findRepeating(number, j, 1))
print max(bits, key=itemgetter(0))
