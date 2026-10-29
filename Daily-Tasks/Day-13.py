# 1- Write a Python program to sort the given list in ascending order using Bubble Sort.
arr = [5, 3, 8, 1, 2]  # [1,2,3,5,8]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)



# 2- Write a Python program to sort the given list based on the absolute value of each number using Bubble Sort.
arr = [-8, 3, -2, 5, 1]  # [1,-2,3,5,-8]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if abs(arr[j]) > abs(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)



# 3- Write a Python program to find all elements greater than the average of the list.
arr = [10, 20, 30, 40, 50]  #[40,50]
avg_list = []
sum = 0
for i in arr:
    sum+= i
avg = sum/len(arr)
for i in arr:
    if avg < i:
        avg_list.append(i)
print(avg_list)



# 4- An element is a leader if it is greater than or equal to every element to its right. Write a Python program to find all leaders.
arr = [16, 17, 4, 3, 5, 2]  #[17, 5, 2]
leader_list = []

for i in range(len(arr)):
    flag = True

    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            flag = False
            break

    if flag:
        leader_list.append(arr[i])
print(leader_list)