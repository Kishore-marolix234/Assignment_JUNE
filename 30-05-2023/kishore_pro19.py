""" #20.write program to fetch all words which starts and ends with vowel in str?
st='python is number one language'
 """

#st = input("Enter the String:")#for user input
st = 'python is number one language'
words = st.split()
vowel_words = []

for word in words:
    if word[0].lower() in 'aeiou' and word[-1].lower() in 'aeiou':
        vowel_words.append(word)

print("Words starting and ending with a vowel:", vowel_words)

#comprehensiv way:
st = 'python is number one language'
#st = input("Enter the String:")#for user input
vowel_words = [word for word in st.split() if word[0].lower() in 'aeiou' and word[-1].lower() in 'aeiou']

print("Words starting and ending with a vowel:", vowel_words)
