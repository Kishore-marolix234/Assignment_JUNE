""" #18.write a program to fetch all words which contain only 4 or lessthen 4 charectors?
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
words_4_or_less = []
words = st.split()

for word in words:
    if len(word) <= 4:
        words_4_or_less.append(word)

print("Words containing 4 or fewer characters:", words_4_or_less)

#comprehensiv way:
st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
words_4_or_less = [word for word in st.split() if len(word) <= 4]

print("Words containing 4 or fewer characters:", words_4_or_less)
