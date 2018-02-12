"""def getTriangles(i):
    return [[i, a, b, c] for a in xrange(1, i+1) for b in xrange(1, i+1) for c in xrange(1, i+1) if a + b + c == i if a < b if b < c if a**2 + b**2 == c**2]

def getSolutions(triangles):
    ans = []
    for triangle in triangles:
        i, a, b, c = triangle
        if a**2 + b**2 == c**2 and a + b + c == i:
            ans.append([i, a, b, c])
    return ans

answer = []
for i in xrange(1, 1001):
    print i
    solutions =
    if len(solutions) > len(answer):
        answer = solutions
        print answer"""

# print [[i, a, b, c] for i in xrange(1, 1001) for c in xrange(i/2, i) for a in xrange(i/2, c) for b in xrange(i/2, c)  if a + b + c == i if a < b if b < c if a**2 + b**2 == c**2]

# All answers in this array
answers = []
# Integral side a
a = 1
# Integral side b
b = 2
# highest perimeter
p = 0
# While the highest perimeter is less that 2000
while p <= 10000:
    # Find c^2
    c2 = a**2 + b**2
    # Find curP (current perimeter)
    curP = a + b + c2**0.5
    # If it's a whole number
    if "." not in str(curP)[:len(str(curP)) - 2] and p <= 1000 and b < c2**0.5:
        # put it at the end of the answers
        answers.append(curP)
    if curP > p:
        # if the current perimeter is more than the highets one, set it as the highest one
        p = curP
    # increment a and then maybe b
    a += 1
    if a == b:
        b += 1
        a = 1

print sorted([[answers.count(p), p] for p in answers])
print max([[answers.count(p), p] for p in answers])
