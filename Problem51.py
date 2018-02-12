import itertools


def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False


def count(begin=0):
    while True:
        yield begin
        begin += 1


class SpecialNumber(int):
    pass


for i in count(1):
    for j in xrange(0, len(str(i)) - 1):
        primes = list()
        for k in itertools.permutations(str())
            for l in xrange(0, 10):
                print i, j, k
