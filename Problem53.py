import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

a = 0

for n in xrange(23, 101):
    for r in xrange(1, n + 1):
        ncr = nCr(n, r)
        if ncr > 1000000:
            a = a + 1

print a
