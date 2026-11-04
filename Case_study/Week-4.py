# 1- Write a Python program to group words according to their lengths using a dictionary.
words = ['cat', 'apple', 'dog', 'ball', 'banana']   # {3: ['cat', 'dog'], 5: ['apple'], 4: ['ball'], 6: ['banana']}
new_dic = {}
for i in words:
    if len(i) in new_dic:
        new_dic[len(i)].append(i)
    else:
        new_dic[len(i)] = [i]
print(new_dic)



# 2-  Write a Python program to find all common keys between two dictionaries.
d1 = {'A': 10, 'B': 20, 'C': 30}
d2 = {'B': 40, 'C': 50, 'D': 60}   # Common keys: ['B', 'C']
new_list = []
for i in d1:
    if i in d2:
        new_list.append(i)
print(new_list)



# 3- Write a Python program to count the frequency of each element in a list using a dictionary and display the element with the highest frequency.
numbers = [1, 2, 3, 2, 4, 2, 1, 3]  # output: Most frequent element: 2 Frequency: 3
new_dic = {}
for i in numbers:
    if i not in new_dic:
        new_dic[i] = 1
    else:
        new_dic[i]+=1
freq_ele = 0
freq_val = 0
for i in new_dic:
    if new_dic[i] > freq_val:
        freq_ele = i
        freq_val = new_dic[i]
print('Most frequent element: ' , freq_ele)
print('Frequency: ' , freq_val)



# 4- Write a Python program to calculate the average product price and display the products whose prices are greater than the average.
products = {'Pen': 10, 'Book': 100, 'Bag': 500, 'Scale': 30}
# Output: Average price: 160.0
# Products above average: {'Bag': 500}
sum = 0
for i in products:
    sum += products[i]
avg = sum//len(products)
new_dic = {}
for i in products:
    if products[i] > avg:
        new_dic[i] = products[i]
print(new_dic)




# 5- Write a Python program to count the frequency of each character in a string, ignoring spaces and treating uppercase and lowercase letters as the same.
text = "Python Python"  # output:{'p': 2, 'y': 2, 't': 2, 'h': 2, 'o': 2, 'n': 2}
new_dic = {}
for i in text.replace(" ","",1):
    if i in new_dic:
        new_dic[i] +=1
    else:
        new_dic[i] = 1
print(new_dic)