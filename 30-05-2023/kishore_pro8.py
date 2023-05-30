""" #8.write a program to count no.of vowels in str?
st='python is good language for beginners' """

#st = input("Enter the String:")#for user input
st = 'python is a good language for beginners'
vowel_count = 0

for char in st:
    if char.lower() in 'aeiou':
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)

#Comprehensive Approach:
st = input("enter the String: ")#user input
#st = 'python is a good language for beginners'

vowel_count = sum(1 for char in st if char.lower() in 'aeiou')

print("Number of vowels in the string:", vowel_count)
