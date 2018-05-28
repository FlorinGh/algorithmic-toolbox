#Uses python3

import sys

def getKey(item):
    return str(item)[0]

def largest_number(a):
    '''build the largest number from a list on integers'''
    # sort values in the list based on the first digit
    digits=[]
    numbers = []
    
    for i in range(len(a)):
        if int(a[i]) < 10:
            digits.append(a[i])
        else:
            numbers.append(a[i])
    
    digits = sorted(digits, key=getKey, reverse=True)
    numbers = sorted(numbers, key=getKey, reverse=True)
    a = digits + numbers
    a = sorted(a, key=getKey, reverse=True)
   
    # add all these values in a final number:
    res = ""
    for x in a:
        res += str(x)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
