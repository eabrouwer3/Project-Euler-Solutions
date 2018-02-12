def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

spiral = 8
j = 49
primes = 8.0
corners = 13.0
while primes * 100.0 / corners >= 10.0:
    for k in xrange(4):
        j = j + spiral
        if isprime(j):
            primes = primes + 1.0
        corners = corners + 1.0
    spiral = spiral + 2
print (str(primes * 100.0 / corners))
print spiral - 1
