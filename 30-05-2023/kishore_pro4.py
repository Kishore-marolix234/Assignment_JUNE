""" #4.write a program to count of total of int values in the list
l=[10,'a',True,30,'b',40] """
#hardcore input
l = [10, 'a', True, 30, 'b', 40]
result = []
for i in l:
    if type(i) == int:
        result.append(i)

total_sum = sum(result)
print("Total sum of integer values:", total_sum)
#hard core input comprehensive way
l = [10, 'a', True, 30, 'b', 40]
result = [i for i in l if type(i) == int]
total_sum = sum(result)
print("Total sum of integer values:", total_sum)

#with user input:
user_input = input("Enter elements separated by spaces: ")
elements = eval(user_input)

integer_values = []
for element in elements:
    if type(element) == int:
        integer_values.append(element)

total_sum = sum(integer_values)
print("Sum of integer values:", total_sum)

#user input comprehensive way:
user_input = input("Enter elements separated by spaces: ")
elements = eval(user_input)

integer_values = [element for element in elements if type(element) == int]

total_sum = sum(integer_values)
print("Sum of integer values:", total_sum)






