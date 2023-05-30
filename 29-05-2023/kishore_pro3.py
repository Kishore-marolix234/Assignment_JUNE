""" num = 1
for i in range(1, 5):
    pattern = ""
    for j in range(i):
        pattern = str(num) + pattern
        num += 1
    print(pattern) """

num = 1
for i in range(1, 5):
    pattern = ""
    for j in range(i):
        pattern += str(num)
        num += 1
    if i != 1:  # Exclude the first line from reversal
        pattern = pattern[::-1]
    print(pattern)

 




    
