alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text =  input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount)%26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    return cipher_text
    # print(f"The encoded text is {cipher_text}")
    
# encrypt(plain_text=text, shift_amount=shift)    
print("################---END---####################")

def decrypt(encoded_text, shift_amount):
    plain_text = ""
    for letter in encoded_text:
        if letter in alphabet: # Test if the provided letters are all in the alphabet
            position = alphabet.index(letter)
            new_position = (position - shift_amount)%26
            old_letter = alphabet[new_position]
            plain_text += old_letter
        else:
            plain_text += letter # For the characters that are not in the alphabet then replace with themselves
    return plain_text
    # print(f"The decoded text is: {plain_text}")

# decrypt(encoded_text=text, shift_amount=shift)
if direction == "encode":
    encoded_text = encrypt(plain_text=text, shift_amount=shift)
    print(f"The coded text is: {encoded_text}")
elif direction == "decode":
    decoded_text = decrypt(encoded_text=text, shift_amount=shift)
    print(f"The decoded text is: {decoded_text}")
else:
    print("The direction unknown!")