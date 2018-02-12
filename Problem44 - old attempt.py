def P(n):
    return n * (3 * n - 1) / 2

pentagonals = [P(l) for l in xrange(1, 10000)]
pensums = []
pendiffs = []
j = 0
k = 0
while k <= len(pentagonals) - 1:
    #print str(pentagonals[j]) + " : " + str(pentagonals[k])
    pensums.append((j, k, pentagonals[j] + pentagonals[k]))
    pendiffs.append(pentagonals[j] - pentagonals[k])
    j += 1
    if j > len(pentagonals) - 2:
        k += 1
        j = k

for (p, q) in zip(pensums, pendiffs):
    if p[2] in pentagonals and q in pentagonals:
        print str(j) + " : " + str(k)
    
"""a = 1
b = 1
while a < 99:
    print str(pentagonals[a] + pentagonals[b]) + " : " + str(abs(pentagonals[b] - pentagonals[a]))
    if pentagonals[a] + pentagonals[b] in pentagonals and abs(pentagonals[b] - pentagonals[a]) in pentagonals:
        print abs(pentagonals[b] - pentagonals[a])
    b += 1
    if b == 99:
        b = 1
        a += 1
"""
