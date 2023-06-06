"""1. write a program to take tuple of numbers from 
your key board and print sum , average """

# Take input from the keyboard as a tuple of numbers
numbers = tuple(map(float, input("Enter numbers separated by commas: ").split(',')))
print(numbers)
# Calculate the sum
total_sum = sum(numbers)

# Calculate the average
average = total_sum / len(numbers)

# Print the sum and average
print("Sum:", total_sum)
print("Average:", average)