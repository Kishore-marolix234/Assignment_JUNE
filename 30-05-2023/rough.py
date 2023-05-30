""" numbers_input = input("Enter a comma-separated list of numbers: ")
numbers_list = list(map(int, numbers_input.split(',')))

even_numbers = []

for num in numbers_list:
    if num % 2 == 0:
        even_numbers.append(num)

print("All the even numbers in the list are:", even_numbers) """
#a1 = eval(input("Enter a comma-separated list of elements: "))
#print(a1)
""" user_input = input("Enter a comma-separated list of elements: ")
a1 = user_input.split(",")

string_elements = [item for item in a1 if isinstance(item, str)]

print("The string elements are:", string_elements) """
""" user_input = input("Enter elements separated by spaces: ")
elements = user_input.split()

string_list = []
for element in elements:
    if type(element)==str:
        string_list.append(element)

print("The string elements are:", string_list) """

""" user_input = input("Enter elements separated by spaces: ")
elements = user_input.split(",")

string_list = list(filter(lambda x: isinstance(x, str), map(eval, elements)))

print("The string elements are:", string_list) """
""" user_input = input("Enter elements separated by spaces: ")
elements = user_input.split(",")

string_list = []

for element in elements:
    evaluated_element = eval(element)
    if type(evaluated_element) == str:
        string_list.append(evaluated_element)

print("The string elements are:", string_list)
 """
""" def get_string_elements(inputs):
    string_elements = []
    for element in inputs:
        if type(element) == str:
            string_elements.append(element)
    return string_elements

# Choose input option
option = input("Choose input option (1 - User Input, 2 - Hardcoded Input): ")

# User input
if option == '1':
    user_input = input("Enter elements separated by spaces: ").split(',')
    input_list = user_input
# Hardcoded input
elif option == '2':
    input_list = ['a', 1, 'hello', True, 4]
else:
    print("Invalid input option!")
    exit()

# Convert string elements to list
string_elements = get_string_elements(input_list)

# Print the string elements
print("The string elements are:", string_elements) """
""" def get_string_elements(inputs):
    string_elements = []
    for element in inputs:
        if type(element) == str:
            string_elements.append(element)
    return string_elements

# User input
user_choice = input("Enter 'U' for user input or 'H' for hardcoded input: ")

if user_choice.lower() == 'u':
    # User input
    user_input = input("Enter elements separated by spaces: ").split(',')
    inputs = [eval(element.strip()) for element in user_input]
else:
    # Hardcoded input
    inputs = [10, 'a', 20, True, 30, 'b', 40]

# Convert string elements to list
string_elements = get_string_elements(inputs) """

""" # User input option
user_input = input("Enter elements separated by spaces: ")
l = eval(user_input)

# Hardcoded input option
# l = ['a', 1, 'hello', True, 4]

string_elements = [str(element) for element in l if isinstance(element, str)]

print("String elements:", string_elements)
 """

""" import ast

user_input = input("Enter elements separated by commas: ")
elements = ast.literal_eval(user_input)

total_sum = 0
for element in elements:
    if isinstance(element, int):
        total_sum += element

print("Sum of integer values from user input:", total_sum) """
""" user_input = input("Enter elements separated by commas: ")
elements = eval(user_input)

total_sum = 0
for element in elements:
    if isinstance(element, int):
        total_sum += element

print("Sum of integer values from user input:", total_sum) """
""" 
l = [10, 'a', True, 30, 'b', 40]
result = []
for i in l:
    if type(i) == int:
        result.append(i)

total_sum = sum(result)
print("Total sum of integer values:", total_sum) """
""" user_input = input("Enter elements separated by commas: ")
elements = user_input.split(",")

total_sum = 0
for element in elements:
    if element.strip().isdigit():
        total_sum += int(element.strip())

print("Sum of integer values:", total_sum) """

""" user_input = input("Enter elements separated by spaces: ")
elements = eval(user_input)

integer_values = [element for element in elements if type(element) == int]

total_sum = sum(integer_values)
print("Sum of integer values:", total_sum) """

""" user_input = input("Enter elements separated by spaces: ")
elements = eval(user_input)

integer_values = []
for element in elements:
    if type(element) == int:
        integer_values.append(element)

total_sum = sum(integer_values)
print("Sum of integer values:", total_sum)
 """

st = 'python is a good language for beginners'
vowels = []

for char in st:
    if char.lower() in 'aeiou':
        vowels.append(char)

print("Vowels in the string:", vowels)



























