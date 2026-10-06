# 1- Count Even Digits and Odd Digits
num = 583291  # even digits:2 and odd digits:4
even_digits = 0
odd_digits = 0
while num > 0:
    digit = num%10
    if digit%2 == 0:
        even_digits+=1
    else:
        odd_digits+=1
    num = num//10
print(even_digits)
print(odd_digits)


# 2- Check whether the reverse of a number is greater than the original.
num = 123
temp = num
rev = 0
while num > 0:
    digit = num%10
    rev = rev * 10 + digit
    num = num//10
if rev > temp:
    print('Yes it is greater than original number')
else:
    print('No it is not greater than original number')


# 3- Check First Digit == Last Digit?
num = 12321
last_digit = num%10
first_digit = 0
while num>10:
    first_digit = num//10
    num = num//10
if last_digit == first_digit:
    print('Yes it is!')
else:
    print('No it is not!')


# 4- Find LCM Using while loop?
a = 12
b = 18
smaller_num = 0
if a > b:
    smaller_num = b
else:
    smaller_num = a

gcd = 0
i = 1
while i<=smaller_num:
    if a%i == 0 and b%i == 0:
        gcd = i
    i+=1
lcm = a*b//gcd
print(lcm)


# 5- Find Largest Even Digit?
num = 583246
Largest = 0
while num>0:
    digit = num % 10
    if digit%2==0 and Largest < digit:
        Largest = digit
    num = num//10
print(Largest)


# 6- Remove every second digit and print them all?
num = 12345678  #1357
units = 1
count=0
res = 0
while num > 0:
    count += 1
    if count == 2:
        res = num%10 * units + res
        units *= 10
        count = 0
    num = num // 10
print(res)



# 7- Remove the largest digit?
num = 583291  #53291
temp = num
res = 0
units = 1
largest = 0
while num>0:
    digit = num%10
    if digit > largest:
        largest = digit
    num=num//10
while temp>0:
    digit = temp%10
    if digit != largest:
        res = digit * units + res
        units *= 10
    temp = temp//10
print(res)