# Uses python3
import sys

import math
def optimal_summands(s):
    # returns a list of numbers that sum up to s
    # the numbers in the list are always ascending
    n = int(math.sqrt(2*s))
    n = int(math.sqrt(2*s-n))
    
    optimal_summands = []
    for i in range(1, n+1):
        optimal_summands.append(i)
    optimal_summands[-1] += s - sum(optimal_summands) 
    
    return optimal_summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
