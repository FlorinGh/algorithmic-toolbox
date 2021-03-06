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

def lcm_fast(a, b):
    lcm = a * b // gcd_fast(a, b)
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

