# My codes without the tutorial, I just did it on the go as soon
# as I saw what was the project about...
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

# And this is how my instructor went through about it.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")