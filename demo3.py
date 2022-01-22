import random
#a=random.randrange(2,12)
player1=input()
player1_money=1000
player2_money=1000
hotel_worth=200
hotel_rent=50
jail_fine=150
treasure_value=200
player1_steap=0
player2_steap=0
empty="E"
hotel="H"
treasure="T"
jail="J"
d={1:"E",2:"E",3:"H",4:"T",5:"E",6:"E",7:"J",8:"E",9:"E",10:"H",11:"E",12:"E",13:"T",14:"E",15:"E",16:"E",17:"E",18:"J",19:"E",20:"H",21:"E",22:"E",23:"T",24:"E",25:"E",26:"E",27:"E",28:"J",29:"E",30:"E",31:"E",32:"E",33:"H",34:"T",35:"E",36:"J",37:"E",38:"E"}
for i in range(1,10):
    a=random.randrange(2,12)
    for x in d:
        if player1=="A":
            player1_steap=player1_steap+x
            print("first player","dice",a)
            if d[x]=="J":
                print("you are in jail fine 150",player1_money)
                player1_money=player1_money-jail_fine
            elif d[x]=="T":
                print("you win 200 rupice add",player1_money)
                player1_money=player1_money+treasure_value
            elif d[x]=="H":
                hotelworth=input("enter youre choice hotel buy or not")
                if hotelworth=="buy":
                    player1_money=player1_money-hotel_worth
                    print("hotel is youre",player1_money)
                else:
                    print("this is not my hotel",player1_money)
            else:
                print("empty")
    for x in d:
        player2=input()
        if player2=="b":
            player2_steap=player2_steap+x
            print("second player","dice",a)
            if d[x]==6 or d[x]==17 or d[x]==26 or d[x]==34:
                print("you are in a jail fine 150",player2_money)
                player2_money=player2_money-jail_fine
            elif d[x]==3 or d[x]==12 or d[x]==22 or d[x]==32:
                print("you win 200 rupice add",player2_money)
                player2_money=player2_money+treasure_value
            elif d[x]==2 or d[x]==9 or d[x]==19 or d[x]==31:
                hotelworth=input("enter youre choice hotel buy or not")
                if hotelworth=="buy":
                    player2_money=player2_money-hotel_worth
                    print("hotel is youre",player2_money)
                else:
                    print("this is not my hotel",player2_money)  
            else:
                print("empty")
print("first player", player1_money)
print("second player",player2_money)




