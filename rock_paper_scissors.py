import random
import os
import time
from csv import DictWriter

# to clear the screen
def clear():
    os.system("clear")

#instructions for Rock,Paper and Scissor 
def rps_instructions():

    print("***********")
    print("Instructions for Rock-Paper-Scissors : ")
    print("***********")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("***********")

def match_info():
    print("***********")
    print("Number of match played :",numberofmatch)
    print("Number of match won by computer :",computer_win)
    print(f"Number of match won by {name} :",user_win)
    print("Number of match were Tie :",numberofmatch_Tie)
    time.sleep(5)




def rps():
    global numberofmatch
    global user_win
    global computer_win
    global numberofmatch_Tie
    while True:
        
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instruction")
        print("Enter \"rock\",\"paper\",\"scissors\" to play")
        print("Enter \"exit\" to quit")
        print("---------------------------------------")
        print("***************")
        
        user_input=input("Enter your move :").lower()
        computer_move=random.choice(game_map)

        if user_input=="help":
            clear()
            rps_instructions()
        elif user_input=="exit":
            clear()
            break
        elif user_input=="rock" or user_input=="paper" or user_input=="scissors":
            numberofmatch+=1

            print("Computer making a move....")
            time.sleep(2)
            print("Computer chooses ",computer_move)

            if user_input==computer_move:
                numberofmatch_Tie+=1
                print("Tie")
            elif (user_input=="rock") and (computer_move=="paper") or (user_input=="paper") and (computer_move=="scissor") or (user_input=="scissor") and (computer_move=="rock"):
                computer_win+=1
                print("computer wins the match")
            else:
                user_win+=1
                print(f"{name} wins the match")
        else:
            clear()
            print("Wrong input")
            rps_instructions()
            continue
            
        print("**********")
        time.sleep(2)

        with open('Move_info.csv','a',newline='') as f:
            dict_write=DictWriter(f,fieldnames=['Player_move','Computer_move'])
        
            if os.stat('Move_info.csv').st_size==0:
                dict_write.writeheader()
            dict_write.writerow({
                'Player_move':user_input,
                'Computer_move':computer_move 
            })
        

if __name__ == '__main__':

	# The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
    name = input("Enter your name: ")
    numberofmatch=0
    user_win=0
    computer_win=0
    numberofmatch_Tie=0

	# The GAME LOOP
    while True:
		#The Game Menu
        print("***********")
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print("Enter 3 to see the Game info")
        print("***********")

		# Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")	
            continue

		# Play the traditional version of the game
        if choice == 1:
            rps()

	# Quit the GAME LOOP 	
        elif choice == 2:
            break
	# to see the match info
        elif choice==3:
            match_info()
            clear()

	# Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")                
