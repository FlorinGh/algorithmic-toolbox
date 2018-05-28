# Uses python3
import sys

# Creating the list of fibonacci last digits
fib_last = []
fib_last.append(0)
fib_last.append(1)
for i in range(2, 60):
    fib_last.append((fib_last[i-1] + fib_last[i-2])%10)
	
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(sum(fib_last[from_%60: (to+1)%60])%10)