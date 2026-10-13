# 1- Write a Python program to find the first repeated element in a list?
list = [4, 2, 7, 3, 2, 5, 7]
# Approach-1
'''
found = False
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            print(list[i])
            found= True
            break
    if found:
        break
'''
# Approach-2
seen = set()
for i in list:
    if i in seen:
        print(i)
        break
    else:
        seen.add(i)



# 2- Write a Python program to find the pair of elements with the maximum sum in a list?
list = [10, 25, 5, 40, 30]
sum = 0
pair_list = []
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if sum < list[i] + list[j]:
            sum = list[i] + list[j]
            pair_list = [list[i],list[j]]
print(sum)
print(pair_list)



# 3- Write a Python program to find all duplicate elements in a list?
list =  [1, 2, 3, 2, 4, 5, 1, 6]
duplicate_list = []
seen = set()
for i in range(len(list)):
    if list[i] in seen:
        duplicate_list.insert(0,list[i])
    else:
        seen.add(list[i])
print(duplicate_list)



# 4- Write a Python program to rotate a list to the right by one position?
list = [10, 20, 30, 40, 50]  # [50,10,20,30,40]
k = 2
k = k%len(list)
for i in range(0,k):
    list.insert(0, list.pop())
print(list)



# 5- Write a Python program to swap the first and last elements of a list?
list = [5, 10, 15, 20, 25]  # [25,10,15,20,5]
list[-1], list[0] = list[0], list[-1]
print(list)



# 6- Write a Python program to find all pairs of elements whose sum is equal to a given target value?
list = [1, 2, 3, 4, 5, 6, 7]  # [[2,7], [3,6], [4,5]]
target = 9
pair_list = []
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if target == list[i]+list[j]:
            pair_list.append([list[i], list[j]])
print(pair_list)

