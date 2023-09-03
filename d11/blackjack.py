
import random
# from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

  play_game()



















# from art import logo
# import random

# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)
# user_cards=[]
# computer_cards=[]
# for _ in range(2) :
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# def calculate_score():
#     sum(cards)
#     if 11 in cards and sum>21:
#         sum=sum-10
#         return sum
        
#     if user_cards and computer_cards==0 or computer_cards==0 or user cards>21:
#         return "game over"
#     return sum


# ans=input("Do you want to play blackjack? (y/n): \n")
# if ans== "y":
#     print(logo)
#     deal_card()
    
    
#     calculate_score()
   

#     # if computer_cards==0 or user_cards==0 or user_cards>21:
#     #     print("thanks for the play!")
    
#     answer=input("Want to draw another card? (y/n):\n")
#     if answer=="y":
#         play=True
#         while play :
        
#             deal_card()
#             calculate_score()





# else:
#     print("No problem! have a good day.")
























# import random
# from art import logo 

# def deal_card():
#     if 11 in cards and 10 in cards and len(cards) ==2:
#         return 0 
#     if 11 in cards and sum(cards)>21:
#         # sum = sum - 10
#         cards.remove(11)
#         cards.append(1)
#     else:
#        sol= input("Want to draw another card? (y/n): \n")
#        if sol =="yes":
           
#         cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     card=random.choice(cards)
#     return card

# def calculate_score(cards):
#     return sum(cards)

# user_cards=[]
# computer_cards=[]
# game_over=False

# for _ in range(2):
#     new_card=deal_card()
#     user_cards.append(new_card)
#     new_card=deal_card()
#     computer_cards.append(new_card)
# user_score=calculate_score(user_cards)

# computer_score=calculate_score(computer_cards)
# print(f"your card: {user_cards}, current score={user_Score}")
# print(f"computers first card: {computer_cards[0]}")
# if user_score>21 or computer_score==0 or user_score==0:
#     game_over=True


# # ans=input("Do you want to play BlackJack? (y/n): \n")
# # while ans=="y":
  