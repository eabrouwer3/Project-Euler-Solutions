from timeit import timeit
import math

def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n - 1)

for i in range(1,11):
    print timeit(lambda:fact(i), number=10)
    print timeit(lambda:math.factorial(i), number=10)
