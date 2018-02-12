import math
cur = [1,1,1,1,1]
a = 0
inc = 0
while (cur != [6,6,6,6,6]):
    cur[4] = cur[4] + 1
    if (cur[4] == 7):
        cur[4] = 1
        cur[3] = cur[3] + 1
    if (cur[3] == 7):
        cur[3] = 1
        cur[2] = cur[2] + 1
    if (cur[2] == 7):
        cur[2] = 1
        cur[1] = cur[1] + 1
    if (cur[1] == 7):
        cur[1] = 1
        cur[0] = cur[0] + 1
    b = list(cur)
    b.sort(reverse=True)
    if (sum(b[:3]) == 15):
        a = a + 1
    print cur
print a
