# 1- Write a Python program to find the longest word in a sentence.
string = 'Python programming is interesting'   # programming
def longest_sentence(s):
    words = s.split()
    longest_count = 0
    longest_word = ""
    for word in words:
        if longest_count < len(word):
            longest_word = word
            longest_count = len(word)
    return longest_word
print(longest_sentence(string))




# 2- Question: Write a Python program to count the number of words that start with a vowel (a, e, i, o, u) in a sentence. 
string = "Apple is an orange"  # 3
def count_vowel(s):
    words = s.split()
    count = 0
    for word in words:
        if word[0] in 'aeiou':
            count+=1
    return count
print(count_vowel(string))




# 3- Write a Python program to reverse each word in a sentence without changing the order of the words.
string = "hello world python"  # olleh dlrow nohtyp
def reverse_string(s):
    words = s.split()
    rev = ""
    for word in words:
        rev += word[::-1] + " "
    return rev
print(reverse_string(string))




# 4- Write a Python program to count the number of words that contain more than five characters in a sentence.
string = "Python programming is really interesting"  # 3
def count_words(s):
    words = s.split()
    greater_count = 0

    for word in words:
        if len(word) > 5:
            greater_count+=1
    return greater_count
print(count_words(string))