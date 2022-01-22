a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=int(input("enter number"))
if a>b and a>c and a>d:
    print(a,"a is greater")
elif b>a and b>c and b>d:
    print(b,"b is greater")
elif c>a and c>b and c>d:
    print(c,"c is greater")
else:
    print(d,"d is greater")
