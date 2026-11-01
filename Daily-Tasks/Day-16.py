# 1- Write a Python program to create a new tuple by inserting the index of every element immediately after it.
t = (10, 20, 30, 40)  # (10, 0, 20, 1, 30, 2, 40, 3)
new_list = []
for i in range(len(t)):
    new_list.append(t[i])
    new_list.append(i)
print(tuple(new_list))



# 2- Write a Python program to create a new tuple by repeating every element according to its position.
t = (10, 20, 30, 40)  # (10, 20, 20, 30, 30, 30, 40, 40, 40, 40)
new_list = []
for i in range(len(t)):
    for j in range(0,i+1):
        new_list.append(t[i])
print(tuple(new_list))



# 3- Write a Python program to create a new tuple by inserting the sum of digits of every element immediately after that element.
t = (12, 35, 101)  # (12, 3, 35, 8, 101, 2)
new_list = []
for i in t:
    sum = 0
    num = i
    while num>0:
        sum += num%10
        num = num//10
    new_list.append(i)
    new_list.append(sum)
print(tuple(new_list))



# 4- Write a Python program to create a new tuple containing only those elements that are greater than the average of the tuple.
t = (10, 25, 15, 30, 20)  # (25, 30)
sum = 0
for i in t:
    sum+=i
avg = sum//len(t)
new_list = []
for i in t:
    if avg < i:
        new_list.append(i)
print(tuple(new_list))




# 5- Write a Python program to create a new tuple by replacing every even-index element with its square and every odd-index element with its cube.
t = (2, 3, 4, 5, 6)  # (4, 27, 16, 125, 36)
new_list = []
for i in range(len(t)):
    if i%2 == 0:
        new_list.append(t[i]**2)
    else:
        new_list.append(t[i]**3)
print(tuple(new_list))