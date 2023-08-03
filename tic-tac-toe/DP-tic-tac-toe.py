import numpy as np 
import random
import time

# Tic-Tac-Toe - casual mode

#tic tac toe board
board = np.full((3,3), '.', dtype=str)

game_over = False

def print_board(board): 
    #prints a stylized board that indicates index/positions of the board 
    print("\n")
    horizontal_labels = ['0', '1', '2']
    vertical_labels = ['0', '1', '2']
    print('  ' + ' '.join(horizontal_labels))
    for i, row in enumerate(board):
        print(vertical_labels[i] + ' ' + ' '.join((str(element) for element in row)))


def validate_usr_symbol(usr_symbol):
    #validates user symbol input to ensure the input is either 'X' or 'O'
    if usr_symbol.upper() != 'X' and usr_symbol.upper() != 'O':
        raise ValueError(print("Invalid symbol choice. Please choose either 'X' or 'O'"))
    else:
        pass

def validate_incoord(urc, ucc):
    #validate a user's placement of symbol - checks if it is in the board and/or if there isn't another sybmol present 
    if not(0 <= int(urc) <= 2 and 0 <= int(ucc) <= 2):
        raise ValueError(print("Coordinates are not within the 3x3 board."))
    elif not(board[int(urc), int(ucc)] == '.'):
        raise ValueError(print("There is a symbol in this position already. Choose a different position."))
    else:
        pass
    
    
    #unfortunately I have not found a way to raise errors if the user types in a letter that is relatively scaleable
    #granted any person in their right mind would know to type in numbers, especially after seeing the board but I just wanted to make sure 
        

def usr_turn(usr_symbol):
    print("\nYour turn:")
    while True:
        try:
            urc = input('\nWhich row?: ') # urc means User Row Choice
            ucc = input('Which column?: ') # ucc means User Column Choice
            validate_incoord(urc, ucc) #validate coordinates
            board[int(urc), int(ucc)] = usr_symbol
            print_board(board)
            break
        except ValueError:
            continue
    
def cpu_turn(cpu_symbol, usr_symbol):
    print("\nOpponent's turn")
    
    while True:
        try:
            cpu_rc = random.choice([0,1,2]) #cpu_rc means CPU row choice
            cpu_cc = random.choice([0,1,2]) #cpu_rc means CPU column choice
            if board[cpu_rc, cpu_cc] == '.' and not(board[cpu_rc, cpu_cc] == usr_symbol):
                board[cpu_rc, cpu_cc] = cpu_symbol
                print('Opponent placed:', [cpu_rc, cpu_cc])
                print_board(board)
                break
        except ValueError:
            continue 
      
        
def end_game(symbol): 
    for i in range(3):
        #respectively check each row 'all(board[i][j] == symbol for j in range(3))' and check each column 'all(board[j][i] == symbol for j in range(3))' - whichever one fulfills the conditions (and only 1 of them need to be fulfilled)
        #return true 
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            global game_over
            game_over = True
            print('Game over' + symbol + 'wins!')
        
    # Check diagonals for a win
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        game_over = True
        print('Game over ' + symbol + ' wins!')
        
    return game_over


def usr_go_first(usr_symbol, cpu_symbol):
    print('\nTake a look at the game board below:')
    print_board(board)
    
    while game_over == False:    
        usr_turn(usr_symbol)
        end_game(usr_symbol)
        time.sleep(1)
        cpu_turn(cpu_symbol, usr_symbol)
        end_game(cpu_symbol)
        if game_over == True:
            break
        

def cpu_go_first(usr_symbol, cpu_symbol):
    while game_over == False:
        cpu_turn(cpu_symbol, usr_symbol)
        end_game(cpu_symbol)
        time.sleep(1)
        usr_turn(usr_symbol)
        end_game(usr_symbol) 
        if game_over == True:
            break  
    
    #the only issue is now is that if the cpu ever wins with the cpu_go first function, the user still has to make one more 
    #guess because the end_game function needs to check the board state one last time 
 

def play_game():
    #entrance statement for game 
    print("\nLet's play tic-tac-toe! Would you like to be 'X' or 'O'? X will have the first turn.")
    
    #while loop to allow user input and to validate the input - this will require a user input validation function (i want it to be multifaceted as well)
    while True:
        try:
            usr_symbol = input('X or O?: ')
            validate_usr_symbol(usr_symbol) # - this will be the validation function I mentioned earlier
            print('User:', usr_symbol.upper())
            break
        except ValueError:
            continue
    

    #then an if statement to indicate if the user will have the 1st or 2nd turn depending on which symbol they chose
    if usr_symbol.upper() == 'X':
        cpu_symbol = 'O'
        print('CPU: ', cpu_symbol)
        usr_go_first(usr_symbol, cpu_symbol) #- this will be the turn based loop function that allows the user to go first if they choose X as their symbol
    elif usr_symbol.upper() == 'O':
        cpu_symbol = 'X'
        print('CPU: ', cpu_symbol)
        cpu_go_first(usr_symbol, cpu_symbol) # - this will be the turn based loop function that allows the cpu to go first if the user chooses O as their symbol 
    

play_game()

# So this is essentially 80% done I would say. I think the main things to fix right now are: 
# 1. the turn based game loop - whenever the user plays as 'X', the cpu always ends up needing to take another turn even though the game is essentially done
#    - this is essentially working how I would like it to, so I would just need to find a way to cancel the cpu_turn() and probably even the usr_turn() function AS SOON as game_over = True
# 2. I would like to implement some heading so that each round of the game can be distinguished and easy to determine in the terminal. This will be the ultimate beautifying effect for the game

# with this being the case, I may shift to the other parts of the assesment just to get a jumpstart since I'm still stuck on this part. But before the, lets spend some time thinking deeply about how to treat issue #1 (this may require some archetectural redesign)