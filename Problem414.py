iterations = 0

def Cb(number, base):
    SToB = []
    BToS = []
    SToB.append(number)
    BToS.append(number)
    SToB[0].sort()
    BToS[0].sort(reverse=True)
    print SToB
    print BToS
    return 1
    
def sb(number, base):
    if (i == Cb(number, base) or sorted(number) == sorted(number, reverse=True)):
        return 0
    else:
        iterations = 0
        return Cb(number, base)

def S(k):
    b = 6*k+3
    a = 0
    for i in range(0,b**5):
        a + sb(convert(i, b), b)
    return a

def convert(num,n):
    new_num=[]
    current=num
    while current!=0:
        remainder=current%n
        new_num.insert(0,remainder)
        current=current/n
    length = len(new_num)
    while (length < 5):
        new_num.insert(0,0)
        length = length + 1
    return new_num

a = 0
for i in range(2,300):
    a = a + S(i)
print a
