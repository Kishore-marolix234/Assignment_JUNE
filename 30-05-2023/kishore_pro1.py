#1.write a program to fetch all even numbers given list?
""" numbers_input = input("Enter a comma-separated list of numbers: ")
l1 = list(map(int, numbers_input.split(','))) """  #The above two code is for user input
l1 = [10, 11, 13, 14, 9, 8]
even_numbers = []

for i in l1:
    if i % 2 == 0:
        even_numbers.append(i)

print("All the even numbers in the list are:", even_numbers)
 
 #or comprehensive way
numbers_input = input("Enter a comma-separated list of numbers: ")
l2 = list(map(int, numbers_input.split(','))) #The above two code is for user input
#l2 = [10, 11, 13, 14, 9, 8]

even_numbers = [num for num in l2 if num % 2 == 0]
print("All the even numbers in the list are:", even_numbers)






    
