#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")


#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.
while "_" in display:
    guess = input("Guess a letter: ").lower()

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess

    print(display)

print("You won!")