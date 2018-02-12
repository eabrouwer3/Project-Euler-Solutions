import time

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False

def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def primefactors(n):
    return [p for p in xrange(2,n) if p not in [np for i in xrange(2, int(n**0.5)) for np in xrange(i * 2, n, i)]]

def isrelativelyprime(x, n):
    if x % n != 0:
        print factors(x)
        print "prime: " + str(primefactors(x))
        xf = factors(x)[1:]
        for i in factors(n)[1:]:
            if i in xf:
                return False
        return True
    return False

a = 0.0
b = 0
for n in xrange(1,1000001):
    start = time.time()
    if not isprime(n):
        relativePrimes = []
        mid = time.time()
        for i in xrange(1,(n / 2) + 1):
            if isrelativelyprime(n,i):
                relativePrimes.append(i)
        mid2 = time.time()
        relativePrimes.insert(0, 1)
        if float(n)/float(len(relativePrimes)) > a:
            a = float(n)/float(len(relativePrimes))
            b = n
            print str(a) + " : " + str(b)
    finish = time.time()
    #print "fin: " + str(finish - start)
    #print "mid: " + str(mid2 - mid)
    
print a
print b
