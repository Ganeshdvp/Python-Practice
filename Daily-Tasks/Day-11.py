# 1- Given a list of integers, write a Python program to find the contiguous (continuous) subarray that has the maximum sum and print that sum.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
max_sum = float('-inf')
for i in range(len(nums)):
    temp_sum = 0
    for j in range(i,len(nums)):
        temp_sum = temp_sum + nums[j]
        if max_sum < temp_sum:
            max_sum = temp_sum
            subArray = nums[i:j+1]
print(max_sum)  # 6
print(subArray) # [4,-1,2,-1]






# 2- Given a list of integers nums and an integer k, write a Python program to find the k-th largest element in the list without using the built-in sort() or sorted() functions.
nums = [3, 2, 1, 5, 6, 4]  #5
k = 2
for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
res = nums[len(nums)-k]
print(res)


# 3- Write a Python program to count how many elements are greater than the average of the list.
list =  [10, 20, 30, 40, 50]  #2
sum = 0
for i in list:
    sum+=i
avg = sum/len(list)
count = 0
for i in list:
    if i < avg :
        count+=1
print(count)


# 4- Write a Python program to count how many numbers in a list end with the digit zero.
list =  [10, 25, 30, 44, 50, 67]  #3
count = 0
for i in list:
    if i%10 == 0:
        count+=1
print(count)



# 5- Write a Python program to find the second smallest distinct number without using sort(), sorted(), or min().
list = [8, 3, 5, 3, 1, 8]  #5

for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
k = len(list)-1
count=0
for i in range(k, 0, -1):
    if list[i] == list[i-1]:
        k-=1
    else:
        count+=1
        if count == 2:
            print(list[i])
            break
        k-=1



