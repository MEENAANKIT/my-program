i=4
k=1
n=9
str1=""
while n>=4:
    b=n
    while b<9:
        str1+=" "
        b=b+1
    j=n
    while j>=k:
        str1+="*"
        j=j-1
    k=k+1
    str1+="\n"
    n=n-1
k=3
i=1

while i<=4:
    b=3
    while b>=i:
        str1+=" "
        b=b-1
    j=1
    while j<=k:
        str1+="*"
        j=j+1
    str1+="\n"
    i=i+1
    k=k+2
print(str1)
    


    



