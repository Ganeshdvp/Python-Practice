# 1- Write a Python program to find the union of two sets and display the result?
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}    # {10, 20, 30, 40, 50, 60}
union = A.union(B)
print(union)



# 2- Write a Python program to find the intersection of two sets?
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}    # {30, 40}
intersection = A.intersection(B)
print(intersection)




# 3- Write a Python program to find the difference between two sets (A - B)?
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}   # {10, 20}
difference = A.difference(B)
print(difference)




# 4- You are given two lists containing tuples of integers. Write a Python program to find all tuples that are present in both lists.
list1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
list2 = [(3, 4), (7, 8), (9, 10), (1, 2)]  # [(1, 2), (3, 4), (7, 8)]
new_list = []
# Approach-1
'''for i in range(len(list1)):
    if list1[i] in list2:
        new_list.append(list1[i])
print(new_list)'''
# Approach-2
seen = set(list2)
for i in list1:
    if i in seen:
        new_list.append(i)
print(new_list)



# 5- You are given a list of tuples containing integer values. Write a Python program to find the tuple whose elements have the highest sum.
data = [(1, 2), (10, 5), (3, 4), (7, 8)]   # (7, 8)
sum = 0
new_list = []
for i in data:
    temp_sum = 0
    for j in i:
        temp_sum += j
    if temp_sum >= sum:
        sum = temp_sum
        new_list = i
print(sum)
print(new_list)