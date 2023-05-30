"""  #25.write a program to fetch longest  palendram word
names=['madam','python','dad','language','eye','malayalam','narayaayaran']"""

names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam', 'narayaayaran']
longest_palindrome = ''

for word in names:
    if len(word) > len(longest_palindrome) and word == word[::-1]:
        longest_palindrome = word

print("Longest palindromic word:", longest_palindrome)

#comprehensive:
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam', 'narayaayaran']
longest_palindrome = max([word for word in names if word == word[::-1]], key=len)

print("Longest palindromic word:", longest_palindrome)
