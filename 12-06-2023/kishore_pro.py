# Empty dictionary to store student data
student_data = {}

# Collecting student data from user input
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks of student {i+1}: "))
    percentage = float(input(f"Enter the percentage of student {i+1}: "))

    student_data[name] = {'Marks': marks, 'Percentage': percentage}

# Displaying the student data as a table
print("Student Data")
print("Name\tMarks\tPercentage")
print("-------------------------")
for name, data in student_data.items():
    marks = data['Marks']
    percentage = data['Percentage']
    print(f"{name}\t{marks}\t{percentage}")
