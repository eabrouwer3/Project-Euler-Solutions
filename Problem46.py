def iscomposite(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return True
    return False

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def isoneprime(l):
    for n in l:
        if isprime(n):
            return True
    return False

for i in xrange(6000):
    a = 0
    l = []
    while (i % 2 is not 0 and iscomposite(i) and a is 0):
        b = 2
        while (2 * b**2) < i:
            if ((i - (2 * b**2)) > 0):
                l.append((i - (2 * b**2)))
            b = b + 1
        b = b - 1
        if not isoneprime(l):
            print str(i) + " = " + str(i - (2 * b**2)) + " + 2 * " + str(b) + "^2"
        a = 1
