#snake water gun game :
#first we need random module :
#comparision between random and player :
print("     ~ WELCOME TO SNAKE WATER GUN GAME ~     ")
import random
dice =["snake","water","gun"]
c=0
won=0
lose=0
draw=0
while c!=10:
    robot = random.choice(dice)
    player = input("enter your choice from snake,water,gun...\n ")
    if robot == "snake" and player == "snake":
        draw+=1
        c+=1
    elif robot == "snake" and player == "water":
        lose+=1
        c+=1
    elif robot == "snake" and player == "gun":
        won+=1
        c+=1
    elif robot == "water" and player == "snake":
        won+=1
        c+=1
    elif robot == "water" and player == "gun":
        won+=1
        c+=1
    elif robot == "water" and player == "water":
        draw+=1
        c+=1
    elif robot == 'gun' and player == "gun":
        draw+=1
        c+=1
    elif robot == "gun" and player == 'water':
        lose+=1
        c+=1
    elif robot == 'gun' and player == 'snake':
        lose+=1
        c+=1
    else:
        print("wrong input")
else:
    print(won,'Times you win the game')
    print(lose,'Times you lose the game')
    print(draw,'Times game drawn')
input('press enter to exit')

