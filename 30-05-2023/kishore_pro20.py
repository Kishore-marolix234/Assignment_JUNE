""" #21.write a program to fetch all palendram words from  lst?
names=['madam','python','dad','language','eye','malayalam'] """

names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words = []

for word in names:
    if word == word[::-1]:
        palindrome_words.append(word)

print("Palindrome words:", palindrome_words)

#comprehensive approach:
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words = [word for word in names if word == word[::-1]]

print("Palindrome words:", palindrome_words)

