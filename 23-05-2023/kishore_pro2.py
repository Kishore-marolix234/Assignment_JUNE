""" To print reverse of the word for ex:-.
input = "raju is good boy"
output = "boy good is raju" using split function with any loop. """

#iam using for loop for the solution

string = input("Enter the string: ")
words = string.split()
reversed_string = ""

for i in range(len(words)):
    reversed_string = words[i] + " " + reversed_string

print(reversed_string)
