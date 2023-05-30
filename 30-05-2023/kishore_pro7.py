""" #7write a program to fetch all vowels from the string?
st='python is good language for beginners'
 """

st = input("Enter the string: ")# for user input
#st = 'python is a good language for beginners'
vowels = []

for char in st:
    if char.lower() in 'aeiou':
        vowels.append(char)

print("Vowels in the string:", vowels)
 #Comprehensiv approach:
#st = input("Enter the string: ")# for user input
st = 'python is a good language for beginners'
vowels = [char for char in st if char.lower() in 'aeiou']

print("Vowels in the string:", vowels)
