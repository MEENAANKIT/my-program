a={"a":"name","b":"age","c":{"a":"class","b":"address"}}
#print(a["a"])
#print(a["c"]["b"])
#a["c"]["c"]="mobileno"
#a["a"]="ankit"
#print(a)
b={i:a[i] for i in a}
print(b)