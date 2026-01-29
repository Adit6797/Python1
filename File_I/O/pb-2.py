# this causes some error
import random

def game():
        score=random.randint(1,999)
        print("your are playing the game!!!")
        print(f"your score is {score}")
        with open("C:\\Users\\ag065\\OneDrive\\Dokumen\\python\File_I\\O\\highscore.txt") as f:
            highscore=f.read()
            if(highscore!=""):
                  highscore=int(highscore)
            else:
                  highscore=0

        if(score>highscore):
               with open("C:\\Users\\ag065\\OneDrive\\Dokumen\\python\File_I\\O\\highscore.txt","w") as f:
                     f.write(str(score))
                     print(f"New highscore is {score}")
        else:
               print(f"highscore is {highscore} you couldn't beat it")              
        return score
game()
