# 1- Write a Python program to find the smallest positive integer missing from a list.
arr = [3, 4, -1, 1]  # 2
num = 1
while num in arr:
    num+=1
print(num)


# 2- Write a Python program to find all unique pairs whose sum equals the target value.
arr = [1, 5, 7, -1, 5]  #[(1,5), (7,-1)]
target = 6
# approach-1
pairs_set = set()
paris_arr = []
'''for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            pair = tuple((arr[i], arr[j]))
            if pair not in pairs_set :
                paris_arr.append(pair)
                pairs_set.add(pair)'''
# approach-2
seen_set = set()
pairs = set()
for i in arr:
    num = target - i
    if num in seen_set:
        pairs.add(tuple((num,i)))
    seen_set.add(i)
print(list(pairs))



# 3- Write a Python program to create a new list where each element is the product of all other elements, without using division.
arr = [1, 2, 3, 4]
product_arr = []
for i in range(len(arr)):
    product = 1
    for j in range(i+1,len(arr)):
        product*=arr[j]
    for k in range(0,i):
        product*=arr[k]
    product_arr.append(product)
print(product_arr)



# 4- Write a Python program to find the maximum product of any two elements in a list.
arr = [-10, -3, 5, 6, -2]
max_product = float('-inf')
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > 0:
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
print(max_product)


# 5- Write a Python program to find the smallest absolute difference between any two elements.
arr = [8, 3, 15, 10, 2] # 1
smallest_value = float('inf')
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        small = abs(arr[i] - arr[j])
        if small < smallest_value:
            smallest_value = small
print(smallest_value)

