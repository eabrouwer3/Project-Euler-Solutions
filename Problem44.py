import math

def P(n):
    return n * (3 * n - 1) / 2
def n(P):
    return ((24 * P + 1)**.5 + 1) / 6

pentagonals = [P(l) for l in xrange(1, 10000)]
difs = []

for j in pentagonals:
    for k in pentagonals[pentagonals.index(j):]:
        if str(n(j + k))[-2:] == '.0':
            print (j,k,j+k)
            if str(n(math.fabs(k-j)))[-2:] == '.0':
                print (j,k,j+k,k-j)
                difs.append(k-j)

print difs
