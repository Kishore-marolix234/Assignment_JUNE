#11.Reverse a given integer number.

num = int(input("Enter the value: "))
result = ''.join(reversed(str(num)))
print(result)
#or
print("by second method:")
num = int(input("Enter the value: "))
result = int(str(num)[::-1])
print(result)
print("----------------------------------------")

#12.Use a loop to display elements from a given list present at odd index positions.

l1 = [1,2,'Aman',False,3,'Alok',True,4,5]
print("Elements from l1 which are in odd positions are:")
for i in range(len(l1)):
    if i%2==1:
        print(l1[i])
#or
print("by second method:")
for i in range(1, len(l1), 2):
        print(l1[i])     
print("----------------------------------------")

#13.Calculate the cube of all numbers from 1 to a given number.

n=int(input("enter the last range or value:"))
for i in range(1,n+1):
     print(i**3)
print("----------------------------------------")

#14.Find the sum of the series upto n terms. 
 
n = 10  # Number of terms
a = 2   # First term
d = 3   # Common difference

series_sum = (n / 2) * (2 * a + (n - 1) * d)
print("Sum of the series:", series_sum)
print("----------------------------------------")

#15.Append new string in the middle of a given string.

given_string = "Hello OpenAI Language Model"
new_string = "amazing"
words = given_string.split()
middle_index = len(words) // 2

result = ' '.join(words[:middle_index+1] + [new_string] + words[middle_index+1:])
print("Modified string:", result)
print("----------------------------------------")

#16.Arrange string characters such that lowercase letters should come first.

input_string = input("Enter a string: ")

lowercase_chars = []
uppercase_chars = []

for char in input_string:
    if char.islower():
        lowercase_chars.append(char)
    elif char.isupper():
        uppercase_chars.append(char)

lowercase_chars.sort()
uppercase_chars.sort()

sorted_string = ''.join(lowercase_chars + uppercase_chars)

print("Sorted string:", sorted_string)
print("----------------------------------------")

#17.Count all letters, digits, and special symbols from a given string.

input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0
symbol_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isspace():
        symbol_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)
print("Number of special symbols:", symbol_count)
print("----------------------------------------")

#18: Find all occurrences of a substring in a given string by ignoring the case.

input_string = input("Enter a string: ")
substring = input("Enter a substring: ")

lower_input = input_string.lower()
lower_substring = substring.lower()

occurrences = []
start_index = 0

while True:
    index = lower_input.find(lower_substring, start_index)
    if index == -1:
        break
    occurrences.append((index, index + len(substring)))
    start_index = index + 1

print("Occurrences of substring:")
for start, end in occurrences:
    print("Start:", start, "End:", end)
print("----------------------------------------")

#19.Calculate the sum and average of the digits present in a string.

input_string = input("Enter a string: ")

digits = []
for char in input_string:
    if char.isdigit():
        digits.append(int(char))

sum_digits = sum(digits)
average_digits = sum(digits) / max(len(digits), 1)

print("Digits:", digits)
print("Sum of digits:", sum_digits)
print("Average of digits:", average_digits)
print("----------------------------------------")

#20.Write a program to count occurrences of all characters within a string.
input_string = input("Enter a string: ")

char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Occurrences:")
for char, count in char_count.items():
    print(f"{char}: {count}")


    