"1. Addition program using function"
def add(a,b):
    a = int(input("Enter the value: "))
    b = int(input("Enter the value: "))
    r = a+b
    print(r)
add(11,12)    
#or
print("second method")
def add(a,b):
    """ a = int(input("Enter the value: "))
    b = int(input("Enter the value: ")) """
    r = a+b
    return r
result = add(12,13)
print(result)
print("---------------------------------")
#2.Odd_even program using function
def odd_even(x):
    x = int(input("Enter the number:"))
    if x%2==0:
        print(x,"is the even number.")
    else:
        print(x,"is the odd number.")
odd_even(4)            
#or
print("second method")
def odd_even(x):
    if x%2==0:
        r = print(x,"is the even number.")
    else:
        r = print(x,"is the odd number.")
    return r    
x = int(input("Enter the number:"))    
result = odd_even(x)
print(result)    
print("---------------------------------")

#3.CalC using function:
def calc(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    print("Addition of the number", a,'and', b, "is:",add)
    print("subtraction of the number", a ,'and', b, "is:",sub)
    print("multiplication of the number", a, 'and', b, "is:",mul)
    print("division of the number", a, 'and', b, "is:",div)

calc(6,2)    
#or
print("second method")
def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = calc(a, b)

print("Addition of the numbers", a, 'and', b, "is:", result[0])
print("Subtraction of the numbers", a, 'and', b, "is:", result[1])
print("Multiplication of the numbers", a, 'and', b, "is:", result[2])
print("Division of the numbers", a, 'and', b, "is:", result[3])
print("---------------------------------")

"""4.To find the maximum of 2 and max of 3 numbers  """
def max_of_two(x, y):
    if x > y:
        print(x)
    else:
        print(y)

def max_of_three(x, y, z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

max_of_three(3, 6, -5)

#or
print("second method")
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))
print("---------------------------------")

#5.To print square of the numbers by function:
def squa(num):
    square = num*num
    print("Square of the number is",square)
squa(5)
#or
print("second method")

def squa(num):
    square = num*num
    return square

result = squa(5)
print("Square of the number is", result)
print("---------------------------------")
    
#6.Write a Python function to sum all the numbers in a list.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    print(total)

sum((8, 2, 3, 0, 7))
#or
print("second method")
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
print("---------------------------------")

#7.Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    print(total)

multiply((8, 2, 3, -1, 7))
#or
print("second method")

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))
print("---------------------------------")

#To find faactorial of a number:
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

n = int(input("Input a number to compute the factorial: "))
result = factorial(n)
print(result)

#or
print("second method")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))







