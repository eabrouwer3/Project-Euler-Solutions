def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

abundantNums = []

for i in xrange(1, 28124):
    if sum(sorted(list(factors(i)))[:len(factors(i)) - 1]) > i:
        abundantNums.append(i)

pairSums = []
for j in abundantNums:
    for k in abundantNums:
        pairSums.append(j+k)

pairSums = list(set(pairSums))
ans = []
for l in xrange(1, 28124):
    if l not in pairSums:
        ans.append(l)

print sum(ans)
