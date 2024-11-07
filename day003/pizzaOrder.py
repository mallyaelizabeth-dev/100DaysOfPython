print("Thank you for choosing Python Pizza Deliveries!")

size = input("What pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# initilizae the bill
bill = 0

# set price of pizza according to different sizes.
if size == "S":
    bill = 15
elif size == "M":
    bill == 20
elif size == "L":
    bill == 25 

# Add pepperoni

if add_pepperoni == "Y":
    if size == "S":
        bill+=2 # for small pizza
    else:
        bill += 3 # for medium and large pizza
else:
    print("Unkown selection")    
# Add extra cheese 
if extra_cheese == "Y":
    bill += 1

# Final bill
print(f"Your final pizza bill is {bill}")

# A task for tommorrow is to limit the user 
# to choose only the identified characters and 
# to be returned to the prev if the correct one not chosen.