def f(n, p, k, t):
    return sum(sum(1 if n == 3 else
                   (0 if k == 1 else
                    (1.0/36) * f(n-1, p_prime, k-1, t-(max(p_prime,i))))
                    for i in xrange(1, 7))
                   for p_prime in xrange(1, 7))

print sum(f(5,j,3,15) for j in xrange(1, 7))
