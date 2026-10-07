# 1- Write a program to calculate the sum of the first N natural numbers using a while loop?
n = 10
sum = 0
i = 1
while i<=n:
    sum += i
    i+=1
print(sum)



# 2- Write a program to count the number of digits in a given number using a while loop?
num = 123456
count = 0
while num > 0:
    count+=1
    num = num//10
print(count)



# 3- Write a program to find the product of all odd numbers from 1 to N using a while loop?
n = 10
product = 1
i = 1
while i<=n:
    if i%2 != 0:
        product*=i
    i+=1
print(product)



# 4- Write a Python program to count the number of even digits in a number?
num = 24563
count = 0
while num > 0:
    digit = num%10
    if digit%2 == 0:
        count+=1
    num = num // 10
print(count)



# 5- Write a Python program to reverse a given number?
num = 1234
rev = 0
while num > 0:
    digit = num%10
    rev = rev * 10 + digit
    num = num//10
print(rev)



# 6- Write a Python program to check whether a number is Prime or not using a while loop?
n = 17
i = 2
flag = True
while i<=n-1:
    if i%n == 0:
        flag = False
        break
    i+=1
if flag:
    print('it is prime')
else:
    print('it is not prime')



# 7- write a python program to Print numbers divisible by both 2 and 3 using while loop?
n = 20
i=1
while i<=n:
    if i%2 == 0 and i%3 == 0:
        print(i)
    i+=1



# 8- write a Python program to check whether a given number is a perfect square or not?
n = 4
flag = False
i = 1
while i<=4:
    if i**2 == n:
        flag = True
        break;
    i+=1
if flag:
    print('Yes it is perfect square!')
else:
    print('No it is not perfect square!')