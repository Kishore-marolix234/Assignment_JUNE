# 9. Write a Python program to print the even numbers from a given list.
# 	Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	Expected Result : [2, 4, 6, 8]

def eve(input_list):
    even_list = []
    for num in input_list:
        if num%2==0:
            even_list.append(num)
    return even_list        

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = eve(Sample_List)
print("The even number from the list is:",result)
print("---------------------------------")

# 10. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# 	Sample Items : green-red-yellow-black-white
# 	Expected Result : black-green-red-white-yellow

def sort_hyphen_sequence(input_sequence):
    words = input_sequence.split('-')  # Split the input sequence into individual words
    sorted_words = sorted(words)  # Sort the words alphabetically
    sorted_sequence = '-'.join(sorted_words)  # Join the sorted words back into a hyphen-separated sequence
    return sorted_sequence

# Test the program
sample_sequence = "green-red-yellow-black-white"
result = sort_hyphen_sequence(sample_sequence)
print("Sorted hyphen-separated sequence:", result)
print("---------------------------------")

#11. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30

def square_numbers():
    squares = []
    for num in range(1, 31):
        square = num ** 2
        squares.append(square)
    return squares

# Test the function
result = square_numbers()
print("List of squares:", result)
print("---------------------------------")

#12.Write a Python program to create any chain of function decorators.

def decorator1(func):
    def inner():
        print("Decorator 1")
        func()
    return inner

def decorator2(func):
    def inner():
        print("Decorator 2")
        func()
    return inner

def decorator3(func):
    def inner():
        print("Decorator 3")
        func()
    return inner

@decorator1
@decorator2
@decorator3
def my_function():
    print("Original function")

# Call the decorated function
my_function()
print("---------------------------------")

#13. Write a Python program to access a function inside a function.
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()  # Calling the inner function inside the outer function

# Calling the outer function
outer_function()
print("---------------END------------------")