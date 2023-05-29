l1 = [1,2,3,4,3,5,6,4,2,3,7,8]
i = 0
while i<len(l1):
    if l1[i]==3:
        l1.remove(l1[i])
    else:
        i+=1
print(l1)            