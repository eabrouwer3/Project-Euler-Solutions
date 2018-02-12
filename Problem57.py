class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

a = 0

for i in xrange(1,1000):
    cur = Fraction(3,2)
    for j in xrange(1,i):
        cur.num = cur.num + cur.denom
        tempnum = cur.num
        cur.num = cur.denom
        cur.denom = tempnum
        cur.num = cur.num + cur.denom
    if len(str(cur.num)) > len(str(cur.denom)):
        a = a + 1

print a
        
