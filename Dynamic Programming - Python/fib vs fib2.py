from timeit import timeit

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    n2, n1 = 0, 1
    for i in range(n-2): 
        n2, n1 = n1, n1 + n2
    return n2+n1

print timeit(lambda:fib(10), number = 100000)
print timeit(lambda:fib2(10), number = 100000)
