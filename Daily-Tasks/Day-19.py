# 1- Write a Python program to merge two dictionaries into a single dictionary. If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.
d1 = {'a': 1, 'b': 2}
d2 = {'b': 5, 'c': 3}   # {'a': 1, 'b': 5, 'c': 3}
# Approach-1
merged_dic = {**d1, **d2}
print(merged_dic)
# Approach-2
new_dic = d1 | d2
print(new_dic)
# Approach-3
merge_dic = {}
for i in d1:
    if i in merge_dic:
        merge_dic[i] = d1[i]
    else:
        merge_dic[i] = d1[i]
for i in d2:
    if i in merge_dic:
        merge_dic[i] = d2[i]
    else:
        merge_dic[i] = d2[i]
print(merge_dic)



# 2- Write a Python program to find all common keys present in two dictionaries and store them in a list.
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 5, 'c': 7, 'd': 9}  # ['b', 'c']
new_list = []
seen = {}
for i in d1:
    if i in seen:
        new_list.append(i)
    else:
        seen[i] = d1[i]
for i in d2:
    if i in seen:
        new_list.append(i)
    else:
        seen[i] = d2[i]
print(new_list)



# 3- Write a Python program to remove all key-value pairs from a dictionary whose value is less than 10.
d = {'a': 5, 'b': 12, 'c': 7, 'd': 20}  # {'b': 12, 'd': 20}
new_dic = {}
for i in d:
    if d[i] > 10:
        new_dic[i] = d[i]
print(new_dic)




# 4- Write a Python program to group student names based on their department using a dictionary.
students = [
    ('raju', 'CSE'),
    ('Ravi', 'ECE'),
    ('shiva', 'CSE'),
    ('Kiran', 'EEE')
]   # {'CSE': ['raju', 'shiva'],'ECE': ['Ravi'],'EEE': ['Kiran']}
new_dic = {}
for i in students:
    if i[1] in new_dic:
        new_dic[i[1]].append(i[0])
    else:
        new_dic[i[1]] = [i[0]]
print(new_dic)



# 5- Write a Python program to find the second highest value key present in a dictionary.
d = {'a': 10, 'b': 40, 'c': 25, 'd': 30}  # d
largest_val = float('-inf')
largest_key = 0
second_val = float('-inf')
second_key = 0
for i in d:
    if d[i] > largest_val:
        second_val = largest_val
        largest_val = d[i]
        smallest_key = largest_key
        largest_key = i
    elif second_val < d[i]:
        second_val = d[i]
        second_key = i
print(second_key)