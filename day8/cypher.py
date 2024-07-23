from cypher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def all_shift(letter, shift, direction):
    if letter not in alphabet:
        return letter
    
    letter_index = alphabet.index(letter)    
    final_shift = shift
    final_target = 0
    if shift >= len(alphabet):
        final_shift = shift%26
    
    if direction == "decode":
        final_shift *= -1
        
    final_target = letter_index+final_shift
    shifted_letter = alphabet[final_target]
    return shifted_letter

def caesar(text,shift,direction):
    final_text = "" 
    for letter in text:
        final_text += all_shift(letter, shift, direction)
    print(f"The {direction} text is {final_text}")

keep_running = True
while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift_number, direction=direction)
    
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no' ") 
    keep_running = True if (user_input == "yes") else False
    