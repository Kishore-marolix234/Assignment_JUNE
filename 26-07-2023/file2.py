# Import the example_functions module
import file1

#1 Call the add_numbers function
sum_result = file1.add_numbers(5, 7)
print("Sum:", sum_result)
print("------------------------------------")

#2 Call the is_even function
num = 10
if file1.is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
print("------------------------------------")

#3 Call the factorial function
factorial_result = file1.factorial(5)
print("Factorial of 5:", factorial_result)
print("------------------------------------")

#4 Call the max_number function
max_result = file1.max_num(15, 7)
print("Max number:", max_result)
print("------------------------------------")

#5 Call the rectangle_area function
length = 5
width = 10
area_result = file1.area_of_rectangle(length, width)
print(f"Area of rectangle with length {length} and width {width}: {area_result}")
print("------------------------------------")

#6 Call the is_palindrome function
word = "radar"
if file1.is_pallindrome(word):
    print(f"{word} is a pallindrome.")
else:
    print(f"{word} is not a pallindrome.")
print("------------------------------------")

#7 to count the number of occurrences of a character in a string
text = "Hello, World!"
char_count = file1.count_char_occurrences(text, 'l')
print("Number of 'l' occurrences:", char_count)
print("------------------------------------")

#8 to reverse a string
reversed_text = file1.reverse_string(text)
print("Reversed text:", reversed_text)
print("------------------------------------")

#9 to convert a string to uppercase
uppercase_text = file1.to_uppercase(text)
print("Uppercase text:", uppercase_text)
print("------------------------------------")

#10 to capitalize the first letter of a string
capitalized_text = file1.capitalize_first_letter(text)
print("Capitalized text:", capitalized_text)
print("------------------------------------")

# List operations
#11 to find the sum of all elements in a list
numbers = [1, 2, 3, 4, 4, 5, 5, 6]
sum_result = file1.list_sum(numbers)
print("Sum of numbers:", sum_result)
print("------------------------------------")

#12 to get the average of elements in a list
average_result = file1.list_average(numbers)
print("Average of numbers:", average_result)
print("------------------------------------")

#13 to remove duplicates from a list
unique_numbers = file1.remove_duplicates(numbers)
print("List with duplicates removed:", unique_numbers)
print("------------------------------------")

#14 to reverse a list
reversed_numbers = file1.reverse_list(numbers)
print("Reversed list:", reversed_numbers)
print("------------------------------------")

#15 to find the maximum value in a list
numbers = [5, 8, 2, 1, 10]
max_value = file1.find_max(numbers)
print("Maximum value:", max_value)
print("--------------END-------------------")
