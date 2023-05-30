""" #11.write a program to fetch all words which starts with vowel from given str?
st='python is a simple and easy language'(note:10th question is repetative question) """

st = 'python is a simple and easy language'
#st = input("Enter the String:")#for user input

words = st.split()
vowel_words = []

for word in words:
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_words.append(word)

print("Words starting with a vowel:", vowel_words)

#comprehensive way:
#st = 'python is a simple and easy language'
st = input("Enter the String:")#for user input
vowel_words = [word for word in st.split() if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]

print("Words starting with a vowel:", vowel_words)

