# 1- Write a Python program to print the multiplication table of a given number?
num = 5
for i in range(1,10+1):
    print(num*i)



# 2- Write a Python program to print all even numbers from 1 to N using a for loop?
n = 10
for i in range(1,10+1):
    if i%2 == 0:
        print(i)



# 3- Write a Python program to find the factorial of a given number using a for loop?
n = 5
product = 1
for i in range(5,0,-1):
    product*=i
print(product)



# 4- Write a Python program to print all factors of a given number using a for loop?
n = 12
for i in range(1,n+1):
    if n%i == 0:
        print(i)



# 5- Write a Python program to print all prime numbers from 1 to N using for loops?
n = 20
for i in range(2,n+1):
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag:
        print(i)