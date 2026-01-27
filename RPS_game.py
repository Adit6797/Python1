# rock paper scessor game

import  random

computer =  random.choice([1,2,3])
you = input("Enter your choise as Rock=R/Paper=P/scissor=S :").upper()
if(you=="R" and you=="P" and you=="S"):
    youdict={"R":1,"P":2,"S":3}
    revdict={1:"Rock",2:"Paper",3:"scessor"}
    you = youdict[you]
    print(f"You choose {revdict[you]}")
    print(f"Computer choose {revdict[computer]}")

    if(computer==you):
        print("Match Draw !!!")
    else:
        if(computer==1 or you==2):
            print("You win !!")
        elif(computer==1 or you==3):
            print("you Lose!!")
        elif(computer==2 or you==3):
            print("You win !!")
        elif(computer==2 or you==1):
            print("you Lose!!")
        elif(computer==3 or you==1):
            print("You win !!")
        elif(computer==3 or you==2):
            print("you Lose!!")
else:
    print("Somthing went wrong!!")