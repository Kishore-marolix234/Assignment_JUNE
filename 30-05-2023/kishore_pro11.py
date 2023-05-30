""" #12.write a program to fetch all words which endswith consonent in the given str?
st='python is simple and easy language' """

#st = 'python is simple and easy language'
st = input("Enter the String:")#for user input

words = st.split()
consonant_words = []

for word in words:
    if word[-1].lower() not in ['a', 'e', 'i', 'o', 'u']:
        consonant_words.append(word)

print("Words ending with a consonant:", consonant_words)

#Comprehensive way:

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input

consonant_words = [word for word in st.split() if word[-1].lower() not in ['a', 'e', 'i', 'o', 'u']]

print("Words ending with a consonant:", consonant_words)
