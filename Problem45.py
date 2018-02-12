triangles = [.5 * n * (n + 1) for n in xrange(1, 100001)]
pentagonals = [.5 * n * (3 * n - 1) for n in xrange(1, 100001)]
hexagonals = [n * (2 * n - 1) for n in xrange(1, 100001)]

for triangle in triangles:
    if triangle in pentagonals and triangle in hexagonals:
        print str(triangle) + " : " + str(triangles.index(triangle)) + " : " + str(pentagonals.index(triangle)) + " : " + str(hexagonals.index(triangle))
