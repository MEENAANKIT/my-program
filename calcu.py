operater=input("enter any operater")
a=int(input("enter first vlue"))
b=int(input("enter second vlue"))
if operater=='+':
    print(a,operater,b,"=",a+b)
elif operater=='-':
    print(a,operater,b,"=",a-b)
elif operater=='*':
    print(a,operater,b,"=",a*b)
elif operater=='/':
    print(a,operater,b,"=",a/b)
else:
    print("invalide operater")