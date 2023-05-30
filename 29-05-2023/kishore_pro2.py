#S = input("Enter the word: ") #For user input.
S = ' python'
length = len(S)

for i in range(1, length + 1):
    pattern = ""
    for j in range(i):
        pattern += S[j].capitalize()
    print(pattern)

for i in range(length - 1, 0, -1):
    pattern = ""
    for j in range(i):
        pattern += S[j].capitalize()
    print(pattern)

#or by using slicing operator:-

""" for i in range(1, length + 1):
    pattern = S[:i].capitalize()
    print(pattern)

for i in range(length - 1, 0, -1):
    pattern = S[:i].capitalize()
    print(pattern) """
    
