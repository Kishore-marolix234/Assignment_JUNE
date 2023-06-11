# Empty dictionary
my_dict = {}

# Lists of keys and values
keys = ['a', 'b', 'c','d','e']
values = [1, True, 'Alok',2.5,False]

# Check if the length of keys and values is the same
if len(keys) == len(values):
    # Iterate through the range based on the length of the keys or values list
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]

    # Print the filled dictionary
    print(my_dict)
else:
    print("The number of keys and values does not match.")

##using while Function:
# Empty dictionary
my_dict = {}

# Lists of keys and values
keys = ['a', 'b', 'c','d']
values = [1, 2, 3,1+2j]

# Check if the length of keys and values is the same
if len(keys) == len(values):
    # Initialize index variable
    i = 0

    # Iterate until the index reaches the length of the keys or values list
    while i < len(keys):
        my_dict[keys[i]] = values[i]
        i += 1

    # Print the filled dictionary
    print(my_dict)
else:
    print("The number of keys and values does not match.")
