""" To print reverse of the word for ex:-.
input = "raju is good boy"
output = "boy good is raju" using split function with direct method. """

string = input("Enter the string: ")
words = string.split()
reversed_string = ' '.join(words[::-1])
print(reversed_string)