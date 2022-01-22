a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[]
for i in range(5):
    b.append(a[i]**2)
for i in range(-1,-5,-1):
    b.append(a[i]**2)
print(b)

