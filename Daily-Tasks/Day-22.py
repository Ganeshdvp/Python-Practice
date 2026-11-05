# 1- Write a function to check whether a number is prime.
num = 17  # True
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print(isPrime(num))



# 2- Write a function to find the sum of digits of a number.
num = 1234  # 10
def sumOfDigits(n):
    sum = 0
    while n>0:
        sum+=n%10
        n = n//10
    return sum
print(sumOfDigits(num))



# 3- Write a function to check whether a number is a palindrome
num = 121  # True 123
def isPalindrome(n):
    num = n
    rev = 0 
    while n > 0:
        digit = n%10
        rev = rev * 10 + digit
        n = n//10
    if num == rev:
        return True
    else:
        return False
print(isPalindrome(num))



# 4- Write a function to find the second-largest distinct element without sorting.
list = [10, 20, 5, 20, 15]  # 15
def isSecondLargest(arr):
    largest = float('-inf')
    smallest = float('-inf')
    for i in arr:
        if largest < i:
            smallest = largest
            largest = i
        else:
            if largest > i and smallest < i:
                smallest = i
    return smallest
print(isSecondLargest(list))




# 5- Write a function to find duplicate elements without using count().
list = [1, 2, 3, 2, 4, 1]  # [1, 2]
def isDuplicate(arr):
    new_list = []
    seen = set()
    for i in arr:
        if i in seen:
            new_list.append(i)
        else:
            seen.add(i)
    return new_list
print(isDuplicate(list))