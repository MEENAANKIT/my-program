n=int(input("enter a number"))
i=2
count=0
while i<=n-1:
    if n%i==0:
        count=count+1
        print("not prime",n)
        break
    i=i+1
if count==0:
    print("prime",i)
