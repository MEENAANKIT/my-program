# def add():
#     def sub():
#         x=10
#         y=20
#         c=y-x
#         print(c)
#     x=10
#     y=20
#     d=x+y
#     print(d)
#     sub()
# add()

# def add ():
#     def sub ():
#         def div():
#             x=20
#             c=x/2
#             print(c)
#         x=20
#         y=10
#         c=x-y
#         print(c)
#         div()
#     x=10
#     y=20
#     c=x+y
#     print(c)
#     sub()
# add()
ages=[15,12,17,18,32,22,38,49]
def myfun(x):
    if x<18:
        return False
    else:
        return True
audels=list(filter(myfun,ages))
for x in audels:
    print(x)
    print(type(x))





