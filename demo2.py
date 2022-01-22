import random


player1_money=1000
player2_money=1000
hotel_worth=200
hotel_rent=50
jail_fine=150
treasure_value=200
player1_step=0
player2_step=0
z=['E','E','J','H','E','T','E','E','H','E','E','T','H','E','E']
player1_hotel=[]
player2_hotel=[]

for i in range(1,11):
    
    
    for x in range(len(z)):
        for j in range(1):
            a=random.randrange(1,13)
            
            print(a)
            player1=input("first player: ")
            if player1=="A":
                player1_step=player1_step+a
                if z[x]=="J":
                    print("jail fine 150 ")
                    player1_money=player1_money-jail_fine
                elif z[x]=="T":
                    print("you are won 200 rs")
                    player1_money=player1_money+treasure_value
                elif z[x]=='H':
                    v=input("you puechase the hotel: yes or no")
                    if v=="yes":
                        print("you are owner")
                        player1_money=player1_money-hotel_worth
                        player1_hotel.append(z[x])
                    else:
                        print("hotel is not your")
                elif z[x] in player2_hotel:
                        print("pay the rent")
                        player1_money=player1_money-hotel_rent
                    
                else:
                    print("empty")
        
        for g in range(1):
            
            d=random.randrange(1,13)
            print(d)


            player2=input("second player")
            if player2=='B':
                player2_step=player2_step+d
                if z[x]=="J":
                    print("jail fine 150 rs")
                    player2_money=player2_money-jail_fine
                elif z[x]=="T":
                    print("you are won 200 rs")
                    player1_money=player1_money+treasure_value
                elif z[x]=="H":
                    v=input("you are purchase the hotel: yes or no")
                    if v=="yes":
                        print ("you are owner this hotel")
                        player2_money=player2_money-hotel_worth
                        player2_hotel.append(z[x])
                    else:
                        print("not buying the hotel")
                elif z[x] in player1_hotel:
                    print("pay the rent")
                    player2_money=player2_money-hotel_rent
                    
                else:
                    print("empty")


            



        
        







        
            



    
    