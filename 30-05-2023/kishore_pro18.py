""" #19.write a program to fetch all words which contain odd number of charectors in str?
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
odd_length_words = []
words = st.split()

for word in words:
    if len(word) % 2 != 0:
        odd_length_words.append(word)

print("Words containing odd number of characters:", odd_length_words)

#comprehensive way:
st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input

odd_length_words = [word for word in st.split() if len(word) % 2 != 0]

print("Words containing odd number of characters:", odd_length_words)

