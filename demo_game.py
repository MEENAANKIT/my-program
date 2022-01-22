import random
count=0
hotel_worth=200
jail_fine=150
treasure=200
hotel_rent=50
player1_money=1000
player2_money=1000
player1_step=0
player2_step=0
player1_hotel=[]
player2_hotel=[]
count=0
d=["E","E","H","T","E","E","J","E","E","H","E","E","T","E","E","E","E","J","E","H","E","E","T","E","E","E","E","J","E","E","E","E","H","T","E","J","E","E"]
def dice():
    for i in range(len(d)):
    #for m in range(1):
        player1=input(" player1 name")
        a=random.randrange(2,12)
        print(a)
        #i=a
        
        if d[i]=="T":
            print("you are won price is 200")
            player1_money=player1_money+treasure
        elif d[i]=="J":
            print("jail fine is 150")
            player1_money=player1_money-jail_fine
        elif d[i]=="H":
            print("you are owner this hotel")
            player1_money=player1_money-hotel_worth
            player1_hotel.append(d[i])
            d.remove(d[i])
        elif d[i] in player2_hotel:
            print("pay the rent: ")
            player1_money=player1_money-hotel_rent
            player2_money=player2_money+hotel_rent
        else:
            print("empty")
        #player2_step=player2_step+i
        player2=input("player2 name")
        y=random.randrange(1,13)
        print(y)
        #i=y
        if d[i]=="T":
            print("you are won price is 200")
            player2_money=player2_money+treasure
        elif d[i]=="J":
            print("jail fine is 150 ")
            player2_money=player2_money-jail_fine
        elif d[i]=="H":
            print("you are owner this hotel")
            player2_money=player2_money-hotel_worth
            player2_hotel.append(d[i])
            d.remove(d[i])
        elif d[i] in player1_hotel:
            print("pay the rent")
            player2_money=player2_money-hotel_rent
            player1_money=player1_money+hotel_rent
        else:
            print("empty")


        
        
    

            




            




