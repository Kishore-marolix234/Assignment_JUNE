""" 3. input = ABBCDEFFGHILJK
output= ABCDEFGHIJK
using join function by direct method """

#input_string =  input("Enter the string: ") #This line is for user input
input_str = "ABBCDEFFGHILJK"
unique_chars = sorted(set(input_str))
result = ''.join(unique_chars)
print(result)

