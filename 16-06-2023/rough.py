""" size = 5

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()  """

""" size = int(input("Enter the size: "))

for i in range(size,0,-1):
    for j in range(size - 1):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print() """
""" size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print() """

""" size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print() """
""" size = int(input("Enter the size: "))

for i in range(size):
    print(' ' * (size - i - 1) + "*" * (i + 1)) """
""" size = int(input("Enter the size: "))

for i in range(1,size+1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(j, end="")
    print() """
""" size = int(input("Enter the size: "))

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end=' ')
    for j in range(i):
        print(i, end=' ')
    print() 

n = int(input("Enter the no. of row:"))
for i in range(n,0,-1):
    print("* "*i)   

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()    """   

   