# Uses python3
# ask for n input: the number of integers
n = int(input())

# ask for the list of numbers
a = [int(x) for x in input().split()]

# check if the list is the expected length
assert(len(a) == n)

# initialize result
result = 0

# initialize index
index = 0

# search for the index of the max number in the list
for i in range(1, n):
    if a[i] > a[index]:
        index = i

# swap the last number with the max number
a[-1], a[index] = a[index], a[-1]
        
# reset index value
index = 0

# search the index of the max number in list excluding last number
for i in range(1, len(a)-1):
    if a[i] > a[index]:
        index = i

# swap the second last number with the second biggest 
a[-2], a[index] = a[index], a[-2]

# result is the sum of the last two values in the list
result = a[-1] * a[-2]

print(result)
