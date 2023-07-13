#1. Write a Python function to find the maximum of three numbers.

def find_maximum(a, b, c):
    # Compare a with b and c to find the maximum
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

maximum = find_maximum(num1, num2, num3)
print("The maximum number is:", maximum)
print("---------------------------------")
# 2. Write a Python function to sum all the numbers in a list.
# 	Sample List : (8, 2, 3, 0, 7)
# 	Expected Output : 20

def sumof(l1):
    total = 0
    for i in l1:
        total +=i
    print("The sum of all the element in the list is:",total)

l1 = [8,2,3,0,7]
sumof(l1)
print("---------------------------------")

# 3. Write a Python function to multiply all the numbers in a list.
# 	Sample List : (8, 2, 3, -1, 7)
# 	Expected Output : -336
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Test the function
sample_list = [8, 2, 3, -1, 7]
result = multiply_list(sample_list)
print("The product of the numbers in the list is:", result)
print("---------------------------------")

# 4. Write a Python program to reverse a string.
# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Test the function
sample_string = "1234abcd"
result = reverse_string(sample_string)
print("The reversed string is:", result)
print("---------------------------------")

#5. Write a Python function to calculate the factorial of a number. 
# The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is:", result)
print("---------------------------------")

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# 	Sample String : 'The quick Brow Fox'
# 	Expected Output :
# 	No. of Upper case characters : 3
# 	No. of Lower case Characters : 12

def count_case_characters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Test the function
sample_string = 'The quick Brow Fox'
upper, lower = count_case_characters(sample_string)
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)
print("---------------------------------")

# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]

def get_unique_list(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Test the function
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = get_unique_list(sample_list)
print("Unique List:", result)
print("---------continue in kishore_pro2.py------------")
