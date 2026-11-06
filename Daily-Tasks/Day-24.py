# 1- Write a Python program to check whether a given string is a palindrome without using slicing.
string = "madam"  # Palindrome
def isPalindrome(s):
    rev = ""
    for i in s:
        rev = i + rev
    if rev == s:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(isPalindrome(string))



# 2- Write a Python program to count how many times a given character occurs in a string without using the count() method.
# Input: Enter a string: programming
#        Enter a character: g
# Output: Character occurs 2 times
'''def count_characters(s,ch):
    count = 0
    for i in s:
        if i == ch:
            count+=1
    return count
def count_res():
    string = input('Enter a string : ')
    ch = input('Enter a character : ')
    return count_characters(string,ch)
print('Character occurs ', count_res(), 'times')'''




# 3- Write a Python program to remove duplicate characters from a string while maintaining their original order.
string = "programming"  # progamin
def removeDuplicates(s):
    unique_str = ""
    seen = set()
    for i in s:
        if i not in seen:
            unique_str+=i
            seen.add(i)
    return unique_str
print(removeDuplicates(string))

    


# 4- Write a Python program to find the first character that appears only once in a given string.
string = "swiss"  # First non-repeating character: w
def frequency_count(s):
    new_dic = {}
    for i in s:
        if i in new_dic:
            new_dic[i] += 1
        else:
            new_dic[i] = 1
    return new_dic
def ch_appear_once(s):
    frequency_ch = frequency_count(s)
    for i in frequency_ch:
        if frequency_ch[i] == 1:
            return i
print(ch_appear_once(string))

    