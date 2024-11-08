print("Thank you for choosing Python Pizza Deliveries!")

# get the valid size
def get_valid_size():
    size = input("What pizza do you want? S, M, or L: ").upper()
    while size not in ['S', 'M', 'L']: # Force the user to choose from the given letters.
        print("Invalid choice! Please choose between S, M or L!")
        size = input("What pizza do you want? S, M, or L: ").upper()
    return size

# function to get a valid Yes or No response!
def get_valid_yes_no(question):
    choice = input(question).upper()
    while choice not in ['Y', 'N']: # Force the use to choose the correct response!
        print("Invalid input! Please choose either Y or N.")
        choice = input(question).upper()
    return choice
    
size = get_valid_size()

add_pepperoni = get_valid_yes_no("Do you want pepperoni? Y or N: ").upper()
extra_cheese = get_valid_yes_no("Do you want extra cheese? Y or N: ").upper()

# initilizae the bill
bill = 0

# set price of pizza according to different sizes.
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25 

# Add pepperoni

if add_pepperoni == "Y":
    if size == "S":
        bill+=2 # for small pizza
    else:
        bill += 3 # for medium and large pizza

# Add extra cheese 
if extra_cheese == "Y":
    bill += 1
    
    
    
# Final bill
print(f"Your final pizza bill is {bill}")

# A task for tommorrow is to limit the user 
# to choose only the identified characters and 
# to be returned to the prev if the correct one not chosen.