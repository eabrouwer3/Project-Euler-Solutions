def getLeft(ref):
    if ref == 0 or ref == []:
        return []
    row = ref[0] + 1
    if row == 15:
        return []
    col = ref[1]
    return [[row, col + 1, rows[row][col + 1]], [row, col, rows[row][col]]]

def getPredecessors(ref):
    if ref == 0 or ref == []:
        return []
    row = ref[0] - 1
    col = ref[1]
    if row == 1 or col >= row:
        return []
    a = []
    if col > 1:
        a.append([row, col - 1, rows[row][col - 1]])
    a.append([row, col, rows[row][col]])
    return a

def search(cur, paths):
    cur2 = []
    for r in cur:
        for s in getPredecessors(r):
            print s
            cur2.append(s)
        for l in paths:
            if l[-1] == r:
                for j in cur2:
                    l.append(j)
        cur2 = []

def search2(cur, paths):
    cur2 = []
    big = []
    for r in cur:
        for s in getPredecessors(r):
            if s not in cur2:
                cur2.append(s)
        if cur2 != []:
            big.append(max(cur2, key=lambda j:int(j[2])))
            cur2 = []
    for l in getSuccessors(big):
        print l
    
    

string = "75\n95 64\n17 47 82\n18 35 87 10\n20 04 82 47 65\n19 01 23 75 03 34\n88 02 77 73 07 63 67\n99 65 04 28 06 16 70 92\n41 41 26 56 83 40 80 70 33\n41 48 72 33 47 32 37 16 94 29\n53 71 44 65 25 43 91 52 97 51 14\n70 11 33 28 77 73 17 78 39 68 17 57\n91 71 52 38 17 14 91 43 58 50 27 29 48\n63 66 04 68 89 53 67 30 73 16 69 87 40 31\n04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
rows = [dict(list(enumerate(s.split(), start=1))) for s in string.split("\n")]

"""cur = [[14, k + 1, rows[14][j]] for (j, k) in zip(rows[14], range(15))]"""
paths = [[[14, k + 1, rows[14][j]]] for (j, k) in zip(rows[14], range(15))]
cur = [[15, k + 1, '0'] for k in range(16)]
search2(cur, paths)
