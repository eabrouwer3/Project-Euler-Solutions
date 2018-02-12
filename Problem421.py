import math
from ctypes import c_longlong as ll

def isPrime(n):
    if n==1: return False
    elif n<4: return True
    elif n % 2==0: return False
    elif n<9: return True
    elif n % 3==0: return False
    else:
        r=math.floor(float(n)**float(float(1)/float(2)))
        f=5
        while f<=r:
            if n % f==0: return False
            if n % (f+2)==0: return False
            f=f+6
    return True

ans = 0

for i in range(int(600851475143/2), 600851475143):
    if isPrime(i):
        ans = i

print(ans)
