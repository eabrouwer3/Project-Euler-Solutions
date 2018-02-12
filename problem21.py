def d(n):
    sumo = 0
    for j in xrange(1, n/2 + 1):
        if n % j == 0:
            sumo += j
    return sumo

sums = 0
for i in xrange(2, 10001):
    if i == d(d(i)) and i != d(i):
        sums += i
print sums
