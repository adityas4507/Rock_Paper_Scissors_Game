import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games_list = [rock,paper,scissors]

your_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"Your Choice is : {your_move}")

if your_move >= 0 and your_move<=2:
    print(games_list[your_move])
else:
    print("You typed an invalid number.ERROR.\n")


#This can also be used for printing random moves but it's not suitable for this type of problem
# computer_move = random.choice(games_list)
# print("Computer chose:")
# print(computer_move)
computer_move = random.randint(0,2)
print(f"Computer chose: {computer_move}")
print(games_list[computer_move])

# Or we can use this method but it takes more lines of code
# if your_move >= 3 or your_move < 0:
#     print("You typed an invalid number. You lose!")
# or we can put an elif statement above instead of if statement and it should be above because this statement has to be checked first. that is:
# # elif your_move >= 3 or your_move < 0:
# #   print("You typed an invalid number. You lose!")
# elif your_move == 0 and computer_move == 2:
#     print("You win!")
# elif computer_move == 0 and your_move == 2:
#     print("You lose!")
# elif computer_move > your_move:
#     print("You lose!")
# elif your_move > computer_move:
#     print("You win!")
# elif computer_move == your_move:
#     print("It's a draw!")

if computer_move == your_move:
    print("It's a Draw")
elif (computer_move == 2 and your_move == 0) or (computer_move == 0 and your_move == 1) or (computer_move == 1 and your_move == 2):
    print("You Win!")
elif (computer_move == 1 and your_move == 0) or (computer_move == 2 and your_move == 1) or (computer_move == 0 and your_move == 2):
    print("You Lose!")
else:
    print("You typed an invalid number. You lose!. Try Again")