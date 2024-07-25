############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

#################################################################

import random
import art

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def initialize_hand():
   return [deal_card(), deal_card()]

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
      return 0
   
    if 21 in hand and sum(hand) > 21:
      hand.remove(21)
      hand.append(1)
    
    return sum(hand)

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

def game():
    print(art.logo)
    player_hand = initialize_hand()
    computer_hand = initialize_hand()
    keep_running = True

    while keep_running:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"   Your cards: {player_hand}, current score: {player_score}")
        print(f"   Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            keep_running = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_hand.append(deal_card())
            else:
                keep_running = True

        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

        print(f"   Your final hand: {player_hand}, final score: {player_score}")
        print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
        print(compare(player_score, computer_score))
            
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        game()
    else: 
        exit()

game()