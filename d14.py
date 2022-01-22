a={1:200,2:100,3:300,4:150}
m=0
for i in sorted(a):
    print(a[i])
    if a[i]>m:
        m=a[i]
        print("max",m)
    else:
        if a[i]<=m:
            print("min",m)