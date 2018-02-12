numS = "3608528850368400786036725"
for i in xrange(1, len(numS) + 1):
    if (int(numS[:i]) % len(numS[:i]) == 0):
        print "true"
