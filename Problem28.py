cur = 1
curAdd = 2
ans = 0
while curAdd != 1002:
    for i in xrange(4):
        ans += cur
        cur += curAdd
    curAdd += 2
ans += cur

print ans
