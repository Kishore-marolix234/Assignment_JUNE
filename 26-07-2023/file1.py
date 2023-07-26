#1 Function to add two numbers:
def add_numbers(a, b):
    return a + b

#2 Function to check if a number is even:
def is_even(number):
    return number % 2 == 0

#3 Function to calculate the factorial of a number:
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

#4 Function to find the maximum of two numbers:

def max_num(a,b):
    return a if a>b else b

#5 function to  calculate the area of rectangle:

def area_of_rectangle(length,width):
    return length*width

#6 Function to check if a string is pallindrome or not:

def is_pallindrome(s):
    return s==s[::-1]

#7 Function to count the number of occurrences of a character in a string
def count_char_occurrences(s, char):
    return s.count(char)

#8 Function to reverse a string
def reverse_string(s):
    return s[::-1]

#9 Function to convert a string to uppercase
def to_uppercase(s):
    return s.upper()

#10 Function to capitalize the first letter of a string
def capitalize_first_letter(s):
    return s.capitalize()

#11 Function to find the sum of all elements in a list
def list_sum(numbers):
    return sum(numbers)

#12 Function to get the average of elements in a list
def list_average(numbers):
    return sum(numbers) / len(numbers)

#13 Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

#14 Function to reverse a list
def reverse_list(lst):
    return lst[::-1]

#15 Function to find the maximum value in a list
def find_max(lst):
    return max(lst)