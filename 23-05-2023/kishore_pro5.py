""" 3. input = ABBCDEFFGHILJK
output= ABCDEFGHIJK
using join function by using for loop """

#input_string = input("Enter the string: ") #This is for user input
input_string = "ABBCDEFFGHILJK"
unique_chars = []

for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)

output_string = ''.join(unique_chars)
print(output_string)
