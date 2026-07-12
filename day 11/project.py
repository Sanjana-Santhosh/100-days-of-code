# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# your_hand = [random.choice(cards),random.choice(cards)]
# print(your_hand)
# computer_hand = [random.choice(cards),random.choice(cards)]
# print(computer_hand)
#
# # Calculate the scores
# user_score = sum(your_hand)
# computer_score = sum(computer_hand)
#
# # blackjack check
# if  sum(computer_hand) == 21:
#     print("computer gets a blackjack. you lose!")
# elif sum(your_hand) == 21:
#     print("you gets a blackjack. you win!")
# else:
#
#     # Calculate the user's and computer's scores based on their card values.
#
#     if user_score>21:
#         print("you lost")
#     else:
#         user_choice = input("do you want to take another card: y for yes or n for no: ")
#         if user_choice == "y":
#             your_hand.append(random.choice(cards))
#             print(your_hand)
#             user_score = sum(your_hand)
#             if user_score > 21:
#                 print("You lose")
#             else:
#                 user_choice = input("do you want to take another card: y for yes or n for no: ")
#                 if user_choice == "y":
#                     your_hand.append(random.choice(cards))
#                     user_score = sum(your_hand)
#                     if user_score > 21:
#                         print("you lose")
#                 else:
#                     if user_score > computer_score:
#                         print("you win")
#
#         else:
#             print("You lose")
#

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    else:
        user_should_deal = input("Type y to get another card,type n to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True



