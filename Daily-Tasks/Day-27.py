# 1- Write a Python program to replace every vowel (a, e, i, o, u) in a given string with *. Keep all other characters unchanged.
string =  "education"  # output:- *d*c*t**n
def replace_ch(s):
    new_str = ""
    for ch in s:
        if ch in 'aeiou':
            new_str += '*'
        else:
            new_str+=ch
    return new_str
print(replace_ch(string))




# 2- Write a Python program to expand a compressed string in which each character is followed by a number representing how many times that character should be repeated.
string = "a3b2c4d"  # aaabbccccd
def repeat_ch(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isdigit():
            new_str += s[i-1] * (int(s[i])-1)
        else:
            new_str+=s[i]
    return new_str
print(repeat_ch(string))




# 3- Write a Python program to replace all spaces in a given string with hyphens (-) without changing any other characters.
string = "I love Python programming"  # I-love-Python-programming
def replace_spaces(s):
    new_str = ""
    for ch in s:
        if ch == " ":
            new_str+= '-'
        else:
            new_str+=ch
    return new_str
print(replace_spaces(string))