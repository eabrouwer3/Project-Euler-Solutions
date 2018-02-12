import itertools

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def arePrime(rotations):
    if rotations == []:
        return True
    elif not isprime(int(''.join(map(str,rotations[0])))):
        return False
    else:
        rotations.pop(0)
        return arePrime(rotations)

def getRotations(num):
    seperated = [int(i) for i in list(str(num))]
    if len(seperated) == 1:
        return [seperated, seperated]
    rotations = []
    if len(seperated) == 2:
        a, b = seperated
        rotations.append([a, b])
        rotations.append([b, a])
        return rotations
    if len(seperated) == 3:
        a, b, c = seperated
        rotations.append([a, b, c])
        rotations.append([b, c, a])
        rotations.append([c, a, b])
        return rotations
    if len(seperated) == 4:
        a, b, c, d = seperated
        rotations.append([a, b, c, d])
        rotations.append([b, c, d, a])
        rotations.append([c, d, a, b])
        rotations.append([d, a, b, c])
        return rotations
    if len(seperated) == 5:
        a, b, c, d, e = seperated
        rotations.append([a, b, c, d, e])
        rotations.append([b, c, d, e, a])
        rotations.append([c, d, e, a, b])
        rotations.append([d, e, a, b, c])
        rotations.append([e, a, b, c, d])
        return rotations
    if len(seperated) == 6:
        a, b, c, d, e, f = seperated
        rotations.append([a, b, c, d, e, f])
        rotations.append([b, c, d, e, f, a])
        rotations.append([c, d, e, f, a, b])
        rotations.append([d, e, f, a, b, c])
        rotations.append([e, f, a, b, c, d])
        rotations.append([f, a, b, c, d, e])
        return rotations
    
ans = []
for num in xrange(2, 1000000):
    if arePrime(getRotations(num)):
        ans.append(num)

print ans
print len(ans)
