# 1- Write a Python program to count the number of vowels and consonants in a given string. Ignore spaces, digits, and special characters. 
string = "python$$" # Vowels = 1 Consonants = 5
def isCharacter(ch):
    if (ch >= 'a' and ch <= 'z') or (ch>='A' and ch<='Z'):
        return True
    else:
        return False
    
def countOfVC(s):
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            vowel_count+=1
        else:
            if isCharacter(i):
                consonant_count+=1
    return vowel_count,consonant_count
print(countOfVC(string))




# 2- Write a Python program to count the number of uppercase and lowercase letters in a given string.
string = "PyTh$$On" # Uppercase = 3 Lowercase = 3
def countUL(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if isCharacter(i):
            if i == i.upper():
                upper_count+=1
            else:
                lower_count+=1
    return upper_count,lower_count
print(countUL(string))




# 3- Write a Python program to count the total number of digits present in a given string.
string = "abc123de45"  # 5
def isDigit(s):
    count = 0
    seen = {'0','1','2','3','4','5','6','7','8','9'}
    for i in s:
        if i in seen:
            count+=1
    return count
print(isDigit(string))



# 4- Write a Python program to remove all spaces from a given string without changing the order of the characters.
string = "P y t h o n"  # Python
def removeSpaces(s):
    new_string = ""
    for i in s:
        if i != ' ':
            new_string += i
    return new_string
print(removeSpaces(string))




# 5- Write a Python program to count the total number of spaces present in a given string.
string = "Python is easy"  # 2
def count_spaces(s):
    count = 0
    for i in s:
        if i == ' ':
            count+=1
    return count
print(count_spaces(string))