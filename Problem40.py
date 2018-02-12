a = 0
b = '1'
d1 = 1
d10 = 0
d100 = 0
d1000 = 0
d10000 = 0
d100000 = 0
d1000000 = 0
cur = 2
while len(b) < 10:
    b += str(cur)
    cur += 1
d10 = int(b[9])
while len(b) < 100:
    b += str(cur)
    cur += 1
d100 = int(b[99])
while len(b) < 1000:
    b += str(cur)
    cur += 1
d1000 = int(b[999])
while len(b) < 10000:
    b += str(cur)
    cur += 1
d10000 = int(b[9999])
while len(b) < 100000:
    b += str(cur)
    cur += 1
d100000 = int(b[99999])
while len(b) < 1000000:
    b += str(cur)
    cur += 1
d1000000 = int(b[999999])
print str(d1) + ' ' + str(d10) + ' ' + str(d100) + ' ' + str(d1000) + ' ' + str(d10000) + ' ' + str(d100000) + ' ' + str(d1000000)
print str(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)
    
