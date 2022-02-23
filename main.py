#paper scissors rock
import random
score = 0
print("(¯`·._.·(¯`·._.·(¯`·._.· Welcome to paper scissors rock ·._.·´¯)·._.·´¯)·._.·´¯)")
print("                           type help for all commands")
movelist =["paper","scissors","rock", "help","score"]
playermove = input("What is your move? ")
randommove = random.choice(movelist)

while playermove != "exit":

    if playermove not in movelist:
        print("Wait What???")
        playermove = input("what is your move? ")
        continue
    if playermove == randommove:
        print("draw.... No computer wins")
    elif playermove == "paper" and randommove == "rock":
        print("player wins, computer chose " + randommove)
        score = score - 1 
    elif playermove == "paper" and randommove == "scissors":
        print("computer wins , you chose paper")
    elif playermove == "scissors" and randommove == "rock":
        print("computer wins, you chose scissors ")
    elif playermove == "rock" and randommove == "scissors":
        print("computer wins, you chose rock")
        score = score - 1
    elif playermove == "help":
        print(""" exit - Exit program
                  Score - prints scoreboard""")
    if playermove == "score":
        print("your score is: ")
        print(score)
    
    if playermove == "What do i do here":
        print("Welp This is Scissors paper rock")
        
    
     
          
    playermove = input("what is your move? ")




