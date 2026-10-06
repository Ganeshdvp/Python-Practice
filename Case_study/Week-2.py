# ===== CASE STUDY-2 ====


# 1- find second largest digit in given number
'''
num = 958324
first= 0
second = 0

while num > 0:
    digit = num%10
    if digit > first:
        second = first
        first = digit
    elif digit > second:
        second = digit
    num = num//10

print(second)
'''

# 2- to exact all even digits and print in reverse order
'''
num = 5839246  # 6428
rev = 0
while num > 0:
    digit = num%10
    if digit%2==0:
        rev = rev * 10 + digit
    num = num // 10
print(rev)
'''

# 3- To find the first fibonacci number greater than the given number
'''
num = 50  #55
a = 0
b = 1

while True:
    c = a + b
    if c>num:
        print(c)
        break
    a = b
    b = c
'''

# 4- To convert a decimal number into binary without using built-in conversion functions.
'''
num = 13 #1101
binary = ''

while num > 0:
    reminder = str(num%2)
    binary = reminder + binary
    num = num//2
print(binary)
'''


# 5- To print the below pattern?
# *****
#  * *
#   *
#  * *
# *****
'''
n = 11
i = 1
mid = n//2 + 1

while i<=n:
    if i == 1 or i == n:
        print('*' * n)
    elif mid == i:
        print(' ' * (mid-1) + '*')
    elif mid > i:
        print(' ' * (i-1) + '*' + ' ' * (n - 2*i) + '*')
    else:
        print(' ' * (n - i) + '*' + ' ' * (2*i - 2*mid -1) + '*')
    i = i+1
'''

