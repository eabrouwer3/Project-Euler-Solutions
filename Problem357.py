def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def divisors(n):
    d = []
    for i in xrange(1, n + 1):
        if n % i == 0:
            d.append(i)
    return d

s = 0

for n in xrange(1, 100000001):
    good = True
    # print str(n) + " : " + str(divisors(n))
    for divisor in divisors(n):
        if n == 30:
            print ((divisor + n) / divisor)
        if not isprime((divisor + n) / divisor):
            good = False
    if good:
        s += n
        print s

print s
    
