from art import logo
import random

print(logo)

HARD_TURNS = 10
EASY_TURNS = 5

def get_difficulty_turns(choice):
    if (choice == "easy"):
        return EASY_TURNS
    else:
        return HARD_TURNS

def get_number():
    return random.randint(0,100)

def game():
    difficulty = input("Easy or hard? ")
    turns = get_difficulty_turns(difficulty)
    number = get_number()

    while (turns > 0):
        guess = int(input("Guess a number:"))
        if (guess == number):
            print("Guessed right! You won.")
        else:
            if (guess > number):
                print("Too high!")
            else:
                print("Too low!")
            turns -= 1
            print(f"{turns} turns left")
    print("You loose!")
        

game()

