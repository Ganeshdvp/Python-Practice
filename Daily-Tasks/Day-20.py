# 1- Write a Python program to count the number of letters and digits in a given string. Store the results in a dictionary.
string = 'python123'  # {"letters": 6, "digits": 3}
new_dic = {}
for i in string:
    if i.isalpha():
        if "letters" not in new_dic:
            new_dic["letters"] = 1
        else:
            new_dic["letters"] +=1
    else:
        if "digits" not in new_dic:
            new_dic["digits"] = 1
        else:
            new_dic["digits"] +=1
print(new_dic)



'''2- Write a Python program to group students based on their marks and store the result in a dictionary.
Use the following grading criteria:
A Grade: Marks greater than or equal to 80
B Grade: Marks from 70 to 79
C Grade: Marks below 70

Expected Output:
{
    "A": ["Rahul", "Priya"],
    "B": ["Anu"],
    "C": ["John"]
}'''
students = {
    "Rahul": 85,
    "Priya": 92,
    "John": 65,
    "Anu": 78
}
new_dic = {}
for i in students:
    if students[i] >= 80:
        if "A" not in new_dic:
            new_dic["A"] = []
        new_dic["A"].append(i)
    elif students[i] <= 79 and students[i] >= 70:
        if "B" not in new_dic:
            new_dic["B"] = []
        new_dic["B"].append(i)
    else:
        if "C" not in new_dic:
            new_dic["C"] = []
        new_dic["C"].append(i)
print(new_dic)