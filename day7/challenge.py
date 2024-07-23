import random
from hangman_art import stages,logo
from hangman_words import word_list

stages.reverse()
chosen_word = random.choice(word_list)
lives = 1

print(logo)

display = []
for letter in chosen_word:
    display.append("_")

already_guessed = []

game_ends = False

while not game_ends:
    guess = input("Guess a letter: ").lower()
    if guess not in already_guessed:
        if guess not in display:
            match = False
            for letter in range(len(chosen_word)):
                if guess == chosen_word[letter]:
                    display[letter] = guess
                    match = True                

            print(" ".join(display))

            if not match:
                print(f"{guess} is not on the word.")
                lives += 1
            already_guessed.append(guess)

            print(stages[lives-1])

            if "_" not in display: 
                print("You won")
                game_ends = True

            if lives > 6:
                game_ends = True
                print(stages[lives-1])
                print("You lose")
    else: 
        print("Already guessed this one, try another again!")