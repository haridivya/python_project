import random
print('''       **** Hi welcome to Number Guessing Game! ****
  *-*-*-*You Have The  7 Chances to Guess the Number!*-*-*-*
*********************Let's start the game*********************** 
               ''')
user_number_range = int(input("Range to generate a Number:"))
random_value = random.randint(1, user_number_range)
print(random_value)
user_number = 0
no_of_chances = 0
for i in range(0, 7):
    user_number = int(input("Guess the number:"))
    if user_number == random_value:
        no_of_chances += 1
        print("Congratulations the Guessed the Right Number ")
        break
    elif user_number>user_number_range:
        print("Oop's the Given Number it is Not in the Range")
        print("you Lose The game")
        break
    elif user_number >random_value:
        print("Your Guess Number is Too High")
        no_of_chances += 1
    else:
        print("Your Guess Number is Too Low")
        no_of_chances += 1
    if no_of_chances<=7:
        value=7-no_of_chances
        print(f"The Remaining Changes are to guess the Number is: {value}")
    if no_of_chances==7:
        print("You Lose the Game")
