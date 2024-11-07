# simple if block condition..
age = int(input("Enter your age:  "))
if age >=18:
    print("You are allowed to Enter")
else:
    print("You are not allowed to Enter!!")

# print("#########################################")    

# Nested if function if/else:
height = int(input("Enter your height:  " + "cm"))
age = int(input("Enter your age:  "))

if height >=120:
    print("You can ride the rollercoaster!!")
    if age <= 18:
        print("You can pay 7$")
    else:
        print("Please pay 12$")
else:
    print("You are too short, You cannot ride the rollercoster!!")

print("***************************************")

# Nested if/elif/else functions (Applicable when you have multiple conditons to be changed.)