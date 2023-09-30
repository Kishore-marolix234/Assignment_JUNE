"""1. Write a program to reverse an integer in Python. """

n = int(input("Please give a number: "))
print("Before reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse)
# or using string slicing
num = int(input("Please give a number: "))
print("Before reverse your number is : %d" %num)
rev = int(str(num)[::-1])
print("After reverse the number:", rev)
print("-----------------------------------")

"""2. Write a program in Python to check whether an integer
 is Armstrong number or not. """

n = input("Enter the number: ")
l = len(n)
r=0
for x in n:
    r = int(x)**l + r
if r==int(n):
    print("Number is Armstrong")
else:
    print("Number is not armstrong")   

print("-----------------------------------")

"""3. Write a program in Python to print the Fibonacci series
 using iterative method. """

n = int(input("please give a number for fibonacci series : "))
first,second=0,1
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second
      first = second
      second = result
    print(result)
print("-----------------------------------")   

"""4. sum of digits of number"""
#a using recursion
def sum_of_digits(num):
    # Base case: if the number is a single digit
    if num < 10:
        return num
    else:
        # Recursive call: sum the last digit with the sum of digits of the rest of the number
        return num % 10 + sum_of_digits(num // 10)

# Input from the user
num = int(input("Enter a number: "))

# Calculate the sum of digits
sum_digits = sum_of_digits(num)

print(f"The sum of digits of {num} is: {sum_digits}")

#b using iteration method:
num = input("Enter a number: ")
r = 0
for x in num:
    r = r+int(x)
print("The sum of digits of",num,"is:",r)    
print("-----------------------------------")

"""5. Factorial of a Number. """

#taking an integer input from user
num=int(input("Enter the whole number to find the factorial: "))
factorial = 1
if num < 0:
   	print("Factorial can't be calculated for negative number")
elif num == 0:
   print("Factorial of 0 is 1")
else:
#calculating the factorial of the input number
    for i in range(1,num + 1):
        factorial = factorial*i
    print("Factorial of",num,"is",factorial)
#using recursion:-

def fact(n):  
   if n == 1:  
       return n  
   else:  
#recursion 
       return n*fact(n-1)

num = int(input("Enter a whole number to find Factorial: "))  
if num < 0:  
   print("Factorial can't be calculated for negative number")  
elif num == 0:  
   print("Factorial of 0 is 1")  
else:  
   print("Factorial of",num,"is",fact(num))  