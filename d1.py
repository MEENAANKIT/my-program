a={1:"aman",4:"khemu",3:"ram"}
print(len(a))
print(sorted(a))
#method
print("keys- ",a.keys())
print("values- ",a.values())
print("items- ",a.items())
print("get- ",a.get(3))
#a.clear()
#print(a)
b=a.copy
print("copy- ",b)
print("pop- ",a.pop(1))
print("popitem- ",a.popitem())
x=["name","class","rollno","address"]
b={}
class1=b.fromkeys(x,10)
print("fromkeys- ",class1)
class1["name"]="ankit"
class1["class"]="it"
class1["rollno"]=123
class1["address"]="ktg"
print(class1)
#update
a.update({4:"ankit",1:"abhi"})
print(a)
