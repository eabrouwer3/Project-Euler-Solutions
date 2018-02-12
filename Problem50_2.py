def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

primes = []

for i in xrange(2, 1000000):
    if isprime(i):
        primes.append(i)

j = 2
k = 0
ans = 0

print len(primes)

while j < len(primes):
    thing = sum(primes[k:k+j])
    stuff = len(primes[k:k+j])
    if stuff > ans and isprime(thing) and thing < 1000000:
        print str(stuff) + " : " + str(thing)
        ans = stuff
    k = k + 1
    if k >= len(primes) - 1 or thing > 1000000:
        j = j + 1
        k = 0
