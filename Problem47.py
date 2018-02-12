def isprime(n):
    if i == 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def primeFactors(n):
    fs = factors(n)
    pf = []
    for f in fs:
        if isprime(f):
            pf.append(f)
    return list(set(pf) - set([1]))

for i in xrange(1000,1000000):
    if len(primeFactors(i)) == 4 and len(primeFactors(i+1)) == 4 and len(primeFactors(i+2)) == 4 and len(primeFactors(i+3)) == 4:
        print i
        print primeFactors(i)
        break
