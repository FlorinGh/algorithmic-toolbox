# Uses python3
import sys

def fib_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current + 1

    return current % 10
	
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_fast(n%60))
