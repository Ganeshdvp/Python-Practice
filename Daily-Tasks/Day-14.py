# 1- Write a Python program to merge two lists into one list without duplicate elements, preserving their original order.
list1 = [1, 2, 3, 2]
list2 = [3, 4, 5, 1]   # [1, 2, 3, 4, 5]
seen = set()
results = []
for i in list1+list2:
    if i not in seen:
        results.append(i)
        seen.add(i)
print(results)



# 2- Write a Python program to check whether any number in a list is negative using any().
list = [10, 20, -5, 30] # True
res = any(i<0 for i in list)
print(res)



# 3- Write a Python program to check whether all numbers in a list are even.
list = [2, 4, 6, 8]  # True
res = all(i%2==0 for i in list)
print(res)



# 4- Write a Python program to check whether any number in a list is greater than a given value x.
list = [10, 20, 30, 40]  # True
x = 25
res = any(x<i for i in list)
print(res)



# 5- Write a Python program to check whether all numbers in a list are within the range 1 to 100.
list = [10, 25, 50, 100]  # True
res = all(i>=1 and i<=100 for i in list)
print(res)