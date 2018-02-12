def f(n, k, s):
    ans = 0
    for j in range(1, min(k,s) + 1):
        if (n == 1):
            if (k >= s):
                print 1
                ans = ans + 1
            elif (k < s):
                print 01
                ans = ans + 0
        elif (s > n):
            print 02
            ans = ans + 0
        elif (n*k < s):
            print 03
            ans = ans + 0
        else:
            print 04
            ans = ans + f(n-1,j,s-j)
    return ans

print f(10, 12, 70)
