""" #5.write a program to count of total no.of charectors in given string(include spaces)
st='python language """
st = input("Enter the strings: ") #for user input
#st = 'python language'

if len(st) == 0:
    print("String value can't be left empty")
else:
    count = len(st)
    print("Total number of characters:", count)


#by using comprehensive way:

#st = input("Enter a string: ")# for user input
st = 'python language'

count = len(st) if len(st) > 0 else "String value can't be left empty"
print("Total number of characters:", count)

