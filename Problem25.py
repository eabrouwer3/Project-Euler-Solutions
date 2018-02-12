i = 1
j = 1
inc = 2
while (len(str(i)) < 1000):
    k = i
    i = i + j
    j = k
    inc = inc + 1
print inc
