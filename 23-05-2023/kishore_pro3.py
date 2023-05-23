""" 2. program to display all the 
positions of sub string in the given
 string using while loop """

string = input("Enter the string: ")
substring = input("Enter the sub-string: ")
positions = []
start = 0

while start < len(string):
    index = string.find(substring, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

if positions:
    print(f"The sub-string '{substring}' occurs at positions: {positions}")
else:
    print("Sub-string not found in the string.")
