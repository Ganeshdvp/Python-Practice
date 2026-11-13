# An online shopping website provides discounts based on the purchase amount.
# 1- Write a function calculate discount(amount) that gives a 10% discount when the amount is ₹5,000 or more; otherwise, no discount is given.
def discount(amount):
    if amount>= 5000:
        return amount - amount * 10 // 100
    return 0
print(discount(5000))



# 2- A website needs to check whether a user's password meets its security rules.
# Question: Write a function validate_password(password) that checks whether the password contains at least 8 characters, one digit, and one special character.
string = "Enteeer2r*"
def validate_password(password):
    if len(password) < 8:
        return "less than 8 characters!"
    count_digit = 0
    special_cnt = 0
    for ch in password:
        if ch.isdigit():
            count_digit+=1
        if not ch.isalpha() and not ch.isdigit():
            special_cnt+=1
    if count_digit == 0:
        return "need atleast one digit!"
    if special_cnt != 1:
        return "need only one special character!"
    return "Successfully validated!"
print(validate_password(string))




# 3- Scenario: An online shopping company calculates delivery charges based on the order amount.
# Question: Create a function delivery_charge(amount) that returns free delivery for orders of ₹1,000 or more and ₹50 for smaller orders. Sample input: Order amount:
def delivery_charge(amount):
    if amount >= 1000:
        return amount
    else:
        if amount < 1000:
            return amount + 50
print(delivery_charge(900))