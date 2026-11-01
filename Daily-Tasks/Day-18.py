# 1- Write a Python program to find the key that has the maximum value in a dictionary.
d = {'a': 10, 'b': 50, 'c': 30}  # b
max_value = 0
max_key = 0
for i in d:
    if d[i] > max_value:
        max_value = d[i]
        max_key = i
print(max_key)



# 2- Write a Python program to remove duplicate values from a dictionary and create a new dictionary containing only unique values.
d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}  # {'a': 10, 'b': 20, 'd': 30}
new_dic = {}
for i in d:
    if d[i] not in new_dic.values():
        new_dic[i] = d[i]
print(new_dic)



# 3- Write a Python program to sort a dictionary in ascending order based on its keys.
d = {'c': 3, 'a': 1, 'b': 2}  # {'a': 1, 'b': 2, 'c': 3}
new_dic = {}
for i in sorted(d):
    new_dic[i] = d[i]
print(new_dic)



# 4- Write a Python program to find all repeated elements in a list and count how many times each element occurs using a dictionary.
lst = [1, 2, 3, 2, 4, 1, 5, 2]   # 1 repeated 2 times
                                 # 2 repeated 3 times
frequency = {}
for i in lst:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] = 1
for i in frequency:
    if frequency[i] > 1:
        print(i, 'repeated ', frequency[i], 'times')




# 5- Write a Python program to merge two dictionaries into a single dictionary.
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merged_dic = {**d1, **d2}
print(merged_dic)



# 6- Write a Python program to create a set containing all possible sums by adding one element from the first set and one element from the second set.
A = {1, 3}
B = {2, 4}  # {3, 5, 7}
new_set = set()
for i in A:
    for j in B:
        new_set.add(i+j)
print(new_set)




# 7- Write a Python program to identify the missing elements between the smallest and largest elements of the union of two sets.
A = {2, 5, 8}
B = {4, 10}   # {3, 6, 7, 9}
union_set = A.union(B)
missing_ele = set()
smallest = min(union_set)
largest = max(union_set)
for i in range(smallest, largest+1):
    if i not in union_set:
        missing_ele.add(i)
print(missing_ele)