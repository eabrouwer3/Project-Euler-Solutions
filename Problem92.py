def chain(once, n):
    if n == 89 and once == 1:
        return True
    elif n == 89 and once == 0:
        s = 0
        for c in str(n):
            s = s + int(c)**2
        return chain(1, s)
    elif n == 1:
        return False
    else:
        s = 0
        for c in str(n):
            s = s + int(c)**2
        return chain(once, s)

a = 0

for i in xrange(1, 10000000):
    if chain(0, i):
        a = a + 1

print a
