#21.Reverse a given string.

s1 = input("Enter the String: ")
s1 = s1[::-1]
print(s1)
#if you want to reverse on the basis of word:
s1 = input("Enter the string: ")
s1 = s1.split(" ")
s1 = s1[::-1]
s1 = ' '.join(s1)
print(s1)
print("-----------------------------------------")

#22.Split a string on hyphens.

s1 = input("Enter the string: ")
s1 = s1.split(" ")
s1 = "-".join(s1)
print(s1)
print("-----------------------------------------")

#23.Remove empty strings from a list of strings.

my_list = ["Hello", "", "World", "", "Python", ""]

filtered_list = []
for string in my_list:
    if string != "":
        filtered_list.append(string)

print(filtered_list)
#or
print("by second method")
my_list = ["Hello", "", "World", "", "Python", ""]

my_list = list(filter(lambda string: string != "", my_list))

print(my_list)
print("-----------------------------------------")

#24.Removal all characters from a string except integers.

input_string = "abc123xyz456"

result_string = ""
for char in input_string:
    if char.isdigit():
        result_string += char

print(result_string)
#or
print("by second method")
input_string = "abc123xyz456"

result_string = ''.join([char for char in input_string if char.isdigit()])

print(result_string)
print("-----------------------------------------")

#25: Reverse a list in Python.

l = ["Hii",4,"How",True,"are",5.6,"You",False,"?"]
l = l[::-1]
print(l)
#or
l = ["Hii",4,"How",True,"are",5.6,"You",False,"?"]
l.reverse()
print(l)
print("-----------------------------------------")

#26.Concatenate two lists index-wise.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = []
for i in range(min(len(list1), len(list2))):
    concatenated_list.append(list1[i] + list2[i])

print(concatenated_list)
#or
print("by second method: ")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = [x + y for x, y in zip(list1, list2)]

print(concatenated_list)
print("-----------------------------------------")

#27: Turn every item of a list into its square.

l1 = [1,3,5,7,9]
result = []
for i in l1:
    result.append(i*i)
print(result)    
#or
print("by second method: ")
l1 = [1,3,5,7,9]

result = [item ** 2 for item in l1]

print(result)
print("-----------------------------------------")

#28: Add new item to list after a specified item.

my_list = [1, 2, 3, 4, 5]
specified_item = 3
new_item = 6

index = my_list.index(specified_item)  # Find the index of the specified item
my_list.insert(index + 1, new_item)    # Insert the new item after the specified item

print(my_list)
print("-----------------------------------------")

#29: Replace list’s item with new value if found.

my_list = [1, 2, 3, 4, 5]
item_to_replace = 3
new_value = 6

if item_to_replace in my_list:
    index = my_list.index(item_to_replace)
    my_list[index] = new_value

print(my_list)
print("-----------------------------------------")

#30.Remove all occurrences of a specific item from a list.

l1 = [1,2,3,4,5,6,3]
rem_item = 3
l2 = []
for i in l1:
    if i!= rem_item:
        l2.append(i)
print(l2)
#or 
print("by second method:")
l1 = [1,2,3,4,5,6,3,6,7]
rem_item = 6
l2 = [i for i in l1 if i!=rem_item]
print(l2)
#or
print("by third method")
my_list = [1, 2, 3, 4, 2, 5, 2]
item_to_remove = 2

while item_to_remove in my_list:
    my_list.remove(item_to_remove)

print(my_list)
print("-----------------END---------------------")
