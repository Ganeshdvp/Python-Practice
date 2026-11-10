# 1- Write a program to reverse the order of words in a sentence.
string = "Python is very easy"  # "easy very is Python"
def reverse_words(s):
    rev_str = ""
    words = s.split()
    for i in words:
        rev_str = i + ' ' + rev_str
    return rev_str
print(reverse_words(string))



# 2- Write a program to capitalize the first letter of every word without using the title() method.
string = "welcome to python programming"  # "Welcome To Python Programming"
def cap_first_letter(s):
    new_str = ""
    words = s.split()
    for i in words:
        word = i[0].upper() + i[1:]
        new_str+= word + ' '
    return new_str
print(cap_first_letter(string))




# 3- Write a program to remove consecutive duplicate characters.
string = "aaabbccccdaaa"  # "abcda"
def remove_con_dup(s):
    new_str = ""
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new_str+=s[i]
    else:
        new_str+=s[i+1]
    return new_str
print(remove_con_dup(string))