"""12. to print 1111
                2222
                3333
                4444 """
size = int(input("Enter the size: "))

# Simple for loop to generate the pattern
for i in range(1, size+1):
    print(str(i) * size)
print()
#or
print("second method")
for i in range(1,size+1):
    for j in range(size):
        print(i,end = '')
    print()  
print("------------------------------------")      

"""13. to print 12345
                12345
                12345
                12345"""

size=int(input("Enter the size: "))
for i in range(1,size+1):
    for j in range(1,size+1):
        print(j,end="")
    print()
print("------------------------------------") 

"""14. To print
5555
4444
3333
2222
1111 """
size=int(input("Enter the size: "))
for i in range(1, size+1):
    print(str(size+1-i) * size)
print()
#or
print("second method")
for i in range(1,size+1):
    for j in range(size):
        print(size+1-i,end = '')
    print()  
print("------------------------------------") 

"""15. To print
54321
54321
54321
54321
54321"""
size=int(input("Enter the size: "))
for i in range(1,size+1):
    for j in range(size):
        print(size-j,end = '')
    print()  
print("------------------------------------") 
""" 
16. To print
1
22
333
4444
55555 """
n = int(input("Enter the size: "))
for i in range(1,n+1):
    print(str(i)*i)
print()    
#or
print("second method")
n = int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end = '')
    print()        
print("------------------------------------")

"""17. To print
5
44
333
2222
11111 """

n = int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n+1-i,end = '')
    print()

"""18. To print
1
12
123
1234
12345  """
n = int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = '')
    print()  
print("------------------------------------")    

"""19.To print
5
54
543
5432
54321 """

n = int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n+1-j,end = '')
    print() 
print("------------------------------------")

"""20. To print:
    1
   22
  333
 4444
55555 """
size = int(input("Enter the size: "))

for i in range(1,size+1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(i, end="")
    print()
print("------------------------------------")

"""21.To print:
    1
   12
  123
 1234
12345 """
size = int(input("Enter the size: "))

for i in range(1,size+1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(j, end="")
    print()
print("------------------------------------")
"""22.To print:
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5 """
size = int(input("Enter the size: "))

for i in range(1,size+1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(i, end=" ")
    print()
print("------------------------------------")    

"""23.To print:
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5 """
size = int(input("Enter the size: "))

for i in range(1,size+1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(j, end=" ")
    print()
print("------------------------------------")  

"""24.To print:

5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1 """
size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end=' ')
    for j in range(i):
        print(i, end=' ')
    print()
print("------------------------------------") 

""" 25.To print
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1 """
size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print("------------------------------------")

"""26.To print:
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1 """
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(i, end=" ")
    print() 
print("------------------------------------")

"""27.To print:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 """
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() 
print("------------------------------------")