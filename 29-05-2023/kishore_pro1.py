""" string = "python"
length = len(string)

for i in range(1, length + 1):
    pattern = string[:i] * i
    print(pattern) """
#or
string = "python"
#pattern = ""

for i in range(1, len(string) + 1):
    pattern = ""
    for j in range(i):
        pattern += string[j]    
    pattern = pattern * i
    print(pattern)

