i = 1
end = 0
while end == 0:
    i1 = i
    i2 = 2 * i
    i3 = 3 * i
    i4 = 4 * i
    i5 = 5 * i
    i6 = 6 * i
    if sorted(str(i1)) == sorted(str(i2)) == sorted(str(i3)) == sorted(str(i4)) == sorted(str(i5)) == sorted(str(i6)):
        end = 1
    else:
        i += 1

print i
