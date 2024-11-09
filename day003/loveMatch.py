print("The love calculator is calculating your scores..!!")
name1 = input("What is the name of the first individual?:  ").lower()
name2 = input("What is the name of the second individual?:  ").lower()

combined_names = name1 + name2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

first_digit = t + r + u + e
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

second_digit = l + o + v + e
# We combine turn the digits into string and combine them and not add.
# We also change them back into integer so that we can test them using conditionals
score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"The score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

 
