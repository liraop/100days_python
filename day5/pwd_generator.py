#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def get_random_character_string(characters_number, characters_list):
    random_string = "" 
    counter = characters_number
    while counter > 0:
        random_string += random.choice(characters_list)
        counter -= 1
    return random_string

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def get_easy_pwd():
    pwd = ""
    pwd += get_random_character_string(nr_letters, letters)
    pwd += get_random_character_string(nr_symbols, symbols)
    pwd += get_random_character_string(nr_numbers, numbers)
    return pwd

print(f"easy pwd: {get_easy_pwd()}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def get_hard_pwd():
    selected_characters = list(get_easy_pwd())
    random.shuffle(selected_characters)
    return ''.join(selected_characters)
        
print(f"hard pwd: {get_hard_pwd()}")