a = []
for i in range(1000000):
    if str(i) == str(i)[::-1]:
        binary = str(bin(i))[2:]
        if binary == binary[::-1]:
            a.append(i)
print sum(a)
