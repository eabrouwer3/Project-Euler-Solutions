import math

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def sumOfNums(n):
    return n * (n + 1) / 2

def g(n):
    perm = [1]
    for i in [2 * x for x in xrange(1, (n+1)/2)]:
        for j in xrange(nCr(n,i)):
            perm.append(i**2)
        print perm
    for i in list(reversed(xrange(2,n))):
        for j in xrange(nCr(n, i) - 1):
            #print str(i) + " : " + str(j) + " : " + str(nCr(n,i) - 1)
            perm.append((i+1)**2)
    print perm
    print sum(perm)
    print math.factorial(n)
    print float(sum(perm))/math.factorial(n)

print nCr(7, 2) * nCr(5, 3)
print nCr(7, 3) * nCr(6, 2)

g(3)
g(5)
g(4)
#g(20)

