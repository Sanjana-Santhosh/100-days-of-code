import random
answer = random.randint(1,100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess,actual_answer):
    if user_guess > actual_answer:
        print("Too high")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print(f"You got it. The correct answer is {actual_answer}")


def set_difficulty():
    level = int(input("Choose a difficulty 'easy' or 'hard': "))
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to Number Guessing Project")
print("I'm thinking of a number between 1 and 100")

turns = set_difficulty()
print(f"You have {turns} turns left")
guess = int(input("Guess a number between 1 and 100: "))