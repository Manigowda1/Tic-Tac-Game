from IPython.display import clear_output
import random

#1 Displays board

def display_board(board):
    clear_output()
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print(board[1]+ '|' + board[2]+ '|' + board[3])


# board = [' ',' ','X',' ',' ','X',' ',' ','X']

# display_board(board)

# 2Players input ,chooses players marker
def player_inp():
    marker = ''
    while marker!= 'X' and marker!= 'O':
        marker = input("PLayer1 :Please choose your marker here (X/O) ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# player1_marker,player2_marker = player_inp()
#
# print(player2_marker)

#3 places marker into given position
def place_marker(board,marker,position):
    board[position] = marker


# place_marker(board,'M',6)
# display_board(board)

#4 checks weather any 3 matches either in rows or columns or daigonally
def win_check(board,mark):
    #check
    #Rows
    return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or
            (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (
                    board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)
            )

# print(win_check(board,'X'))

#5 this gives who to start first
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#6 checks any empty positions
def space_check(board,position):
    return board[position]==' '

#7 checks if board is full
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

#8 Allows player to
def player_check(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position : (1 -9) "))
    return position

#9 replay
def replay():
    choice = input("PLay again? Enter Y/N  ")
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False
    else:
        print("Enter valid choice")

# Actual flow starts here

print("Welcome to the TIC- TAC Game")

print("Game instructions : Two players (PLayer1 & player2) player1 can choose his/her marker (X/O) to mark on board.")
print("Players can match their mark on row/column/diagonally to win ")

#1 while loop to keep running the game

while True:
    # Play the game
    # Set everything 1. board,2.Who is first,3.choose markers X,O
    board = [' '] * 10
    player1_marker, player2_marker = player_inp()
    turn = choose_first()
    print(turn + " Will go first ************")

    play_game = input("Ready to play game? Y/N : ")
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # Game play
    while game_on:
        if turn == 'Player 1':
            # show board
            display_board(board)
            # choose a position
            position = player_check(board)


            # place marker on that position

            place_marker(board,player1_marker,position)

            # check if they won
            if win_check(board,player1_marker):
                display_board(board)
                print("******************PLayer 1 has WON!*********************")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game Tie !")
                    game_on = False
                else:
                    turn = 'Player 2'
            #check for tie
            # if no tie and no win , next player turn
        else:
            display_board(board)
            # choose a position
            position = player_check(board)

            # place marker on that position

            place_marker(board, player2_marker, position)

            # check if they won
            if win_check(board, player2_marker):
                display_board(board)
                print("****************PLayer 2 has WON!********************")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game Tie !")
                    game_on = False
                else:
                    turn = 'Player 1'
    # PLayer One turn
    # Player two turn

    if not replay():
        break











# break based on replay condition





