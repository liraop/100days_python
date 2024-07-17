print("The Love Calculator is calculating your score...")
name1 = input().lower() # What is your name?
name2 = input().lower() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

def count_letters(name, word):
  letters_found = 0
  word_letter_list = list(word)
  for letter in word_letter_list:    
    letters_found += list(name).count(letter)
  return letters_found

combined_names = name1+""+name2

true_word_score = 0
true_word_score += count_letters(combined_names, "true")
love_word_score = 0
love_word_score += count_letters(combined_names, "love")
love_score = int(f"{true_word_score}{love_word_score}")

message = None
if (love_score < 10 or love_score >90):
  message = f"Your score is {love_score}, you go together like coke and mentos." 
elif (love_score > 40 and love_score < 50):
  message = f"Your score is {love_score}, you are alright together."
else:
  message = f"Your score is {love_score}."
  
print(message)