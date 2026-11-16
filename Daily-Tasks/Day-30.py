# 1- Remove consecutive duplicate characters repeatedly until no duplicates remain.
string = "azxxzy"  # "ay"
def consecutive(s):
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
print(consecutive(string))




# 2- Compress a string based on consecutive character frequency.
string = "aaabbccccdd"  # "a3b2c4d2"
def compress_s(s):
    new_str = ""
    ele = s[0]
    count = 0
    for i in range(0,len(s)):
        if ele == s[i]:
            count+=1
        else:
            new_str = new_str + ele + str(count)
            count = 1
            ele = s[i]
    else:
        new_str = new_str + ele + str(count)

    return new_str
print(compress_s(string))


# 3- Find the second most repeated character.
string = "programming"  # r
def frequncey(s):
    new_dic = {}
    for i in s:
        if i in new_dic:
            new_dic[i] += 1
        else:
            new_dic[i] = 1
    return new_dic
def second_repeated_ch(dict):
    for i in dict:
        if dict[i] >=2:
            return i
print(second_repeated_ch(frequncey(string)))



# 4- Reverse every alternate word in a sentence.
string = "Python is very easy to learn"  # nohtyP is yrev easy ot learn
def reverse_word(word):
    rev = ""
    for i in word:
        rev = i + rev
    return rev
def alternate_word(s):
    new_str = ""
    splitted_s = s.split()
    for i in range(0,len(splitted_s)):
        if i%2 == 0:
            rev = reverse_word(splitted_s[i])
            new_str = new_str + rev + " "
        else:
            new_str = new_str + splitted_s[i] + " "
    return new_str
print(alternate_word(string))




# 5- Find all duplicate characters and their counts.
string = "mississippi"   # i: 4 s: 4 p: 2
def frequency(s):
    new_dict = {}
    for i in s:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
def find_duplicates(dict):
    new_dict = {}
    for i in dict:
        if dict[i] >= 2:
            new_dict[i] = dict[i]
    return new_dict
print(find_duplicates(frequncey(string)))