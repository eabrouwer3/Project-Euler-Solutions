ans = 0

for a in xrange(1, 101):
    for b in xrange(1, 101):
        c = a**b
        thing = sum([int(d) for d in str(c)])
        if thing > ans:
            ans = thing

print ans
