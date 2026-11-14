# 1- Write a python program to find the longest palindromic substring.
string = "babad"  # bab
new_str = ""
def reverse_string(word):
    rev = ""
    for i in word:
        rev = i+rev
    return rev
def lp_substring(s):
    for i in range(1,len(string)):
        slicing = s[0:i+1]
        rev = reverse_string(slicing)
        if rev == slicing:
            return slicing
print(lp_substring(string))



# 2- Write a python function to remove all special characters from a string.
string = "a@1#b"  # a1b
def check_ch(ch):
    if (ch >= 'a' and ch <= 'z') or (ch>='A' and ch<='Z'):
        return True
    elif ch >= '0' and ch<='9':
        return True
    else:
        return False
def remove_special_ch(s):
    new_str = ""
    for i in s:
        if check_ch(i):
            new_str+=i
    return new_str
print(remove_special_ch(string))



# 3- Write a python function to reverse eevry alternate word in a sentence.
string = "one two three four"   # one owt three ruof
def reverse_ch(word):
    rev = ""
    for i in word:
        rev = i+rev
    return rev
def reverse_word(s):
    new_str = ""
    words = s.split()
    for i in range(1,len(words),2):
        new_str = new_str + words[i-1] + " "
        rev = reverse_ch(words[i])
        new_str += rev + " "
    return new_str
print(reverse_word(string))
