string = "aabbcdeaabbceder"
vowel_count = {}

for letter in string:
    if letter.lower() in 'aeiou':
        if letter.lower() in vowel_count:
            vowel_count[letter.lower()] += 1
        else:
            vowel_count[letter.lower()] = 1

print(vowel_count)
