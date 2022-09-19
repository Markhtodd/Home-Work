
import glob
import numbers
import random
from turtle import position

#Mark Todd Tic-Tac-Toe CES
# introduce game
print ("Welcome to Mark's online Tic Tac Toe! Would you like to play?")


board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

playerUp = 'x'
winner = None
gameGoing = True

# make board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
print_board(board)

#board_keys = []

#for key in board:
    #board_keys.append(key)

def game():
    # take user move
    def user_input(board):
        inp = int(input('Please enter a number from 1-9: '))
        if inp >= 1 and inp <= 9 and board[inp-1] == '-':
            board[inp-1] = playerUp
        else:
            print('Sorry, that is not available!')
 
        
    # check on win
    def columns(board):
        global winner
        if board[0] == board[1] == board[2] and board[1] != '-':
            winner = board[0]
            return True
        elif  board[3] == board[4] == board[5] and board[3] != '-':
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != '-':
            winner = board[6]
            return True

    def rows(board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != '-':
            winner = board[0]
            return True
        elif  board[1] == board[4] == board[7] and board[1] != '-':
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != '-':
            winner = board[2]
            return True

    def diag(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != '-':
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != '-':
            winner = board[2]
            return True
            

    def tie(board):
        global gameGoing
        if '-' not in board:
            print_board
            print('The game it a tie! :/')
            gameGoing = False

    def check_win():
        global gameGoing
        if diag(board) or columns(board) or rows(board):
            print (f"This rounds winner of Mark's Tic Tac Toe is {winner}")
            print ('Thank you for playing!')
            gameGoing = False
            
                
        # change player
    def change_player():
        global playerUp
        if playerUp == 'x':
            playerUp = 'o'
        else:
            playerUp = 'x'

    # computer
    def comp(board):
        while playerUp == 'o':
            position = random.randint(0, 8)
            if board[position] == '-':
                board[position] = 'o'
                change_player()

    # check on win or tie again


    while gameGoing:
        print_board(board)
        user_input(board)
        check_win()
        tie(board)
        change_player()
        comp(board)
        check_win()
        tie(board)

   # try_again = input('Do you want to play another round? (y/n)')
    #if try_again == 'y' or try_again == 'Y':
        #for key in board_keys:

            #board[key] = " "

        #game()


if __name__ == "__main__":
    game()