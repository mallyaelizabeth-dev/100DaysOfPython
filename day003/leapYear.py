year = int(input("Enter the year:  "))

# testing if the year entered is divisible by 4 without a reminder then it's a leap year.

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year!")
        else:
            print(f"Year {year} NOT a leap year")
    else:
        print(f"The year {year} is a Leap year.")
else:
    print(f"Year {year} not a leap year") 
    
# Another way of doing it without the Nested ifs.

year = int(input("Enter the year you want to test: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a LEAP year")
else:
    print(f"The year {year} NOT a LEAP year.")