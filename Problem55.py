def isPalindrome(i):
    if str(i) == str(i)[::-1]:
        return True

def isNotLychrel(i, cur):
    if i == 50:
        return True
    bcur = int(str(cur)[::-1])
    if isPalindrome(cur + bcur):
        return False
    else:
        return isNotLychrel(i + 1, cur + bcur)

a = 0

for i in xrange(10000):
    if isNotLychrel(1, i):
        a += 1

print a
