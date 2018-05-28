# Uses python3
from sys import stdin

fib_last = []
fib_last.append(0)
fib_last.append(1)

fib_last_sq = []
fib_last_sq.append(0)
fib_last_sq.append(1)

for i in range(2, 60):
    val = ((fib_last[i-1] + fib_last[i-2])%10)
    fib_last.append(val%10)
    fib_last_sq.append((val**2)%10)

if __name__ == '__main__':
    n = (int(stdin.read())+1)%60
    print(sum(fib_last_sq[:n])%10)
