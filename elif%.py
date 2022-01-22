i=1
n=100
while i<=n:
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    elif i%3==0 and i%7==0:
        print("navgurukul")
    else:
        print(i)
    i=i+1

