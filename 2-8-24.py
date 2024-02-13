import random

userInput = input("Play a game? (Yes/No)")

while userInput == "Yes":

    pc_choice = random.choice(['rock', 'paper', 'scissors'])

    user_choice = input("Enter Rock, Paper, or Scissors:")

    print("PC Choice:", pc_choice)

    if (user_choice == "Rock" and pc_choice == 'rock')\
            or (user_choice == "Paper" and pc_choice == 'paper')\
            or (user_choice == "Scissors" and pc_choice == 'scissors'):
        print("Tie")

    elif (user_choice == "Rock" and pc_choice == 'paper')\
            or (user_choice == "Paper" and pc_choice == 'scissors')\
            or (user_choice == "Scissors" and pc_choice == 'rock'):
        print("Lose")

    else:
        print("Win")

    userInput = input('Continue? (Yes/No)')

year = int(input("Enter the year:"))


if (year % 4) == 0:
    if (year % 100) != 0:
        print( "Leap Year")
elif (year % 4) != 0:
    print("not Leap Year")
elif (year % 400) == 0:
    print("Leap Year")
else:
    print("not Leap Year")

#
#






