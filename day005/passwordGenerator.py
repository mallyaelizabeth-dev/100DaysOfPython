import random
import string

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like in your password? \n"))
numbers = int(input("How many numbers would you like in your password? \n"))

password = ""

for letter in range(letters):
    password += random.choice(string.ascii_letters) # Random letters from a-zA-Z

filtered_symbol = string.punctuation.replace(" ", "").replace(".", "").replace(":", "") # Codes to remove the white spaces
#  You can even use the replace function to replace some symbols that you don't wish to include in your password
for symbol in range(symbols):
    password += random.choice(filtered_symbol) # remove the white space in the password
for number in range(numbers):
    password += random.choice(string.digits)

password = ''.join(random.sample(password, len(password))) # The function sample() is used to randomize the joined password
# The len(password) is used to speficiy number of items to be returned when random.sample function get executed.
print(f"Here is your password: {password}")
