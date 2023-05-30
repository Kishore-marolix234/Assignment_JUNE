""" #23.write a program to fetch all  palendram words which starts with 'm' charector?
names=['madam','python','dad','language','eye','malayalam'] """

names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words_starting_with_m = []

for word in names:
    if word.startswith('m') and word == word[::-1]:
        palindrome_words_starting_with_m.append(word)

print("Palindromic words starting with 'm':", palindrome_words_starting_with_m)

#comprehensive way:
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
palindrome_words_starting_with_m = [word for word in names if word.startswith('m') and word == word[::-1]]

print("Palindromic words starting with 'm':", palindrome_words_starting_with_m)
