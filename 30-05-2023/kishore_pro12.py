""" #13.write a program to fetch all words which 'a' two or more then two times
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
words = st.split()
result = []

for word in words:
    count = word.lower().count('a')
    if count >= 2:
        result.append(word)

print("Words with two or more 'a' occurrences:", result)

# comprehensive way:
#st = 'python is simple and easy language'
st = input("Enter the String:")#for user input
words = [word for word in st.split() if word.lower().count('a') >= 2]

print("Words with two or more 'a' occurrences:", words)

