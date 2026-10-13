# 1- Write a Python program to find the kth smallest element in a list without using the sort() method?
list = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

for i in range(0,len(list)-1):
    for j in range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list[k-1])




# 2- Write a Python program to move all the zeros to the end of the list while maintaining the original order of the non-zero elements?
list = [1, 2, 0, 4, 3, 0, 5, 0]
k = 0
for i in range(0,len(list)):
    if list[i]>0:
        list[k], list[i] = list[i], list[k]
        k+=1
print(list)



# 3- Write a Python program to find the maximum sum of a subarray of size k?
list = [100,200,300,400]
k = 2 
max = 0

for i in range(0,len(list)-k+1):
    total = 0
    for j in range(i, i+k):
        total+=list[j]
    if total > max :
        max = total
        
print(max)




# 4-  Write a Python program to find the maximum number of consecutive 1s?
list = [1, 1, 0, 1, 1, 1, 1, 0, 1,0] # 3
count = 0
ele = list[0]
temp_count = 0
for i in list:
    if ele == i:
        temp_count+=1
    else:
        if temp_count > count:
            count = temp_count

        temp_count = 1
        ele = i
            
print(count)