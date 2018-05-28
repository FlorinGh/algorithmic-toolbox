# Uses python3
import sys

def get_change(m):
    numCoins = 0
    
    numCoins += int(m/10)
    m = (m % 10)
    
    numCoins += int(m/5)
    m = m % 5
    
    numCoins += m
    
    return numCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
