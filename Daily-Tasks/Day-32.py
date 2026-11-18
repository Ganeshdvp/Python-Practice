# 1- Create a decorator that counts the vowels in the string returned by a function.
Input = "education"  # 5
def vowel_decorator(fun):
    def innerfn(s):
        count = 0
        for i in s:
            if i in 'aeiou':
                count+=1
        return count
    return innerfn
@vowel_decorator
def display(s):
    return s
print(display(Input))


# 2- Create a decorator that squares the value returned by a function.
Input = 5   # 25
def squares_decorators(fun):
    def innerfn(num):
        return num ** 2
    return innerfn
@squares_decorators
def display(num):
    return num
print(display(Input))



# 3- Create a decorator that reverses the string returned by a function.
Input = "python"  # nohtyp
def reverse_decorator(fun):
    def innerfn(s):
        rev = ""
        for i in s:
            rev = i + rev
        return rev
    return innerfn
@reverse_decorator
def display(s):
    return s
print(display(Input))
