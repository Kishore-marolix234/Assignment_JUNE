""" #3.write a program to fetch all 5 divisible from the list?
l=[12,15,27,20,5] """

# User input option
#user_input = input("Enter elements separated by spaces: ")
#l = [int(num) for num in user_input.split()]

# Hardcoded input option
l = [12, 15, 27, 20, 5]

divisible_by_5 = []
for num in l:
    if num % 5 == 0:
        divisible_by_5.append(num)

print("Numbers divisible by 5:", divisible_by_5)
 
##or comprehensive way:
# User input option
user_input = input("Enter elements separated by spaces: ")
l2 = list(map(int, eval(user_input)))

# Hardcoded input option
# l = [12, 15, 27, 20, 5]

divisible_by_5 = [num for num in l2 if num % 5 == 0]

print("Numbers divisible by 5:", divisible_by_5)
 