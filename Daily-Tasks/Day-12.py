# 1- Write a Python program to count the number of elements in an unsorted list that are less than or equal to a given number x.?
arr = [10, 1, 2, 8, 4, 5] # 5
x = 9
count = 0
for i in arr:
    if x == i or x > i :
        count+=1
print(count)


# 2- Write a Python program that takes a list of integers and two elements, x and y. Return the element that occurs more frequently in the list. If both elements have the same frequency, return the smaller element.?
arr = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
x = 4
y = 5
obj = {}
for i in arr:
    if x == i or y == i:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
max_frequency = 0
if obj[x] == obj[y]:
    if x > y:
        max_frequency = y
    else:
        max_frequency = x
else:
    if obj[x] > obj[y]:
        max_frequency = x
    else:
        max_frequency = y
print(max_frequency)


# 3- Write a Python program to determine whether a subsequence with an odd sum exists in a given list of integers. If such a subsequence exists, return the maximum possible odd sum. If no odd-sum subsequence can be formed, return -1.
arr = [4, -3, 3, -5]
max_odd_sum = -1

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        sum = arr[i] + arr[j]
        if sum > max_odd_sum:
            if sum%2 != 0:
                max_odd_sum = arr[i] + arr[j]
print(max_odd_sum)