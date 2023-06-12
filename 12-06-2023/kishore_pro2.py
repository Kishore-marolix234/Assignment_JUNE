# Empty dictionary to store student data
student_data = {}

# Prompt user for student information
while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name == 'q':
        break

    marks = int(input("Enter marks: "))
    percentage = float(input("Enter percentage: "))

    # Add student information to the dictionary
    student_data[name] = {'Marks': marks, 'Percentage': percentage}

# Displaying the student data as a table
print("Student Data")
print("Name\tMarks\tPercentage")
print("-------------------------")
for name, data in student_data.items():
    marks = data['Marks']
    percentage = data['Percentage']
    print(f"{name}\t{marks}\t{percentage}")
