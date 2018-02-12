"""import operator
import itertools
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step

def find():
    for i in numbers:
        if (n % i == 0):
            print i
            a = find2(i)
            if (a != 0):
                return a"""
            


def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


n = 600851475143L
"""j = 300425737572L
numbers = itertools.islice(itertools.count(300425737572, -1), (0-300425737572-1-1+2*(-1<0))//-1)
print find();"""

a = 0
factors = factors(n)
print list(factors)
for i in factors:
    b = isprime(i)
    if (b and i > a):
        a = i
print a
