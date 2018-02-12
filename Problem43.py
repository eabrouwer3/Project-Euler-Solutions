def isPalindrome(n):
    for i in xrange(0, len(str(n))):
        if str(i) not in str(n):
            return False
    return True

pandigitals = []

for i in xrange(1000000000, 9999999999):
    if isPalindrome(i):
        pandigitals.append(str(i))
a = []

for j in pandigitals:
    if j[1:3] % 2 == 0:
        if j[2:4] % 3 == 0:
            if j[3:5] % 5 == 0:
                if j[4:6] % 7 == 0:
                    if j[5:7] % 11 == 0:
                        if j[6:8] % 13 == 0:
                            if j[7:9] % 15 == 0:
                                a.append(int(j))
                            break
                        break
                    break
                break
            break
        break

print a
print sum(a)
