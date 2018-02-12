def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def arePrime(nums):
    for num in nums:
        if not isprime(num):
            return False
    return True

def truncate(num):
    truncations = [num]
    for i in xrange(1, len(str(num))):
        truncations.append(int(str(num)[i:]))
        truncations.append(int(str(num)[:i]))
    return truncations

for i in xrange(10, 1000000):
    if arePrime(truncate(i)) and 1 not in truncate(i):
        print i
        print truncate(i)
