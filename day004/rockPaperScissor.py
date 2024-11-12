import random

# Print a welcoming Note!!!
welcome_note = '''
┓ ┏  ┓      ┏┳┓           
┃┃┃┏┓┃┏┓┏┳┓┏┓┃┏┓          
┗┻┛┗ ┗┗┛┛┗┗┗ ┻┗┛          
┳┓   ┓ ┏┓        ┏┓ •     
┣┫┏┓┏┃┏┃┃┏┓┏┓┏┓┏┓┗┓┏┓┏┏┓┏┓
┛┗┗┛┗┛┗┣┛┗┻┣┛┗ ┛ ┗┛┗┗┛┗┛┛ 
┏┓         ┛              
┃┓┏┓┏┳┓┏┓                 
┗┛┗┻┛┗┗┗                                         
'''
print(welcome_note)
# Define the game images!!
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock, paper, scissor]
user_choice = int(input(f"Choose 0 for rock, 1 for paper and 2 for scissor:  \n"))

if user_choice >=3 or user_choice < 0:
    print("You typed an Invalid number!! You Lose!!")
else: 
    print("You chose" + game_images[user_choice])
    # Use random to let the computer choose a random number between 0 and 2
    computer_choice = (random.randint(0, 2))
    # print the computer choice
    print("Computer chose" + game_images[computer_choice])
    # Start comparing between the user choice against the computer choice.
    if user_choice == 0 and computer_choice ==2: 
        print("User Won!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")  
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Won!!")
    elif computer_choice == user_choice:
        print("It's a Draw!!!")   
        
# Exit the game by printing end of game message

print("""     
  ┏┓  ┓  ┏ ┓   ┏┓       
  ┣┏┓┏┫┏┓╋╋┣┓┏┓┃┓┏┓┏┳┓┏┓
  ┗┛┗┗┻┗┛┛┗┛┗┗ ┗┛┗┻┛┗┗┗                                                                       
      """)