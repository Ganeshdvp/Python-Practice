# 1- Write a Python program to print the product of the digits of each element in a list?
list = [123, 405, 67, 89]
product_list = []
for i in list:
    product = 1
    num = i
    while num>0:
        digit = num%10
        product *= digit
        num = num//10
    product_list.append(product)
print(product_list)



# 2- Write a Python program to find the reverse of each element in a list?
list = [123, 405, 89]
rev_list = []
for i in list:
    rev = 0
    num = i
    while num>0:
        digit = num%10
        rev = rev * 10 + digit
        num = num//10
    rev_list.append(rev)
print(rev_list)



# 3- Write a Python program to replace all even numbers in a list with their square?
list = [2, 5, 6, 9, 8]
for i in range(0,len(list)):
    if list[i]%2 == 0:
        list[i] = list[i] ** 2
print(list)



# 4- write a python program to print the below pattern?
# E
# ED
# EDC
# EDCB
# EDCBA

n = 5
i = 1
while i<=n:
    d = 0
    while d<i:
        print(n-d, end='')
        d+=1
    print()
    i+=1



# 5- Write a Python program to count the digits of each element in a list?
list = [123, 4, 56789]
count_list = []
for i in list:
    num = i
    count = 0
    while num > 0:
        count+=1
        num = num//10
    count_list.append(count)
print(count_list)