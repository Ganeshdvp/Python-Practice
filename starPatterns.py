# ===== Star Patterns in Python ====


# *
# **
# ***
# ****
# *****
'''
rows = int(input('Enter a number: '));
i = 1;
while i<=rows:
    print('*' * i);
    i += 1
'''


#     *
#    **
#   ***
#  ****
# *****
'''
rows = int(input('Enter a number: '));
i = 1;
while i <= rows:
    print(' ' * (rows-i) + '*' * i)
    i += 1
'''


#     *
#    ***
#   *****
#  *******
# *********
'''
rows = int(input('Enter a number: '));
i = 1;
while i<=rows:
    print(' ' * (rows-i) + '*' * (2*i-1))
    i+=1;
'''



# *******
#  *****
#   ***
#    *
'''
rows = int(input('Enter a number: '));
i = rows;
while i >= 1:
    print(' ' * (rows - i) + '*' * (2*i-1))
    i -= 1;
'''



#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
'''
rows = int(input('Enter a number: '));
i=1;
mid = rows//2 + 1
while i<=rows:
    if mid >= i:
        print(' ' * (mid-i), '*' * (2*i-1))
    else:
        print(' ' * (i-mid), '*' * (2*rows - 2*i + 1))
    i += 1
'''



# *
# **
# * *
# *  *
# *   *
# *    *
# *     *
# *      *
# *********
'''
rows = int(input('Enter a number: '));
i = 1;
while i<=rows:
    if i == 1 or i == rows:
        print('*' * i, sep='')
    if i >= 2 and i<rows:
        print('*', ' ' * (i-2), '*', sep='')
    i += 1;
'''



# *********
#  *      *
#   *     *
#    *    *
#     *   *
#      *  *
#       * *
#         *
'''
rows = 7
i=1
while i<=rows:
    if i == 1:
        print('*' * rows)
    elif i == rows:
        print(' ' * (i-1) + '*')
    else:
        print(' ' * (i-1) + '*' + ' ' * (rows-i-1) +'*')
    i+=1
'''



#     *
#    * *
#   *   *
#    * *
#     *
'''
rows = 9
i=1
mid = rows//2 + 1
while i<=rows:
    if i==1 or i==rows:
        print(' ' * (mid-1) + '*')
    elif mid>i:
        print(' ' * (mid-i) + '*' + ' ' * (2*i-3) + '*')
    else:
        print(' ' * (i-mid) + '*' + ' ' * (2*rows-2*i-1) + '*')
    i+=1
'''



# *      *
#  *    *
#    * *
#     *
#    * *
#   *   *
# *      *
'''
rows = 7
i=1
mid= rows//2 + 1
while i<=rows:
    if i==1 or i==rows:
        print('*' + ' ' * (rows-2) + '*')
    elif mid == i:
        print(' ' * (mid-1) + '*')
    elif mid>i:
        print(' ' * (i-1) + '*' + ' ' * (2*mid - 2*i - 1) + '*')
    else:
        print(' ' * (rows-i) + '*' + ' ' * (2*i - 2*mid - 1) + '*')
    i+=1
'''


# 1
# 22
# 333
# 4444
# 55555
'''
rows = 5
i = 1
while i<=rows:
    d = 1
    while d<=i:
        print(i, end='')
        d = d+1
    i = i+1
    print()
'''



#     1
#    123
#   12345
#  1234567
# 123456789
'''
rows = 5
i = 1
while i<=rows:
    print(' ' * (rows-i), end='')
    d = 1
    while d<=i*2-1:
        print(d, end='')
        d = d+1
    i = i+1
    print()
'''



# 54321
# 4321
# 321
# 21
# 1
'''
rows = 5
i = rows
while i>=1:
    d = i
    while d>=1:
        print(d, end='')
        d=d-1
    i = i-1
    print()
'''



# ABCDE
# ABCDE
# ABCDE
# ABCDE
# ABCDE
'''
n = 5
i = 1
while i<=n:
    d = 1
    while d<=n:
        print(chr(64 + d),end='')
        d = d+1
    i = i+1
    print()
'''



# ABCDE
# ABCDE
# ABC
# AB
# A
'''
rows = 5
i=1
while i<=rows:
    d=1
    while d<=(rows-i+1):
        print(chr(64+d),end='')
        d=d+1
    i=i+1
    print()
'''



# A   A 
#  B B
#   C
#  D D
# E   E
'''
n=5
i=1
mid = n//2 + 1
while i<=n:
    if i==1 or i==n:
        print(chr(64+i), ' ' * (n-2),chr(64+i), sep='')
    elif mid == i:
        print(' ' * (i-1), chr(64+i),sep='')
    elif mid>i:
        print(' ' * (i-1), chr(64+i), ' ' * (i-1), chr(64+i), sep='')
    else:
        print(' ' * (2*i - 2*mid - 1), chr(64+i), ' ' * (2*i - 2*mid-1), chr(64+i),sep='')
    i=i+1
'''