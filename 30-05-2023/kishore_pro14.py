""" #15.write a program to fetch the first  and last charector for each word in str?
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
word_chars = []

words = st.split()

for word in words:
    first_char = word[0]
    last_char = word[-1]
    word_chars.append((first_char, last_char))

print("First and last characters of each word:", word_chars)

# comprehensive way:

#st = 'python is simple and easy language'
st = input("Enter the String:")#for user input
word_chars = [(word[0], word[-1]) for word in st.split()]

print("First and last characters of each word:", word_chars)
