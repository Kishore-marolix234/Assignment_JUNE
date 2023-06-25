# # Prompt the user to enter the range
# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# # Display prime numbers within the range
# print(f"Prime numbers between {start} and {end} are:")
# for num in range(start, end + 1):
#     is_prime = True
#     for i in range(2, num + 1):
#         if num % i == 0 and i != num:
#             is_prime = False
#             break
#     if is_prime and num > 1:
#         print(num)
# num = int(input("Enter the value:"))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)
# #or
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num = int(input("Enter the value: "))
# result = factorial(num)
# print(result)
# l1 = [1,2,'Aman',False,3,'Alok',True,4,5]
# for i in range (len(l1)):
#     if i%2==1:
#         print(l1[i])
# n=int(input("enter the last range or value:"))
# for i in range(1,n+1):
#      print(i**3)
# n = 10  # Number of terms
# a = 2   # First term
# d = 3   # Common difference

# series_sum = (n / 2) * (2 * a + (n - 1) * d)
# print("Sum of the series:", series_sum)
# given_string = input("Enter the given string: ")
# new_string = input("Enter the new string: ")
# words = given_string.split()
# middle_index = len(words) // 2

# if len(words) % 2 != 0:
#     words.insert(middle_index + 1, new_string)
# else:
#     words.insert(middle_index, new_string)

# result = ' '.join(words)
# print("Modified string:", result)

# input_string = input("Enter a string: ")

# lowercase_chars = []
# uppercase_chars = []

# for char in input_string:
#     if char.islower():
#         lowercase_chars.append(char)
#     elif char.isupper():
#         uppercase_chars.append(char)

# lowercase_chars.sort()
# uppercase_chars.sort()

# sorted_string = ''.join(lowercase_chars + uppercase_chars)

# print("Sorted string:", sorted_string)
# input_string = input("Enter a string: ")

# letter_count = 0
# digit_count = 0
# symbol_count = 0

# for char in input_string:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif not char.isspace():
#         symbol_count += 1

# print("Number of letters:", letter_count)
# print("Number of digits:", digit_count)
# print("Number of special symbols:", symbol_count)

#15.Append new string in the middle of a given string.

# given_string = "Hello World"
# new_string = " beautifull "
# words = given_string.split()
# middle_index = len(words) // 2

# result = ' '.join(words[:middle_index+1] + [new_string] + words[middle_index+1:])
# print("Modified string:", result)
# print("----------------------------------------")

# input_string = input("Enter a string: ")
# substring = input("Enter a substring: ")

# lower_input = input_string.lower()
# lower_substring = substring.lower()

# occurrences = []
# start_index = 0

# while True:
#     index = lower_input.find(lower_substring, start_index)
#     if index == -1:
#         break
#     occurrences.append((index, index + len(substring)))
#     start_index = index + 1

# print("Occurrences of substring:")
# for start, end in occurrences:
#     print("Start:", start, "End:", end)
# input_string = input("Enter a string: ")

# digits = []
# for char in input_string:
#     if char.isdigit():
#         digits.append(int(char))

# sum_digits = sum(digits)
# average_digits = sum(digits) / max(len(digits), 1)

# print("Digits:", digits)
# print("Sum of digits:", sum_digits)
# print("Average of digits:", average_digits)
# input_string = input("Enter a string: ")

# char_count = {}

# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# print("Character Occurrences:")
# for char, count in char_count.items():
#     print(f"{char}: {count}")

# input_string = input("Enter a string: ")

# char_count = {}

# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 0

#     char_count[char] += 1

# print("Character Occurrences:")
# for char, count in char_count.items():
#     print(f"{char}: {count}")

# s1 = input("Enter the string: ")
# s1 = s1.split(" ")
# s1 = "-".join(s1)
# print(s1)

# l = ["Hii",4,"How",True,"are",5.6,"You",False,"?"]
# l = l[::-1]
# print(l)

# l = ["Hii",4,"How",True,"are",5.6,"You",False,"?"]
# l.reverse()
# print(l)
# l1 = [1,3,5,7,9]
# result = []
# for i in l1:
#     result.append(i*i)
# print(result)    /
# my_list = [1, 2, 7, 4, 5]
# item_to_replace = 7
# new_value = 6

# if item_to_replace in my_list:
#     index = my_list.index(item_to_replace)
#     my_list[index] = new_value

# print(my_list)
l1 = [1,2,3,4,5,6,3,6,7]
rem_item = 6
l2 = [i for i in l1 if rem_item!=i]
print(l2)
