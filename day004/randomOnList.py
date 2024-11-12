
import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items-1)


print(names[random_choice] +"," + " You're buying us all dinner!!")
