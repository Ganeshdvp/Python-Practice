# 1- Write a Python program using a while loop to find the Nth Fibonacci number?
n = 7
count = 0
a = 0
b = 1
i = 1
while True:
    c = a+b
    count+=1
    if count == n:
        print(b)
        break
    a = b
    b = c



# 2- Write a Python program using a while loop to find the sum of the first N Fibonacci numbers?
num = 6
count = 2
a = 0
b = 1
sum = a+b
while True:
    c = a+b
    count+=1
    sum+=c
    if count == num:
        break
    a = b
    b = c
print(sum)



# 3- Write a Python program using while loops to find the sum of all prime numbers between 1 and N?
n = 10
sum = 0
i = 2
while i<=n:
    d = 2
    flag = True
    while d<i:
        if i%d == 0:
            flag = False
            break
        d+=1
    if flag:
        sum+=i
    i+=1
print(sum)



# 4- .Write a Python program using a while loop to find the difference between the largest and smallest digit of a number?
num = 58321
largest = float('-inf')
smallest = float('inf')
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    num = num // 10
print(largest - smallest)



# 5- Write a Python program using a while loop to read N numbers and count how many are positive and how many are negative?
positive_count = 0
negative_count = 0
while True:
    n = int(input('Enter a number : '))
    if n == 0:
        break
    elif n>0:
        positive_count+=1
    else:
        negative_count+=1
print(positive_count)
print(negative_count)