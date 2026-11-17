# 1- Create a closure that stores a tax percentage and returns an inner function. The inner function should accept the price and return the final price after adding the tax.
tax = 18    # 1180
price = 1000
def taxPercentage(t):
    def innerfn(p):
        final_price = (p*t//100) + p
        return final_price
    return innerfn
res = taxPercentage(tax)
print(res(1000))




# 2- Create a closure that maintains a running total. Every time a number is passed to the returned function, add it to the previous total and return the updated total.
input = 10,20,5    # 10 30 35
def running_total():
    total_running = 0
    def innerfn(num):
        nonlocal total_running
        total_running = total_running + num
        return total_running
    return innerfn
res = running_total()
print(res(10))
print(res(20))
print(res(5))




# 3- Create a generator that accepts a list of words and yields only the words whose length is greater than N.
Words = ["cat", "python", "java", "programming"]   # python java programming
N = 4
def greater_N(words,N):
    for i in words:
        if len(i) >= N:
            yield i
for i in greater_N(Words,N):
    print(i)



# 4- Create a generator that accepts a list of strings and a character. Yield only the strings that start with that character.
Words = ["apple", "banana", "avocado", "grape", "apricot"]  # apple avocado apricot
Character = "a"
def generatorfn(words,ch):
    for i in words:
        if i[0] == ch:
            yield i
for i in generatorfn(Words,Character):
    print(i)



# 5- Using filter() and a lambda function, write a program to extract all numbers divisible by 3. 
Input = [10, 12, 15, 17, 21, 25, 30] # [12, 15, 21, 30]
res = list(filter(lambda i: i%3 == 0, Input))
print(res)


# 6- Using a lambda function with map(), write a program to find the square of every number in the given list.
Input = [2, 4, 6, 8]  # [4, 16, 36, 64]
res = list(map(lambda i: i**2 , Input))
print(res)



# 7- Using reduce() and lambda, calculate the product of all numbers without using math prod().
from functools import reduce
Input = [2, 3, 4, 5]  # 120
res = reduce(lambda i,j: i*j , Input)
print(res)