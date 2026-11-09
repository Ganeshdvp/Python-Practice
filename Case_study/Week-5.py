# 1- Write a Python program to group words in a list based on their length. The length of each word should be the dictionary key, and the words with the same length should be stored in a list as the value.
Input = ['cat', 'dog', 'apple', 'bat', 'mango']  # {3: ['cat', 'dog', 'bat'], 5: ['apple', 'mango']}
def group_words(list):
    new_dic = {}
    for word in list:
        if len(word) in new_dic:
            new_dic[len(word)].append(word)
        else:
            new_dic[len(word)] = [word]
    return new_dic
print(group_words(Input))




# 2- Write a Python program to group words in a list based on their first character. The first character of each word should be the dictionary key, and the words starting with the same character should be stored in a list as the value.
Input = ['apple', 'ant', 'ball', 'bat', 'cat']  # {'a': ['apple', 'ant'], 'b': ['ball', 'bat'], 'c': ['cat']}
def group_first_ch(list):
    new_dic = {}
    for word in list:
        if word[0] in new_dic:
            new_dic[word[0]].append(word)
        else:
            new_dic[word[0]] = [word]
    return new_dic
print(group_first_ch(Input))
