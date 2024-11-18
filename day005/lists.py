total_height = 0
student_height = input("Enter heights of students, separate one height from another by space: \n").split()
student_height = [int(height) for height in student_height] # Convert each input to an integer

print(f"Our list is: \n  student_height = {student_height}")
highest_height = max(student_height)
print(f"The highest height in the class is: {highest_height}\n")

print("***********************-END-************************ \n")

for height in student_height: # Loop through each height and add it on total height
    total_height += height # Accumulate the total height
print(f"The total height is: {total_height}\n") # This statement has been indented so that we can only get the final result and not iteration of every added value
print("***********************-END-************************ \n")

target = int(input("Our number is: "))  # Get numbers from the users
total_number = 0 # Initialize the total value of the numbers
numbers = range(0, target+1, 2)
print(f"The numbers are: \n numbers = {numbers}")

for number in numbers:
    print(number)
    total_number += number
print(f"The total number of the numbers in range is: {total_number} \n")

print("----------*Alternatively*------------\n")

sum_even = 0
for number in range(1, target+1):
    print(number)
    if number % 2 ==0:
        sum_even += number
print(f"The sum of all even numbers is: {sum_even}")