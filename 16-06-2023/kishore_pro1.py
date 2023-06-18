"""1. to print * * * * * *
               * * * * * *
               * * * * * *
               * * * * * * """
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print("* ",end = '')
    print()
#or
print("Second Method")
n = int(input("Enter the size: "))
for i in range(n):
    print("* "*n)
#or
print("Third method")    
n = int(input("Enter the size: "))  
pattern = "* "*n + '\n'
square = pattern*n 
print(square)     
print('------------------------')

'''2.To print *
              * *
              * * *
              * * * * 
	          * * * * *'''
n = int(input("Enter the size:"))
for i in range(1,n+1):
    print("* "*i)

#or
print("Second Method")
n = int(input("Enter the size:"))
for i in range(1,n+1):
    for j in range(i):
        print("* ",end = '')
    print()
#or
print("Third Method")
def print_triangle(n):
    if n > 0:
        print_triangle(n - 1)
        print('* ' * n)

size = int(input("Enter the size:"))
print_triangle(size)
print('')
print('------------------------')

"""3 To print
        *
      * *
    * * *
  * * * *
* * * * * """

size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()
print('------------------------')

"""4. To print
* * * * *
* * * *
* * *
* *
* """
n = int(input("Enter the no. of row:"))
for i in range(n,0,-1):
    print("* "*i)
#or
print("second method")
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print('------------------------')

"""5. To print
    *
   * *
  * * *
 * * * *
* * * * * """

size = int(input("Enter the size: "))

for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)

#or
print("Second Method")
size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()

"""6. To print
* * * * *
 * * * *
  * * *
   * *
    * """

size = int(input("Enter the size: "))
for i in range(size,0,-1):
    print(' ' * (size - i) + '* ' * i)
print()        
#or
print("Second Method")
size = int(input("Enter the size: "))
for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
print('------------------------')

"""7. To print
* * * * *
  * * * *
    * * *
      * *
        *
 """
size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print() 
print('------------------------') 

"""8. To print:
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    * """
size = int(input("Enter the size: "))
#upper part
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)

#lower part 
for i in range(size,0,-1):
    print(' ' * (size - i) + '* ' * i)
print()
print('------------------------') 

"""9.To print:
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * * """
size = int(input("Enter the size: "))
#upper part 
for i in range(size,0,-1):
    print(' ' * (size - i) + '* ' * i)

#lower part
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)
print('------------------------') 

"""10.To print:
*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * *
* *
* """
n = int(input("Enter the size:"))
for i in range(1,n+1):
    print("* "*i)

for i in range(n,0,-1):
    print("* "*i)    

print('------------------------')

"""11.To print:
* * * * *
* * * *
* * *
* *
*
*
* *
* * *
* * * *
* * * * * """
n = int(input("Enter the size:"))
for i in range(n,0,-1):
    print("* "*i)

for i in range(1,n+1):
    print("* "*i)
print('------------------------')    