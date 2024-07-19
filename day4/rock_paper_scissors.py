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

#Write your code below this line 👇
import random

choices = {
    1: rock,
    2: paper,
    3: scissors
}

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(1,3)

winner = None
message = ""
# draw
if player == computer:
    message = "Draw"
elif ((player + 1) % 3 == computer % 3): 
    message = "You lose!"
else:
    message = "You won!"


print(choices[player])
print("Computer chose:")
print(choices[computer])
print(message)