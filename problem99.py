def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

f = file("base_exp.txt", 'r')

atob = [[a for a in b.split(",")] for b in f.read().split("\n")]

max = [1,1]
lineNum = 0
i = 1
for cur in atob:
    hcfb = gcd(int(max[0]), int(cur[0]))
    hcfe = gcd(int(max[1]), int(cur[1]))
    newExp1 = int(max[1]) / hcfe
    newExp2 = int(cur[1]) / hcfe
    newBase1 = int(max[0]) / hcfb
    newBase2 = int(cur[0]) / hcfb
    if newBase2**newExp2 > newBase1**newExp1:
        print str(newBase2) + "^" + str(newExp2) + " : " + str(newBase1) + "^" + str(newExp1)
        print i
        max = cur
        lineNum = i
    i = i + 1

print max
print lineNum
