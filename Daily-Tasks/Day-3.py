# 1-  Write a python programme to Print Numbers from 10 to 1 using while loop?
i = 10
while i>=1:
    print(i)
    i-=1


# 2-Write a python programme to Print the first 10 multiples of 5?
i = 1
while i<=10:
    print(5 * i)
    i+=1


# 3- Write a python programme to Find Sum from 1 to 10?
sum = 0
i = 1
while i<=10:
    sum += i
    i+=1
print(sum)



# 4- Write a python programme to Count Numbers from 1 to 100 Divisible by 5?
count = 0
i=1
while i<=100:
    if i%5 == 0:
        count+=1
    i+=1
print(count)



# 5- Write a python programme to Print Numbers Up to User's Number?
num = 7
i = 1
while i<=num:
    print(i)
    i+=1



# 6- Write a python programme to Print Multiplication Table?
num = 7
i = 1
while i<=10:
    print(num * i)
    i+=1



# 7-Write a python programme to Count Down from User's Number?
num = 5
while num>=1:
    print(num)
    num -=1


# 8- Write a python programme to Print 5 to 15?
for i in range(1,15+1):
    print(i)