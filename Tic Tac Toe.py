"""
Developed By: Ashish Kore

Requirements:
Python version-> 3 or later
Python Packages or Modules->    1. IPython

"""

#importing necessary packages and modules
from IPython.display import clear_output 

def print_board(l):
#to print the board in current condition

    print("     |     |\n {} | {} | {} \n ____|_____|_____".format(l[0],l[1],l[2]))
    print("     |     |\n {} | {} | {} \n ____|_____|_____".format(l[3],l[4],l[5]))
    print("     |     |\n {} | {} | {} \n     |     |     ".format(l[6],l[7],l[8]))

def winner(win_mark):
#to print the winner of the game
    
    #checks if player1 is the winner
    if win_mark==" "+play1+" ":
        print("Player 1 is the winner")
        
    #checks if player2 is the winner
    elif win_mark==" "+play2+" ":
        print("Player 2 is the winner")

def win_check():
# to chech if any player has won

    #checks if 1st row has same markers
    if l[0]==l[1]==l[2]:
        winner(l[0])        
        return True
    #checks if 2nd row has same markers
    elif l[3]==l[4]==l[5]:
        winner(l[3])
        return True
    #checks if 3rd row has same markers
    elif l[6]==l[7]==l[8]:
        winner(l[6])
        return True
    #checks if 1st column has same markers
    elif l[0]==l[3]==l[6]:
        winner(l[0])
        return True
    #checks if 2nd column has same markers
    elif l[1]==l[4]==l[7]:
        winner(l[1])
        return True
    #checks if 3rd column has same markers
    elif l[2]==l[5]==l[8]:
        winner(l[2])
        return True
    #checks if main diagonal has same markers
    elif l[0]==l[4]==l[ 8]:
        winner(l[0])
        return True
    #checks if antidiagonal has same markers
    elif l[2]==l[4]==l[6]:
        winner(l[2])
        return True
    #checks if it's a tie
    elif (l.count(" "+play1+" ")+l.count(" "+play2+" "))==len(l):
        print("Whoops!! It's a Tie ")
        return True
    #checks if no row, no column, no diagonal have same markers
    else:
        return False
    

def place_marker(pos,mar):
# to place marker on the board     
    l[pos-1]=" "+mar+" "

def take_input(m1,m2):
# to take position at wich player want to place the marker

    #takes player1's choice to place the marker
    if win_check()!=True and m1==True:
        p1_pos=int(input("Player 1 enter the postion to place your marker:"))
        # checks if the position is already taken or not
        if l[p1_pos-1] != " "+play1+" " and l[p1_pos-1] != " "+play2+" ":
            place_marker(p1_pos,play1)
            
        #if the position is already consumed then it asks for the position again to the same user.
        else:
            m1=True
            m2=False
            print("Place Already used!!")
            take_input(m1,m2)
    print_board(l)
            
    #takes player2's choice to place the marker
    if win_check()!=True and m2==True:
        p2_pos=int(input("Player 2 enter the postion to place your marker:"))
        # checks if the position is already taken or not
        if l[p2_pos-1] != " "+play1+" " and l[p2_pos-1] != " "+play2+" ":
            place_marker(p2_pos,play2)
        #if the position is already consumed then it asks for the position again to the same user.
        else:
            m1=False
            m2=True
            print("Place Already used!!")
            take_input(m1,m2)


#initializes the index of the board
l=[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]

#prints the empty board with position numbers
print_board(l)

print("Welcome to the Game!!\nNote: You can press any of the alphabet keys or special symbol keys, and select it as your marker.")

#takes input of the marker symbol of both the users
play1=input("Player 1 enter your marker:")
play2=input("Player 2 enter your marker:")
while True:
    if play1==play2:
        print("Marker already used!!")
        play2=input("Player 2 enter your marker:")
    else:
        break
    

# Continously takes position input and checks wheather a player has won
while win_check()!=True:
    take_input(True,True)
    
    #clears the previous output
    clear_output() 
    
    print_board(l)
