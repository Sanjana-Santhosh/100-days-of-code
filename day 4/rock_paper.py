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
user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0,2)
print(computer_choice)
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice :
    print("you lose")
elif computer_choice < user_choice :
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
elif computer_choice == user_choice:
    print("draw")
else:
    print("you typed an invalid option")

