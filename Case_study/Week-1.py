# ===== CASE STUDY-1 ====

# 1- To check whether a person is eligible for a loan based on the following conditions:
#           a- Age must be between 21 and 60.
#           b- Salary must be atleast 30,000.
#           c- Credit score must be 700 or above.
#           d- The person should not have an existing loan.
# if all conditions are satisfied, display "loan eligible".otherwise,display "loan not eligible".
age = int(input("Enter your age : " ));
salary = int(input("Enter your Salary : " ));
creditScore = int(input("Enter your credit score : " ));
existingLoan = input("Do you have any existing loan? (Yes/no) : " ); # yes or no

if age >= 21 and age <= 60 and salary >= 30000 and creditScore >= 700 and existingLoan == 'no':
    print("Loan Eligible");
else:
    print("Loan Not Eligible");


# 2- Rock, paper and scissors game.
while True :
    player_1 = input("Player_1 Please enter your choice :");
    player_2 = input("Player_2 Please enter your choice :");
    if player_1 == 'rock' and player_2 == 'paper' :
        print('player_2 is winner')
        break;
    elif player_1 == 'paper' and player_2 == 'scissor' :
        print('player_2 is winner')
        break;
    elif player_1 == 'scissor' and player_2 == 'rock' :
        print('player_2 is winner')
        break;
    elif player_1 == 'paper' and player_2 == 'rock' :
        print('player_1 is winner')
        break;
    elif player_1 == 'scissor' and player_2 == 'paper' :
        print('player_1 is winner')
        break;
    elif player_1 == 'rock' and player_2 == 'scissor' :
        print('player_1 is winner')
        break;
    elif player_1 == player_2 :
        print('Its a Draw dudes')
        break;
    else :
        print("Enter Valid Choice Dude!")


# 3- Find the sum of all its digits.
num = 1234
sum = 0
while num > 0:
    sum += num%10
    num = num//10
print(sum)


# 4- Keep accepting numbers until 0 is entered. Find the largest number.
largest = 0;
while True:
    num = int(input("Enter your number : "))

    if num == 0:
        break;

    if num > largest :
        largest = num
print(largest)