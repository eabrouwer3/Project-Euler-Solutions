def f(n, k, s):
    ans = 0
    if n == 1:
        return int(k >= s)

    for j in range(1, min({k,s}) + 1):
        if n*k >= s:
            ans += f(n-1,j,s-j)
    return ans

print f(10, 12, 70)
