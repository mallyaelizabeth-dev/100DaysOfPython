print("Welcome to Treasure Island, Your mission is to find the treasure!")

print("Your mission is to find the hidden treaure. Good Luck!!")

left_or_right = input('Which direction do you want to take? "left" or "right"?:\n ').lower()

if left_or_right == "left":
    # continue
    swim_or_wait = input('You wanna "Swim" or "Wait"?:\n ').lower()
    if swim_or_wait == "wait":
        # continue
        which_door = input('Which Door do you wanna take, "Blue", "Red" or "Yellow"?:\n ').lower()
        if (which_door == "yellow"):
            # continue
           print("You found the treasure!!") 
        else:
            print("You got lost, Game over for you")
    else:
        print("You drown, Game over!")
else:
    print("You fell into the hole, Game over for you!")

     