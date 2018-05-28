# Uses python3
import numpy as np
def calc_fib(n):
    if n < 2:
        return int(n)
    else:
        fib_gen = []
        fib_gen.append(0)
        fib_gen.append(1)
        for i in range(2, n+1):
            fib_gen.append(fib_gen[i-1] + fib_gen[i-2])
        return fib_gen[-1]

n = int(input())
print(calc_fib(n))
