# initiliaze the total students height to zero.

total_height = 0
student_heights = input("Enter +ve numbers with spaces between one number and another: \n").split()
print(student_heights)
for height in student_heights:
    total_height += int(height)
print(f"total height = {total_height}")

# initiliaze the total no of students to zero
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Number of students = {number_of_students}")
    
average_height = round(total_height / number_of_students)
print(f"The average height for the students is: {average_height}")  




    