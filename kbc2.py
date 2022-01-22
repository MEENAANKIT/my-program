list1=["A.what is capital of india","B.how many letter in alphabet","C.who is prime minister of india"]
list2=[["A.surat","B.bhopal","C.delhi","D.mumbai"],["A.55","B.33","C.26","D.16"],["A.kamal nath","B.narendra modi","C.ratan tata","D.sivraj sing"]]
list3=[["A.surat","C.delhi"],["A.55","C.26"],["A.kamal nath","B.narendra modi"]]
list4=["100000","200000","300000"]
life_line=["5050","question change"]
i=0
count=0

while i<len(list1):
    print(list1[i])
    j=0
    while j<len(list2[i]):
        print(list2[i][j])
        j=j+1
    print("agar ap life line lena chate ho to/5050/question change")
    user1=input("enter your life line")
     
    if user1=="5050":
        print(list3[i])
        

    elif user1=="question change":
        print(list1[i+1])
        print(list2[i+1])

        
    else:
        print("no life line")
    
    user2=input("enter your option")
    if user2=="C.delhi" or user2=="C.26" or user2=="B.narendra modi":
            print("right answer you win",list4[i])
    else:
        print("wrong answer")
        break
    i=i+1
