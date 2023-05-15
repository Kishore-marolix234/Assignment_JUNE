""" To print:
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
* """
n = int(input("Enter the number:"))
for i in range(n,0,-1):
    print("* "*i)
print()   
#or
""" for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    print()   """  
