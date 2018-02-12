ans = 0
ansN = 0

def isprime(n):
    for x in range(2, int(abs(n)**0.5)+1):
        if abs(n) % x == 0:
            return False
    return True

def findConPrimes(pair, n):
    if not isprime(n**2 + (pair[0] * n) + pair[1]):
        return n
    else:
        n += 1
        return findConPrimes(pair, n)

abPairs = [[a, b] for a in xrange(-999, 1000) for b in xrange(-999, 1000)]
for pair in abPairs:
    n = findConPrimes(pair, 0)
    if n > ansN:
        print n
        ansN = n
        ans = pair[0] * pair[1]

print ans
print ansN
