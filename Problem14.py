a = 0
it = 0
for j in range(1, 1000000):
    iterations = 0
    i = j
    while (i != 1):
        if (i % 2 == 0):
            i = i / 2
            iterations = iterations + 1
        else:
            i = 3 * i + 1
            iterations = iterations + 1
    if (iterations > it):
        a = j
        it = iterations
print a