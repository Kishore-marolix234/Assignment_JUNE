""" Tuple related examples """

"""1. Write a program to create an empty tuple """
t = ()
print(t)
print(type(t))

print("-------------------------------------")
"""2. Write a program to create a tuple with five elements of different data types. """
t = (4,True,"Aman",6.0,5,False,"Kishore")
print(t)
print(type(t))

print("-------------------------------------")
"""3. Write a program to access and print the third element of a tuple. """
t = (4,True,"Aman",6.0,5,False,"Kishore")
print(t[3])
print(type(t[3]))

"""4. Write a program to find the length of a tuple. """
t = (4,True,"Aman",6.0,5,False,"Kishore")
print("The length of tuple is:",len(t))

print("-------------------------------------")
"""5.Write a program to concatenate two tuples """
t = (4,True,"Aman",6.0,5,False,"Kishore")
t1 = (1,3,5,7,2,3,4)
result = t + t1
print("The concaneted tuple of t and t1 is:",result)
print(type(result))

print("-------------------------------------")
"""6. Write a program to check if an element exists in a tuple. """

tuple1 = (1, 'a', True, 3.14, 'Hello')
element = "a"
if element in tuple1:
    print("Element exists in tuple")
else:
    print("Element doesnot exists in tuple") 

print("-------------------------------------")
"""7. Write a program to count the number of occurrences of an element in a tuple. """
t = ('a', 1, 'b', 2, 'c', 'a', 'b', 'd', 'a')
element = 'a'
occurance = t.count(element)
print("Number of occurrences of",element,"in the tuple:",occurance)
#or
t = ('a', 1, 'b', 2, 'c', 'a', 'b', 'd', 'a')
element = 'a'

occurrences = 0
for item in t:
    if item == element:
        occurrences += 1

print("Number of occurrences of", element, "in the tuple:", occurrences)

print("-------------------------------------")
"""8. Write a program to convert a tuple into a list. """
t = ('a', 1, 'b', 2, 'c', 'a', 'b', 'd', 'a')
print(t)
print(type(t))
l1 = list(t)
print(l1)
print(type(l1))

print("-------------------------------------")
""" 9.Write a program to convert a tuple into a string."""
t = ('a', 1, 'b', 2, 'c', 'a', 'b', 'd', 'a')
print(t)
print(type(t))
s1 = str(t)
print(s1)
print(type(s1))

print("-------------------------------------")
""" 10.Write a program to reverse a tuple. """
tuple1 = (1, 'a', True, 3.14, 'Hello')
print(tuple1)
print("Reversed of the above tuple is:",tuple(reversed(tuple1)))
#or
print("Reversed of the above tuple using indexing is:",tuple1[::-1])

print("-------------------------------------")
"""11. Write a program to find the maximum and minimum values in a tuple. """
my_tuple = (10, 5, 20, 15, 25)
maximum = max(my_tuple)
minimum = min(my_tuple)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

print("-------------------------------------")
"""12. Write a program to sort a tuple in ascending order. """
my_tuple = (10, 5, 20, 15, 25)
ans = tuple(sorted(my_tuple))
print("The sorted tuple in ascending order is",ans)

print("-------------------------------------")
"""13. Write a program to count the number of even and odd numbers in a tuple. """
t1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
even_count = 0
odd_count = 0
for i in t1:
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1

print("Total number of Even numbers are:",even_count)
print("Total number of odd numbers are:",odd_count)

print("-------------------------------------")
"""14. Write a program to find the sum of all the numbers in a tuple. """
mixed_tuple = ('a', 1, 'b', 2, True, 3, 'd', 4, False, 5)
num = 0
print("numbers in a tuple are:")
for i in mixed_tuple:
    if type(i)==int:
         print(i)
         num = num+i
print("The total number of Number in a tuple are:",num)
print("-------------------------------------")

"""15.Write a program to find the second largest element in a tuple. """

my_tuple = (10, 5, 8, 15, 20, 12)

# Convert the tuple to a list for easy manipulation
my_list = list(my_tuple)

# Sort the list in descending order
my_list.sort(reverse=True)

# Find the second largest element
second_largest = None
for element in my_list:
    if element < max(my_list):
        second_largest = element
        break

print("Second largest element:", second_largest)
print("-------------------END------------------")
