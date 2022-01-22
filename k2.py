n="ABCDEF"
i=0
l=len(n)
str1=""
t=1
p=0
while i<=l-1:
    k=p
    while k<i:
        str1+=str(n[k])
        k=k+1  
    str1+="\n"
    j=t
    while j<=i+1:
        str1+=str(j)
        j=j+1
 
    str1+="\n"
    i=i+2
    p=p+2
    
print(str1)





    
        






     