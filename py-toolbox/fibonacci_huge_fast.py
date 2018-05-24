# Uses python3
import sys

def find_period(m):
    period = []
    a, b = 0, 1
    period.append(a)
    period.append(b)
    for i in range(2, m*m):
        a = b
        b = (a + period[i-2]) % m
        if a == 0 and b == 1:
            return period[0:-1]
        period.append(b)
    return period[0:-1]

def fib_huge(n, m):
    period = find_period(m)
    index = n % len(period)
    return period[index]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_huge(n, m))
