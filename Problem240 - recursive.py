def combinations(n, k):
    """
    Return C(n, k), the number of combinations of `k` out of `n`.
    """
    c = 1
    k = min(k, n - k)
    for i in xrange(1, k + 1):
        c *= (n - k + i)
        c //= i
    return c

@memoized
def T(n, d, k, t):
    """
    Return the number of ways `n` distinguishable `d`-sided dice can
    be rolled so that the top `k` dice sum to `t`.
    """
    # Base cases
    if ???: return 1
    if ???: return 0

    # Divide and conquer. Let N be the maximum number of dice that
    # can roll exactly d.
    N = ???
    return sum(combinations(n, i)
               * T(n - i, d - 1, ???)
               for i in xrange(N + 1))

print T(5, 6, 3, 15)

def f(n, k, s):
"""
f(n) = 
"""
    ans = 0
    if n == 1:
        return int(k >= s)

    for j in range(1, min({k,s}) + 1):
        print j
        if n*k >= s:
            ans += f(n-1,j,s-j)
    return ans
