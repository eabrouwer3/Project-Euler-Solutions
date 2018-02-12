a = 0

for x in xrange(1,100):
    for y in xrange(1,100):
        if len(str(x**y)) == y:
            a = a + 1

print a
