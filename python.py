# python_harsh
#It is a game where a user gives random input of integer and system guess the answer.
import random
lower = int(input("Enter Lower no: "))
Upper = int(input("Enter Upper no: "))
x = random.randint(lower,Upper)
guess_chances = 3
print("\n\tYou've only ", guess_chances, " chances to guess the integer!\n")
count=0
while count<guess_chances:
    count+=1
    guess = int(input("Guess a number: "))
    if x==guess:
        print("Congrat's you did it in", count, "try")
        break
    elif x>guess:
        print("Have one more try")
    elif x<guess:
        print("Have one more try")
if count>guess_chances:
    print("\n\tBetter luck next time")
