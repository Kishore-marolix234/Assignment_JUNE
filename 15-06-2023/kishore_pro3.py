string = "aabbcdeaabbceder"
letter_count = {}

for letter in string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)
