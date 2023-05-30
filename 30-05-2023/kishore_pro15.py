""" #16.write a program to fetch all words each contains 'a' charector in the str?
st='python is simple and easy language' """

#st = input("Enter the String:")#for user input
st = 'python is simple and easy language'

words_with_a = []

for word in st.split():
    if 'a' in word:
        words_with_a.append(word)

print("Words containing 'a':", words_with_a)
# comprehensiv way:

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input

words_with_a = [word for word in st.split() if 'a' in word]

print("Words containing 'a':", words_with_a)
