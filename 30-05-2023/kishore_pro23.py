""" #24.write a program to fetch all  palendram words which more then 3 charectors?
names=['madam','python','dad','language','eye','malayalam'] """
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words = []

for word in names:
    if len(word) > 3 and word == word[::-1]:
        palindrome_words.append(word)

print("Palindromic words with more than 3 characters:", palindrome_words)

# comprehensiv way:
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words = [word for word in names if len(word) > 3 and word == word[::-1]]

print("Palindromic words with more than 3 characters:", palindrome_words)
