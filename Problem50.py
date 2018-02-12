primes = [2]
while sum(primes) < 1000000:
    for i in xrange(primes[-1] + 1, 1000000):
        prime = 1
        for j in xrange(2, i - 1):
            if i % j == 0:
                prime = 0
        if prime == 1:
            primes.append(i)
            break
print primes
print sum(primes)

