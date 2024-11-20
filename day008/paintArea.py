import math
def paint_calc(height, width, coverage):
    # height = input("Height of the wall is: ")
    # width = input("Width of the wall is: ")
    # coverage = input("Coverage of the wall is: ")
    # no_of_cans = round((height*width)/coverage) # Rounds to the nearest number (up or down based on 0.5 rule).
    no_of_cans = math.ceil((height*width)/coverage) # Always rounds up to the next whole number.
    print(f"The number of cans needed to paint this wall is: {no_of_cans}")

paint_calc(height= int(input("Height of the wall is: ")), width= int(input("Width of the wall is: ")),coverage = int(input("Coverage of the wall is: ")) )
