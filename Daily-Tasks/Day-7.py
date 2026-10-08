# 1- Write a Python program to find the most frequent element in a list?
list = [1,2,3,2,4,2,5,2]  # 2
count = 0
ele = 0
for i in list:
    temp_count = 0
    for j in list:
        if i == j:
            temp_count+=1
    if count < temp_count:
        ele = i
        count = temp_count
print(ele)
print(count)



# 2- Write a Python program to find the second largest element in a list?
list = [10,20,50,40,30]
largest = 0
second = 0
for i in range(0,len(list)):
    if list[i] > largest:
        second = largest
        largest = list[i]
    if list[i] < largest and list[i] > second:
        second = list[i]
print(second)



# 3- Write a Python program to find the missing number from a list containing numbers from 1 to n?
list = [1,3,4,5]  # 2
original_sum = 0
actual_sum = 0
for i in range(0,len(list)):
    actual_sum += list[i]

for i in range(1,len(list)+2):
    original_sum += i

res = original_sum - actual_sum
print(res)



# 4- Write a Python program to rotate a list to the left by one position?
list = [1, 2, 3, 4, 5] # [2,3,4,5,1]
n = 1
# Approach-1
'''
rotated_list = []
for i in range(1,len(list)):
    rotated_list.append(list[i])
for i in range(0,n):
    rotated_list.append(list[i])
print(rotated_list)
'''
# Approach-2
k = 0
for i in range(n,len(list)):
    list[i],list[i-1] = list[i-1], list[i]
print(list)



# 5- Write a Python program to find the intersection of two lists?
list1 = [1,2,3,4]
list2 = [2,4,6,8]  # [2,4]
intersection_list = []
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i] == list2[j]:
            intersection_list.append(list1[i])
print(intersection_list)