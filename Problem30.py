a = []
cur = []
for i in xrange(2, 1000000):
    for j in str(i):
        cur.append(int(j)**5)
    if sum(cur) == i:
        a.append(sum(cur))
    cur = []
print sum(a)
