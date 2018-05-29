# recursion
def fib(n):
    if n <=1:
        return n
    return fib(n - 1) + fib(n - 2)


# Dynamic programming solution.
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


import time

timer = time.perf_counter()
print(fib(6))
print(fib(100000))
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
