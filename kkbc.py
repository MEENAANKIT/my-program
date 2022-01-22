print("-:KON BANEGA KARODPATI ME APKA SWAGAT HAI:-")
list1=["(1) what is capital of india ?","(2) name of google ceo ?","(3) how many states of india ?"]
list2=[["(A) surat","(B) bhopal","(C) delhi","(D) mumbai"],["(A)ratan tata","(B) bill gets","(C) naredra modi","(D) sundar pichai"],["(A) 30","(B) 31","(C) 28","(D) 29"]]
list3=["50-50","question change","expert call"]
list4=[["A.surat","C.delhi"],["A.ratan tata","D.sundar pichai"],["A.30","B.31"]]
price=[10000,20000,30000]
for i in range(len(list1)):
    print(list1[i])
    for j in range(len(list2[i])):
        print(list2[i][j])
    user1=input("enter your option-/-life line-: ")
    
    if user1=="(C) delhi" or user1=="(D) sundar pichai" or user1=="(B) 31":
        print("right answer you win" ,price[i])
    elif user1=="life line":
        n=len(list3)
        for k in range(n+2):
            user=input("choose youre life line, 50-50/question change/expert call-: ")
            if user=="50-50":
                print(user)
                fifty_50=[]
                for t in range(len(list2[i])):
                    if list2[i][t]=="(C) delhi" or list2[i][t]=="(B) bhopal" or list2[i][t]=="(A) ratan tata" or list2[i][t]=="(D) sundar pichai" or list2[i][t]=="(A)30" or list2[i][t]=="(B) 31":        
                        fifty_50.append(list2[i][t])
                print(fifty_50)
                user1=input("enter option")
                if user1=="(C) delhi" or user1=="(D) sundar pichai" or user1=="(B) 31":
                    print("right answer you win",price[i])
                else:
                    print("wrong answer")
                    break
                break
            elif user=="question change":
                print(list1[i+1])
                print(list2[i+1])
                break
            elif user=="expert call":
                expert=input("expert answer-: ")
                if expert==list2[0][2]: 
                    print(expert,"right answer you win-: ",price[i])
                elif expert==list2[1][3]:
                    print(expert,"right answer you win-: ",price[i])
                elif expert==list2[2][1]:
                    print(expert,"right answer you win-: ",price[i])
                else:
                    print(expert,"wrong answer you win-: ")
                break
    else:
        print("wrong answer")
        
    