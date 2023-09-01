import numpy as np
import random
import time
import black

# Tic-Tac-Toe - Casual Mode

# tic tac toe board
board = np.full((3, 3), ".", dtype=str)

game_over = False


def print_board(board):
    # prints a stylized board that indicates index/positions of the board
    print("\n")
    horizontal_labels = ["0", "1", "2"]
    vertical_labels = ["0", "1", "2"]
    print("  " + " ".join(horizontal_labels))
    for i, row in enumerate(board):
        print(vertical_labels[i] + " " + " ".join((str(element) for element in row)))


def validate_usr_symbol(usr_symbol):
    # validates user symbol input to ensure the input is either 'X' or 'O'
    if usr_symbol.upper() != "X" and usr_symbol.upper() != "O":
        raise ValueError(
            print("Invalid symbol choice. Please choose either 'X' or 'O'")
        )
    else:
        pass


def validate_incoord(urc, ucc):
    # validate a user's placement of symbol - checks if it is in the board and/or if there isn't another sybmol present
    if not (0 <= int(urc) <= 2 and 0 <= int(ucc) <= 2):
        raise ValueError(print("Coordinates are not within the 3x3 board."))
    elif not (board[int(urc), int(ucc)] == "."):
        raise ValueError(
            print(
                "There is a symbol in this position already. Choose a different position."
            )
        )
    else:
        pass

    # unfortunately I have not found a way to raise errors if the user types in a letter that is relatively scaleable
    # granted any person in their right mind would know to type in numbers, especially after seeing the board but I just wanted to make sure


def usr_turn(usr_symbol):
    print("\nYour turn:")
    while True:
        try:
            urc = input("\nWhich row?: ")  # urc means User Row Choice
            ucc = input("Which column?: ")  # ucc means User Column Choice
            validate_incoord(urc, ucc)  # validate coordinates
            board[int(urc), int(ucc)] = usr_symbol
            print_board(board)
            break
        except ValueError:
            continue


def cpu_turn(cpu_symbol, usr_symbol):
    print("\nOpponent's turn")

    while True:
        try:
            cpu_rc = random.choice([0, 1, 2])  # cpu_rc means CPU row choice
            cpu_cc = random.choice([0, 1, 2])  # cpu_rc means CPU column choice
            if board[cpu_rc, cpu_cc] == "." and not (
                board[cpu_rc, cpu_cc] == usr_symbol
            ):
                board[cpu_rc, cpu_cc] = cpu_symbol
                print("Opponent placed:", [cpu_rc, cpu_cc])
                print_board(board)
                break
        except ValueError:
            continue


def end_game(symbol):
    for i in range(3):
        # respectively check each row 'all(board[i][j] == symbol for j in range(3))' and check each column 'all(board[j][i] == symbol for j in range(3))' - whichever one fulfills the conditions (and only 1 of them need to be fulfilled)
        # return true
        if all(board[i][j] == symbol for j in range(3)) or all(
            board[j][i] == symbol for j in range(3)
        ):
            global game_over
            game_over = True
            print("\nGame over! " + symbol + " wins!")

    # Check diagonals for a win
    if all(board[i][i] == symbol for i in range(3)) or all(
        board[i][2 - i] == symbol for i in range(3)
    ):
        game_over = True
        print("\nGame over! " + symbol + " wins!")

    return game_over


def usr_go_first(usr_symbol, cpu_symbol):
    print("\nTake a look at the game board below:")
    print_board(board)

    while game_over == False:
        usr_turn(usr_symbol)
        end_game(usr_symbol)
        if game_over:
            continue
        time.sleep(1)
        cpu_turn(cpu_symbol, usr_symbol)
        end_game(cpu_symbol)
        if game_over:
            break


def cpu_go_first(usr_symbol, cpu_symbol):
    while game_over == False:
        cpu_turn(cpu_symbol, usr_symbol)
        end_game(cpu_symbol)
        if game_over:
            continue
        time.sleep(1)
        usr_turn(usr_symbol)
        end_game(usr_symbol)
        if game_over == True:
            break

    # the only issue is now is that if the cpu ever wins with the cpu_go first function, the user still has to make one more
    # guess because the end_game function needs to check the board state one last time


def play_game():
    # entrance statement for game
    print(
        "\nLet's play tic-tac-toe! Would you like to be 'X' or 'O'? X will have the first turn."
    )

    # while loop to allow user input and to validate the input - this will require a user input validation function (i want it to be multifaceted as well)
    while True:
        try:
            usr_symbol = input("X or O?: ")
            # - this will be the validation function I mentioned earlier
            validate_usr_symbol(usr_symbol)
            print("User:", usr_symbol.upper())
            break
        except ValueError:
            continue

    # then an if statement to indicate if the user will have the 1st or 2nd turn depending on which symbol they chose
    if usr_symbol.upper() == "X":
        cpu_symbol = "O"
        print("CPU: ", cpu_symbol)
        # - this will be the turn based loop function that allows the user to go first if they choose X as their symbol
        usr_go_first(usr_symbol, cpu_symbol)
    elif usr_symbol.upper() == "O":
        cpu_symbol = "X"
        print("CPU: ", cpu_symbol)
        # - this will be the turn based loop function that allows the cpu to go first if the user chooses O as their symbol
        cpu_go_first(usr_symbol, cpu_symbol)


play_game()

# So this is essentially 80% done I would say. I think the main things to fix right now are:
# ̶ 1̶.̶ t̶h̶e̶ t̶u̶r̶n̶ b̶a̶s̶e̶d̶ g̶a̶m̶e̶ l̶o̶o̶p̶ -̶ w̶h̶e̶n̶e̶v̶e̶r̶ t̶h̶e̶ u̶s̶e̶r̶ p̶l̶a̶y̶s̶ a̶s̶ '̶X̶'̶,̶ t̶h̶e̶ c̶p̶u̶ a̶l̶w̶a̶y̶s̶ e̶n̶d̶s̶ u̶p̶ n̶e̶e̶d̶i̶n̶g̶ t̶o̶ t̶a̶k̶e̶ a̶n̶o̶t̶h̶e̶r̶ t̶u̶r̶n̶ e̶v̶e̶n̶ t̶h̶o̶u̶g̶h̶ t̶h̶e̶ g̶a̶m̶e̶ i̶s̶ e̶s̶s̶e̶n̶t̶i̶a̶l̶l̶y̶ d̶o̶n̶e̶
#    - this is essentially working how I would like it to, so I would just need to find a way to cancel the cpu_turn() and probably even the usr_turn() function AS SOON as game_over = True
# 2. I would like to implement some heading so that each round of the game can be distinguished and easy to determine in the terminal. This will be the ultimate beautifying effect for the game
# 3. I could consider making the cpu_turn() function smarter, but I don't know how serious that may be. If I make it any smarter, is there a way to avoid falling down a m,n,k game theory rabbit hole 😬?
#    - yeah bruh tbh this is the most boring game of tic tac toe ever, like the randomize function for the cpu is laughably abysmal and guarantees a winning option 9 times out of ten
#    - one interesting thing to think about in regards to this is that I can either make the cpu better at position placement OR better at defense. I wonder which would be easier to improve? I could do both but then I think I'd end up with google's level of impossible in their respective version of tic tac toe (which was torturously too good at tic tac toe)

# with this being the case, I may shift to the other parts of the assesment just to get a jumpstart since I'm still stuck on this part. But before the, lets spend some time thinking deeply about how to treat issue #1 (this may require some archetectural redesign)
