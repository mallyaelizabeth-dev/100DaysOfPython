target = int(input("Our FizzBuzz target number is: ")) # Accept target number from the user
numbers = range(1, target+1)

for num in numbers:
    # print(num)
    if num % 3 == 0 and num % 5== 0: # Check first if a number meets both of the conditions
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num) # print the number if it doesn't meet any of the above criterias
       


