""" Set related Examples """
"""1. Write a program to create an empty set. """
s = set()
print(s)
print(type(s))
print("-----------------------------------")

"""2. Write a program to create a set with five elements. """
# Create a set with mixed elements
my_set = {1, 'a', True, 3.14, 'hello'}

# Print the set
print(my_set)
print(type(my_set))
print("-----------------------------------")

"""3. Write a program to add an element to a set."""
my_set = {1, 'a', True, 3.14, 'hello'}
my_set.add("world")
print(my_set)
print(type(my_set))
print("-----------------------------------")

"""4. Write a program to remove an element to a set. """
my_set = {1, 'a', False, 3.14, 'hello'}
my_set.remove("a")
print(my_set)
print(type(my_set))
print("-----------------------------------")

"""5. Write a program to remove an element from a set. """
my_set = {False, 1, 2.5, 'hello', (1, 2, 3)}
print("Original set:", my_set)

element = input("Enter the element to remove: ")

try:
    if element.isdigit():  # Check if input is a digit (integer)
        element = int(element)
    elif element.lower() == "true":
        element = True
    elif element.lower() == "false":
        element = False
    else:
        try:
            element = float(element)
        except ValueError:
            # Check if input is a tuple
            if element.startswith("(") and element.endswith(")"):
                element = eval(element)  # Convert string to tuple
            else:
                element = element.strip("'\"")  # Strip quotes from the input

    if element in my_set:
        my_set.remove(element)
        print("Element removed successfully.")
    else:
        print("Element not found in the set.")
except (ValueError, KeyError):
    print("Element not found in the set.")

print("Set after removing element:", my_set)

print("-----------------------------------")
"""6. Write a program to find the union of two sets. """
# Two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)

# Print the union set
print("Union set:", union_set)
print("-----------------------------------")
"""7. Write a program to find the intersection of two sets. """
set1 = {1, 2, 3}
set2 = {3, 4, 5}
#intersection of two set:
intersection_of_sets = set1.intersection(set2)
#printing intersection of two sets
print("Intersection set:",intersection_of_sets)
print("-----------------------------------")

"""8. Write a program to check if a set is a subset of another set. """
# Two sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}

# Check if set2 is a subset of set1
is_subset = set2.issubset(set1)

# Print the result
if is_subset:
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")
print("-----------------------------------")

"""9. Write a program to check if two sets are disjoint. """
# Two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8}

# Check if the sets are disjoint
is_disjoint = set1.isdisjoint(set2)

# Print the result
if is_disjoint:
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")
print("-----------------------------------")

"""10. Write a program to find the difference between two sets. """
# Two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the difference between the sets
difference = set1 - set2

# Print the difference
print("Difference between set1 and set2:", difference)

print("-----------------------------------")
"""11. Write a program to clear all elements from a set. """
# Set with elements
my_set = {1, 2, 3, 4, 5}

# Clear the set
my_set.clear()

# Print the set after clearing
print("Set after clearing:", my_set)

print("-----------------------------------")
"""12 Write a program to find the symmetric difference between two sets. """
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_diff = set1 ^ set2  # Using the ^ operator
# symmetric_diff = set1.symmetric_difference(set2)  # Using the symmetric_difference() method

print("Symmetric Difference:", symmetric_diff)

print("-----------------------------------")

"""13 Write a program to find the intersection of multiple sets. """
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

intersection = set1.intersection(set2, set3)

print("Intersection of sets:", intersection)
print("-----------------------------------")
"""14. Write a program to remove the common elements from two sets. """
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1_without_common = set1.difference(set2)
set2_without_common = set2.difference(set1)

print("Set 1 without common elements:", set1_without_common)
print("Set 2 without common elements:", set2_without_common)

print("-----------------------------------")
"""15. Write a program to check if two sets are equal or not. """
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 4}

if set1 == set2:
    print("Set 1 and Set 2 are equal")
else:
    print("Set 1 and Set 2 are not equal")

if set1 == set3:
    print("Set 1 and Set 3 are equal")
else:
    print("Set 1 and Set 3 are not equal")
print("---------------END-----------------")