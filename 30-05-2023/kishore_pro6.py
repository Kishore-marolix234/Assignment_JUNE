""" #6write a program to count total no.of words in given string?
 """
#st = input("Enter a string: ")# for user input
st='python is good language for beginners'
if st:
    words = st.split()
    count = len(words)
    print("Total number of words:", count)
else:
    print("Total number of words: 0")

#comprehensive way:

st = input("Enter a string: ")
#st='python is good language for beginners'#hardcore value
count = len(st.split()) if st else 0
print("Total number of words:", count)
