import random
player1_money=1000
player2_money=1000
hotel_worth=200
hotel_rent=50
jail_fine=150
treasure_value=200
player1_steap=0
player2_steap=0
cell_position={1:"E",2:"E",3:"H",4:"T",5:"E",6:"E",7:"J",8:"E",9:"E",10:"H",11:"E",12:"E",13:"T",14:"E",15:"E",16:"E",17:"E",18:"J",19:"E",20:"H",21:"E",22:"E",23:"T",24:"E",25:"E",26:"E",27:"E",28:"J",29:"E",30:"E",31:"E",32:"E",33:"H",34:"T",35:"E",36:"J",37:"E",38:"E"}
hotel='H'
jail='J'
treasure='T'
empty='E'
#dice=[4,4,4,6,7,8,5,11,10,12]
hotel=[]
for i in cell_position:
    for x in range(1,11):
        a=random.randint(2,12)
        i=a
        player1=input("first player -: ")
        if player1=="1":
            for j in range(1):
                player1_steap=player1_steap+i
                if cell_position[i]=='J':
                    #player1_steap=player1_steap+i
                    player1_money=player1_money-jail_fine
                    print("jail",player1_money,"dice -",a)
                    #del cell_position[i]
                elif cell_position[i]=='T':
                    #player1_steap=player1_steap+i
                    #print(player1_steap)
                    player1_money=player1_money+treasure_value
                    print("treasure",player1_money,"dice -",a)
                    #del cell_position[i]
                elif cell_position[i]=='H':
                    #player1_steap=player1_steap+i
                    #print(player1_steap)
                    player1_money=player1_money-hotel_worth
                    print("hotel owner",player1_money,"dice -",a)
                    #del cell_position[i]
                    if cell_position[i] not in hotel:
                        hotel.append(cell_position[i])
                        player1_money=player1_money+hotel_rent
                        print("hotelrent +50",player1_money)
                        #del cell_position[i]
                    else:
                        player1_money=player1_money-hotel_rent
                        print("hotelrentpay -50",player1_money)
                        #del cell_position[i]
                else:
                    #player1_steap=player1_steap+i
                   # print(player1_steap)
                    print("empty",player1_money,"dice -",a)
                    #del cell_position[i] 
        if player1_steap==10:
            print("chance complete")
        else:
            print("chance is uncomplete")
        b=random.randint(2,12)
        i=b
        player2=input("second player -: ")
        if player2=="2":
            for k in range(1):

                player2_steap=player2_steap+i
                if cell_position[i]=='J':
                    #player2_steap=player2_steap+i
                    #print(player2_steap)
                    player2_money=player2_money-jail_fine
                    print("jail",player2_money,"dice -",b)
                    #del cell_position[i]
                elif cell_position[i]=='T':
                    #player2_steap=player2_steap+i
                    #print(player2_steap)
                    player2_money=player2_money+treasure_value
                    print("treasure",player2_money,"dice -",b)
                    #del cell_position[i]
                elif cell_position[i]=='H':
                    #player2_steap=player2_steap+i
                    #print(player2_steap)
                    player2_money=player2_money-hotel_worth
                    print("hotel owner",player1_money,"dice -",b)
                    #del cell_position[i]
                    if cell_position[i] not in hotel:
                        hotel.append(cell_position[i])
                        player2_money=player2_money+hotel_rent
                        print("hatelrent +50",player2_money)
                        #del cell_position[i]
                    else:
                        player2_money=player2_money-hotel_rent
                        print("hotelrentpay -50",player2_money)
                        #del cell_position[i]
                else:
                    #player2_steap=player2_steap+i
                    #print(player2_steap)
                    print("empty",player2_money,"dice -",b)
                    #del cell_position[i]
        if player2_steap==10:
            print("chance complete")
        else:
            print("chance uncomplete")

print("first player total money -:",player1_money)
print("second player total monay -:",player2_money)
print()
if player1_money>player2_money:
    print("first player is winner -:",player1_money)
elif player1_money==player2_money:
    print("match is tai",player1_money,"=",player2_money)
else:
    print("second player is winner -:",player2_money)