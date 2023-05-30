""" #17.write a program to fetch all words does not contain 'e' charector in str?
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input

words_without_e = []

for word in st.split():
    if 'e' not in word:
        words_without_e.append(word)

print("Words not containing 'e':", words_without_e)

# comprehensiv approach:
st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
words_without_e = [word for word in st.split() if 'e' not in word]

print("Words not containing 'e':", words_without_e)

