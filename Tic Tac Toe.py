def set_mark():
    #to assign a matker to each player
    play1=input("Player 1 enter your marker either X or O:")
    play2=input("Player 2 enter your marker either X or O:")
    #if player1=="X":
     #   player2="O"
    #else:
     #   player2="X"


from IPython.display import clear_output 
def print_board(l):
 #to print the board in current condition
    clear_output()    
    print("     |     |\n {} | {} | {} \n ____|_____|_____".format(l[0],l[1],l[2]))
    print("     |     |\n {} | {} | {} \n ____|_____|_____".format(l[3],l[4],l[5]))
    print("     |     |\n {} | {} | {} \n     |     |     ".format(l[6],l[7],l[8]))

def winner(win_mark):
#     print(win_mark,play1,play2)
    print("Player {} is the winner".format(win_mark))

#     if win_mark==play1:
#         print("Player 1 is the winner")
#     elif win_mark==play2:
#         print("Player 2 is the winner")              

def win_check():
# to chech if any player has won
    if l[0]==l[1]==l[2]:
        
        winner(l[0])        
        return True
    elif l[3]==l[4]==l[5]:
        winner(l[3])
        return True
    elif l[6]==l[7]==l[8]:
        winner(l[6])
        return True
    elif l[0]==l[3]==l[6]:
        winner(l[0])
        return True
    elif l[1]==l[4]==l[7]:
        winner(l[1])
        return True
    elif l[2]==l[5]==l[8]:
        winner(l[2])
        return True
    elif l[0]==l[4]==l[ 8]:
        winner(l[0])
        return True
    elif l[2]==l[4]==l[6]:
        winner(l[2])
        return True

    else:
        return False
    

def place_marker(pos,mar):
    # to place marker on the board     
    l[pos-1]=" "+mar+" "

def take_input():
# to take position at wich player want to place the marker
    if win_check()!=True:
        p1_pos=int(input("Player 1 enter the postion to place your marker"))
        mark=""
        place_marker(p1_pos,play1)
        print_board(l)
    if win_check()!=True:
        p2_pos=int(input("Player 2 enter the postion to place your marker"))
        place_marker(p2_pos,play2)
        print_board(l)

a,b,c,d,e,f,g,h,i=" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "
l=[a,b,c,d,e,f,g,h,i]
print_board(l)
print("Welcome to the Game!!")
play1=input("Player 1 enter your marker either X or O:")
play2=input("Player 2 enter your marker either X or O:")
    

while win_check()!=True:
    take_input()
    

