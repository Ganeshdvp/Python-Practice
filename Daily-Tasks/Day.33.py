# 1- Write a recursive function to find the sum of the first N natural numbers.
Input = 5  # 15
def sum_recursion(num):
    if num == 0:
        return 0
    return num + sum_recursion(num-1)
print(sum_recursion(Input))



# 2- Write a recursive function to find the factorial of a given number.
Input = 5  # 120
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)
print(factorial(Input))



# 3- Write a recursive function to reverse a given string.
Input = "python"  # nohtyp
def reverse(s,index):
    if (len(s)-1) == index:
        return s[index]
    return reverse(s,index+1) + s[index]
print(reverse(Input,0))



# 4- Create a closure that stores a bank balance and returns functions to deposit and withdraw money while maintaining the updated balance.
Initial_Balance = 1000
Deposit = 500
Withdraw = 200
'''Output:
Initial Balance: 1000
After Deposit: 1500
After Withdraw: 1300
'''
def bank(i):
    updated_balance = i
    def innerfn(amount,action):
        nonlocal updated_balance
        if action == 'deposit':
            updated_balance += amount
        else:
            updated_balance -= amount
        return updated_balance
    return innerfn
res = bank(Initial_Balance)
print(res(Deposit, 'deposit'))
print(res(Withdraw, 'withdraw'))