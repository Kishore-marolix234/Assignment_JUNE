""" #10.write a program to fetch all no.of consonants in the str?
st='pythion language' """
#st = input("Enter the String:")#for user input
st = 'python language'

consonants = []

for ch in st:
    if ch.isalpha() and ch.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consonants.append(ch)

print("Consonants:", consonants)

# comprehensiv approach:
#st = 'python language'
st = input("Enter the String:")#for user input
consonants = [ch for ch in st if ch.isalpha() and ch.lower() not in ['a', 'e', 'i', 'o', 'u']]

print("Consonants:", consonants)

