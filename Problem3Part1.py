from ctypes import c_longlong

class ll(int):
    def __new__(cls, n):
        return int.__new__(cls, c_longlong(n).value)

    def __add__(self, other):
        return ll(super().__add__(other))

    def __radd__(self, other):
        return ll(other.__add__(self))

    def __sub__(self, other):
        return ll(super().__sub__(other))

    def __rsub__(self, other):
        return ll(other.__sub__(self))

def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
        return True

n = 600851475143L
print isprime(n)


