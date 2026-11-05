# 1- Write a Python function to return the largest prime factor of a given number.
num = 84  # 7
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    else:
        return True

def isPrimeFact(n):
    for i in range(1,n+1):
        if n%i==0:
            if isPrime(i):
                prime = i
    return prime
res = isPrimeFact(num)
print(res)




# 2- Write a Python function to return a new list containing only the elements whose indices are Fibonacci numbers.
list = [10,20,30,40,50,60,70,80,90]  # [10,20,30,40,60,90]
def isFiboindices(list):
    new_list = []
    a = 0
    b = 1
    new_list.append(list[a])
    while True:
        c = a+b
        if c < len(list):
            new_list.append(list[c])
            a = b
            b = c
        else:
            break
    return new_list

res = isFiboindices(list)
print(res)



# 3- Write a Python function to return a tuple after replacing every prime-indexed element with its square while leaving the remaining elements unchanged.
t = (2,3,4,5,6,7,8)  # (2,3,16,25,6,49,8)
def isPrime(num):
    if num >=2:
        for i in range(2,num//2+1):
            if num%i == 0:
                return False
        return True
def primeSquare(t):
    new_list = []
    for i in range(len(t)):
        if isPrime(i):
            new_list.append(t[i]**2)
        else:
            new_list.append(t[i])
    return tuple(new_list)
res = primeSquare(t)
print(res)



# 4- Write a Python function to return the symmetric difference of two sets without using the ^ operator.
A = {1,2,3,4}
B = {3,4,5,6}  # {1,2,5,6}
def symmentric_diff(d1,d2):
    return d1.symmetric_difference(d2)
print(symmentric_diff(A,B))




# 5- Write a Python function to return a dictionary where each value is the sum of the digits of the corresponding value in the original dictionary.
obj = {'A':123, 'B':45, 'C': 908}  # {'A':6, 'B':9, 'C': 17}
def sumOfDigit(num):
    sum = 0
    while num > 0:
        sum+=num%10
        num = num//10
    return sum

def sumOfValues(obj):
    new_dic = {}
    for i in obj:
        sum = sumOfDigit(obj[i])
        new_dic[i] = sum
    return new_dic;
print(sumOfValues(obj))