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

def rps():
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

        if user_input=="help":
            clear()
            rps_instructions()
        elif user_input=="exit":
            clear()
            break
        elif user_input=="rock" or user_input=="paper" or user_input=="scissors":

            print("Computer making a move....")
            time.sleep(2)

            computer_move=random.choice(game_map)
            print("Computer chooses ",computer_move)
            if user_input==computer_move:
                print("Tie")
            elif (user_input=="rock") and (computer_move=="paper") or (user_input=="paper") and (computer_move=="scissor") or (user_input=="scissor") and (computer_move=="rock"):
                print("computer wins the match")
            else:
                print(f"{name} wins the match")
        else:
            clear()
            print("Wrong input")
            rps_instructions()
            continue
            

        print("**********")
        time.sleep(2)

        with open('game_info.csv','a',newline='') as f:
            dict_write=DictWriter(f,fieldnames=['Player_move','Computer_move','Player_name','Match_result'])
        
            if os.stat('game_info.csv').st_size==0:
                dict_write.writeheader()
            dict_write.writerow({
                'Player_move':user_input,
                'Computer_move':computer_move,
                'Player_name':name,
            
            })
        

if __name__ == '__main__':

	# The mapping between moves and numbers
	game_map = {0:"rock", 1:"paper", 2:"scissors"}
	name = input("Enter your name: ")

	# The GAME LOOP
	while True:

		# The Game Menu
		print("***********")
		print("Let's Play!!!")
		print("Enter 1 to play Rock-Paper-Scissors")
		print("Enter 2 to quit")
		print("***********")

		# Try block to handle the player choice 
		try:
			choice = int(input("Enter your choice = "))
		except ValueError:
			clear()
			print("Wrong Choice")	
			continue

		
		if choice == 1:
			rps()

			
		elif choice == 2:
			break

		
		else:
			clear()
			print("Wrong choice. Read instructions carefully.")
			
			
