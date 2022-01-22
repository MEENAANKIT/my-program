d={1:"ankit",2:2,3:"ankit",4:2,5:5}
d2={}
for key,value in d.items():
    if value not in d2.values():
        d2[key]=value
print(d2)

