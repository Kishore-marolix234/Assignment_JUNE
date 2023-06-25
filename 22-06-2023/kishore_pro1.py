#1. Calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter the value:"))
result = 0
for i in range(1,n+1):   #iterate over the range.
    result = result+i    #adding preceding value with current value of i.
print("The total of all the numbers from 1 to", n, "is",result)    
print("----------------------------------------")
#2. Write a program to print multiplication table of a given number.

n = int(input("Enter the value:"))
print("The table of",n,"is:")
for i in range(1,11):
    result = n*i
    
    print("{} x {} = {}".format(n, i, result))
print("----------------------------------------")

#3.Display numbers from a list using loop.    

l1 = [10,20,40,30,12,16,25]
print("The numbers from list l1 are:")
for i in l1:
    print(i)
print("----------------------------------------")

#4: Count the total number of digits in a number.

num = int(input("Enter the number:"))
result = len(str(num))
print("Total number of digits in a number: ",result)
print("----------------------------------------")

#5.Print list in reverse order using a loop.

l1 = [10,20,40,30,12,16,25]
#reversing the list
l1 = l1[::-1]
print("values of above list in reverse order is:")
for i in l1:    #iterate over the list l1 after reverse.
    print(i)
print("----------------------------------------")

#6.Display numbers from -10 to -1 using for loop.

print("The numbers from -10 to -1 are listed below:")
# Iterate over a range of numbers
for i in range(-10,0):
    print(i)
print("----------------------------------------")

#7.Use else block to display a message “Done” after successful execution of for loop.

# Iterate over a range of numbers
for i in range(1, 6):
    print(i)
else:
    print("Done")
print("----------------------------------------")

#8.Write a program to display all prime numbers within a range.

# Prompt the user to enter the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Display prime numbers within the range
print("Prime numbers between {} and {} are:".format(start,end))
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num+1):
            if num % i == 0 and num!=i :
                is_prime = False
                break
        if is_prime:
            print(num)
print("----------------------------------------")

#9.Display Fibonacci series up to 10 terms.
n=int(input("Enter the number of terms: "))
a=0 
b=1 
if n<=0:
    print("The Output of your input is",a)
else:
    print(a,b,end=" ")
    for x in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
print("\n")
print("----------------------------------------")

#10.Find the factorial of a given number.

num = int(input("Enter the value:"))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)
#or using recursion
print("by second method")
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter the value: "))
result = factorial(num)
print(result)
print("----------------------------------------")

