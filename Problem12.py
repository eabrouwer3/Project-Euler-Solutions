def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

done = 0
cur = 0
curNNum = 1
while done == 0:
    cur = cur + curNNum
    curNNum += 1
    print str(cur) + " : " + str(len(factors(cur)))
    if (len(factors(cur)) >= 500):
        done = 1
