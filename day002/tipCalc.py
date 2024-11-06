print("Welcome to the tip calculator!")

initialBill = int(input("What is the total bill? $"))

tipPercent = (int(input("How much tip percernt would you like to give? 10, 12, or 15? ")))


if(tipPercent == 10):
    totalBill = ((initialBill*(10/100)) + initialBill)
elif(tipPercent == 12):
    totalBill = ((initialBill*(12/100)) + initialBill)
elif(tipPercent == 15):
    totalBill = ((initialBill*(15/100)) + initialBill)
else:
    print("No such percentage!")

noOfPeople = int(input("How many people to split the bill? "))


eachPay = input("Each person should pay: $" + str(totalBill/noOfPeople))

print("*********************************************************************")
