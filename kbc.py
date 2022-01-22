a=[["how many continents are there?"], # pehla question
["what is the capital of india?"], # second question
["ng mei kon sa course padhaya jata hai1?"]] # third question
#b=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhji"],["software engineering","counseling","tourism","agriculture"]]
# soultion key

n=len(a)
for i in range(3):
    print(a[i])
    b=[["1:four","2:nine","3:seven","4:eight"],["chandigarh","bhopal","chennai","delhji"],["software engineering","counseling","tourism","agriculture"]]
    for j in range(4):
        for k in range(len(b[j])):
            for l in range(len(b[j][k])):
                d=str(input("enter option-: "))
                if d==b[j][k]:
                    print("right answer")
            #elif d=="1":
                #print("rong answer")
            #elif d=="2":
                #print("rong answer")
            #elif d=="4":
                #print("rong answer")
                else:
                    print("wrong answer")
                print([b[j][k]])
#
#d=str(input("enter answ



