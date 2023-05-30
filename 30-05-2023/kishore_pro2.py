#2.write a program to fetch all stirng values given list?

def get_string_elements(inputs):
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
string_elements = get_string_elements(inputs)

# Print the string elements
print("The string elements are:", string_elements)

## comprehensive way:

# User input option
user_input = input("Enter elements separated by spaces: ")
l = eval(user_input)

# Hardcoded input option
# l = ['a', 1, 'hello', True, 4]

string_elements = [str(element) for element in l if isinstance(element, str)]

print("String elements:", string_elements)

