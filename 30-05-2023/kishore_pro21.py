""" #22.write a program to fetch all  non-palendram words from  lst?
names=['madam','python','dad','language','eye','malayalam']
 """

names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
non_palindrome_words = []

for word in names:
    if word != word[::-1]:
        non_palindrome_words.append(word)

print("Non-palindrome words:", non_palindrome_words)

#comprehensive way:
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
non_palindrome_words = [word for word in names if word != word[::-1]]

print("Non-palindrome words:", non_palindrome_words)

