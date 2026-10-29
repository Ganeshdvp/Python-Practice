# 1- Write a Python program to count positive numbers, negative numbers, and zeros in a tuple.
t = (10, -5, 0, 8, -2, 0, 4) # positive: 3, negative: 2, zero: 2
positive_count = 0
negative_count = 0
zero_count = 0

for i in t:
    if i == 0:
        zero_count+=1
    elif i>0:
        positive_count+=1
    else:
        negative_count+=1
print('positive_count : ', positive_count)
print('negative_count :', negative_count)
print('zero_count :', zero_count)



# 2- Write a Python program to calculate the average of all elements in a tuple.
t = (10, 20, 30, 40, 50)  # 30.0
sum = 0
for i in t:
    sum+=i
avg = sum/len(t)
print(avg)



# 3- Write a Python program to find the first element that occurs only once in a tuple.
t = (4, 2, 7, 2, 4, 5)  # 7
obj = {}

for i in t:
    if i in obj:
        obj[i] +=1
    else:
        obj[i] = 1
for i in obj:
    if obj[i] == 1:
        print(i)
        break



# 4- Write a Python program to find the smallest odd number in a tuple.
t = (12, 7, 18, 3, 10, 9) # 3
small_odd = float('inf')
for i in t:
    if i%2 != 0:
        if small_odd > i:
            small_odd = i
print(small_odd)