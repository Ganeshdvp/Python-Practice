# 1- A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. write a program to display only the available seat numbers?
seats = 20 # 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19
for i in range(1,seats+1):
    if i%5 != 0:
        print(i)


# 2- A company issues employee IDs from 1001 to 1020. write a program to count how many employee IDs are even?
count = 0
for i in range(1001,1020+1):
    if i%2==0:
        count+=1
print(count)


# 3- A game contains 15 levels. Bonus rewards are given for levels divisible by 3. write a program to display all bonus levels?
levels = 15
for i in range(1,15+1):
    if i%3==0:
        print(i)


# 4- A library contains books numbered from 1 to 50. write a program to count how many book numbers are multiples of 7?
count=0
for i in range(1,50+1):
    if i%7==0:
        count+=1
print(count)


# 5- Write a program to find the first number greater than 100 that is divisible by both 7 and 9 using while loop?
i=100
while i>=100:
    if i%7 == 0 and i%9 == 0:
        print(i)
        break
    i+=1


# 6- Write a program to print all numbers from 1 to n whose square is less than 50?
n = 20
for i in range(1,n+1):
    if i*i < 50:
        print(i)
