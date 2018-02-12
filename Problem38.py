def isPalindrome(n):
    for i in xrange(1, len(str(n)) + 1):
        if str(i) not in str(n):
            return False
    return True

a = 0

for i in xrange(1,9999):
    b = ""
    j = 1
    while len(b) < 9:
        b = b + str(i * j)
        j = j + 1
    if len(b) == 9:
        if isPalindrome(b):
            a = b

print a
