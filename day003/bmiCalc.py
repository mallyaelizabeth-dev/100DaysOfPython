weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cm: "))

height_in_squared_metre = ((height/100)**2)

BMI = (weight/height_in_squared_metre)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f} and you are underweight!")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.2f} ,You have a normal weight!!")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.2f} and You are slightly overweight!!")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI:.2f} and I'm sorry to say but, You are Obese!!!")
else:
    print(f"Your BMI is {BMI:.2f} and You are clinically Overweight!!")
    
print("*******************#END#**************************")

# :.2f formatting was used to control the display of floating-point numbers