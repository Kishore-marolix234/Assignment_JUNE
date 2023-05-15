""" To print:-
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6
7 7 7 7
8 8 8
9 9
10 """

n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(i,end = " ")
    print()    