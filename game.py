#snake water gun game :
#first we need random module :
#comparision between random and player :
print("     ~ WELCOME TO SNAKE WATER GUN GAME ~     ")
import random
dice =["snake","water","gun"]
c=0
cw=0
hw=0
cl=0
hl=0
draw=0
while c!=10:
    robot = random.choice(dice)
    print("------- ROUND",c+1,"-------")
    player = input("Enter your choice from s,w,g...\n ")
    if robot == "snake" and player.lower()== "s":
        print('Tie both 0 pointS to each')
        draw+=1
        c+=1
    elif robot == "snake" and player.lower() == "w":
        cw+=1
        print('you loose computer win\nyour point is',hw,'and computer point is',cw)
        c+=1
    elif robot == "snake" and player.lower() == "g":
        hw+=1
        print('you win computer loose\nyour point is',hw,'and computer point is',cw)
        c+=1
    elif robot == "water" and player.lower() == "s":
        hw+=1
        print('you win computer loose\nyour point is',hw,'and computer point is',cw)
        c+=1
    elif robot == "water" and player.lower() == "g":
        hw+=1
        print('you win computer loose\nyour point is',hw,'and computer point is',cw)
        c+=1
    elif robot == "water" and player.lower() == "w":
        draw+=1
        print('Tie both 0 point to each')
        c+=1
    elif robot == 'gun' and player.lower() == "g":
        draw+=1
        print('Tie both 0 point to each')
        c+=1
    elif robot == "gun" and player.lower() == 'w':
        cw+=1
        print('you loose computer win\nyour point is',hw,'and computer point is',cw)
        c+=1
    elif robot == 'gun' and player.lower() == 's':
        cw+=1
        print('you loose computer win\nyour point is',hw,'and computer point is',cw)
        c+=1
    else:
        print("wrong input")
    print(10-c,'rounds left')
else:
    if hw>cw:
        print('you won the game')
    elif hw<cw:
        print('you loose the game')
    else:
        print('game draw')
input('press enter to exit')

