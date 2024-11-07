# simple if block condition..
# age = int(input("Enter your age:  "))
# if age >=18:
#     print("You are allowed to Enter")
# else:
#     print("You are not allowed to Enter!!")

# print("#########################################")    

# Nested if function if/else:
height = int(input("Enter your height in cm:  "))
age = int(input("Enter your age:  "))
bill = 0

if height >=120:
    print("You can ride the rollercoaster!!")
    if age <= 12:
        bill = 5
        print("Child tickets are 5$")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    else:
        bill = 12
        print("Adult tickets are 12$")
        
    wants_photo = input("Do you want your photo taken Y or N. ").upper() #used the upper() method so a user can use caps or small letters
    if wants_photo == "Y":
        bill +=3
    print(f"Your final bill is {bill} ")
else:
    print("You are too short, You cannot ride the rollercoster!!")

print("***************************************")

# Nested if/elif/else functions (Applicable when you have multiple conditons to be changed.)