cur = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,12,12,12,12,11]
a = 0
while (cur != [12,12,12,12,12,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
    cur[19] = cur[19] + 1
    if (cur[19] == 13):
        cur[19] = 1
        cur[18] = cur[18] + 1
    if (cur[18] == 13):
        cur[18] = 1
        cur[17] = cur[17] + 1
    if (cur[17] == 13):
        cur[17] = 1
        cur[16] = cur[16] + 1
    if (cur[16] == 13):
        cur[16] = 1
        cur[15] = cur[15] + 1
    if (cur[15] == 13):
        cur[15] = 1
        cur[14] = cur[14] + 1
    if (cur[14] == 13):
        cur[14] = 1
        cur[13] = cur[13] + 1
    if (cur[13] == 13):
        cur[13] = 1
        cur[12] = cur[12] + 1
    if (cur[12] == 13):
        cur[12] = 1
        cur[11] = cur[11] + 1
    if (cur[11] == 13):
        cur[11] = 1
        cur[10] = cur[10] + 1
    if (cur[10] == 13):
        cur[10] = 1
        cur[9] = cur[9] + 1
    if (cur[9] == 13):
        cur[9] = 1
        cur[8] = cur[8] + 1
    if (cur[8] == 13):
        cur[8] = 1
        cur[7] = cur[7] + 1
    if (cur[7] == 13):
        cur[7] = 1
        cur[6] = cur[6] + 1
    if (cur[6] == 13):
        cur[6] = 1
        cur[5] = cur[5] + 1
    if (cur[5] == 13):
        cur[5] = 1
        cur[4] = cur[4] + 1
    if (cur[4] == 13):
        cur[4] = 1
        cur[3] = cur[3] + 1
    if (cur[3] == 13):
        cur[3] = 1
        cur[2] = cur[2] + 1
    if (cur[2] == 13):
        cur[2] = 1
        cur[1] = cur[1] + 1
    if (cur[1] == 13):
        cur[1] = 1
        cur[0] = cur[0] + 1
    b = list(cur)
    b.sort(reverse=True)
    if (sum(b[:10]) == 70):
        a = a + 1
print a
