stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

stages.reverse()

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 1

display = []
for letter in chosen_word:
    display.append("_")

game_ends = False

while not game_ends:
    guess = input("Guess a letter: ").lower()
    match = False
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
            match = True    
    print(" ".join(display))

    if not match:
        lives += 1
    
    print(stages[lives-1])

    if "_" not in display: 
        print("You won")
        game_ends = True
    
    if lives > 6:
        game_ends = True
        print(stages[lives-1])
        print("You lose")