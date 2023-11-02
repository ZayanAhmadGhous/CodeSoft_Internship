import random
def game(computer, player):
    if computer==player:
        return None
    elif computer =='stone':
        if player=='paper' or player=='Paper':
            return True
        elif player=='scissor' or player=='Scissor':
            return False
    elif computer=='paper':
        if player=='stone' or player=='Stone':
            return False
        elif player=='scissor' or player=='Scissor':
            return True
    elif computer=='scissor':
        if player=='paper' or player=='Paper':
            return False
        elif player=='stone' or player=='Stone':
            return True


print(" Welcome to Rock, Paper, Scissor Game")

randno=random.randint(1,3)

if randno==1:
    computer='stone'
elif randno==2:
    computer='paper'
else:
    computer='scissor'


        
print(" Your's Turn:\nStone\nPaper\nScissor\n ")
player=input(" Enter Stone Paper or Gun to play the game: ")
a=game( computer,player)


if player=="Stone" or player=="stone" or player=="Paper" or player=='paper' or player=='Scissor' or player=="scissor":
    
    print(f" Computer choose {computer}")
    print(f" You choose {player}")

    if a==None:
        print(" Your and your's Computer's choice is same")
    elif a:
        print(" Congratulations! You Won!!!")
    else:
        print(" Alas! You lose")
else:
    raise SyntaxWarning
