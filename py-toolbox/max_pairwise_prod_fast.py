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
    if a[i] > a[index1]:
        index1 = i

if index1 == 0:
    index2 = 1
else:
    index2 = 0
        
for i in range(1, n):
    if ((a[i] != a[index1]) and (a[i] > a[index2])):
        index2 = i
        
result = a[index1] * a[index2]
print(result)
