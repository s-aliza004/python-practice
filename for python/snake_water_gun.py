import random
def gamewin(comp,you):
    #if two values are declare a tie!
    if comp==you:
        return None
    #check all possiblities when computer chose s
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    #check all possiblities when computer chose w
        
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    #check all possiblities when computer chose g
    
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


print("Comp Turn:Snake(s) Water(w) or Gun(g)?")            
randNo = random.randint(1,3)
if randNo == 1:
    comp='s'        
elif randNo == 2:
    comp='w'
elif randNo==3:
    comp='g'

you= input("Player 1 turn: Snake(s) water(w) or gun(g?")
a=gamewin(comp,you)
print(f"Computer chose {comp}")
print(f"you chose {you}")
if a== None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")