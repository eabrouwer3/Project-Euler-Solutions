import itertools

def isprime(n):
    if n == 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

setsOfThree = [list(set(itertools.permutations(str(x)))) for x in xrange(1111,9999) if isprime(x)]
newSetsOfThree = []
newSetsOfThree2 = []

for l in setsOfThree:
    new = []
    for t in l:
        i = ''.join(t)
        if not len(i) < 4 and isprime(int(i)):
            new.append(i)
    if not len(new) < 3:
        newSetsOfThree.append(sorted(new))

for p in newSetsOfThree:
    new2 = list(itertools.combinations(p,3))
    newSetsOfThree2.append(new2)

for l in newSetsOfThree2:
    for t in l:
        if int(t[1]) - int(t[0]) == int(t[2]) - int(t[1]):
            print t
