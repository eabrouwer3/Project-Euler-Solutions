def isPrime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def isPalindrome(n):
    for i in xrange(1, len(str(n)) + 1):
        if str(i) not in str(n):
            return False
    return True

a = 0

for i in xrange(1234,999999999):
    if isPalindrome(i):
        if isPrime(i):
            print i
