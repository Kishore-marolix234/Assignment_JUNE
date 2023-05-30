""" #14.write a program to count number of charector  of each word in the str?
st='python is simple and easy language' """

st = 'python is simple and easy language'
#st = input("Enter the String:")#for user input
word_lengths = []
words = st.split()

for word in words:
    word_lengths.append(len(word))

print("Word lengths:", word_lengths)

#comprehensive way:
#st = 'python is simple and easy language'
st = input("Enter the String:")#for user input
word_lengths = [len(word) for word in st.split()]

print("Word lengths:", word_lengths)

