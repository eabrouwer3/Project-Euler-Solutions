ans = 0
h = 1
g = 2
f = 5
e = 10
d = 20
c = 50
b = 100
a = 200
cur = [0,0,0,0,0,0,0,1]
vals = [h,g,f,e,d,40,b,a]
while cur != [1,0,0,0,0,0,0,0]:
    curCom = cur[0] * a + cur[1] * b + cur[2] * c + cur[3] * d + cur[4] * e + cur[5] * f + cur[6] * g + cur[7] * h
    if curCom == 200:
        print cur
        ans = ans + 1
    cur[7] += 1
    for piece in cur:
        if piece == vals[cur.index(piece)] + 1:
            cur[cur.index(piece) - 1] += 1
            cur[cur.index(piece)] = 0
    if cur == [0,0,0,0,0,0,0,200]:
        cur = [0,0,0,0,0,0,1,0]
    if cur == [0,0,0,0,0,0,100,0]:
        cur = [0,0,0,0,0,1,0,0]
    if cur == [0,0,0,0,0,40,0,0]:
        cur = [0,0,0,0,1,0,0,0]
    if cur == [0,0,0,0,20,0,0,0]:
        cur = [0,0,0,1,0,0,0,0]
    if cur == [0,0,0,10,0,0,0,0]:
        cur = [0,0,1,0,0,0,0,0]
    if cur == [0,0,5,0,0,0,0,0]:
        cur = [0,1,0,0,0,0,0,0]
    if cur == [0,2,0,0,0,0,0,0]:
        cur = [1,0,0,0,0,0,0,0]

print ans + 1
