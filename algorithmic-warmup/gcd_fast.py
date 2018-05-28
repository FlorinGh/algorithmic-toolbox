# Uses python3
import sys

def gcd_fast(a, b):
    gcd = 1
    a, b = max(a, b), min(a, b)
    if b == 0:
        gcd = a
    else:
        gcd = gcd_fast(b, a % b)

    return gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))
