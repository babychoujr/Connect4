import connectfour
#Eric Chou
#10/29/2017
#connectfour_console.py
#ICS 32A

def printboard(game: 'GameState'): #prints out the Connect Four board
    for x in range(connectfour.BOARD_COLUMNS):
        print(x+1, end = ' ')
    print()
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            space = game.board[col][row]
            if space == 0:
                print('.', end = ' ')
            elif space == 1:
                print('R', end = ' ')
            elif space == 2:
                print('Y', end = ' ')
        print()

def winner_game(game):
    if (connectfour.winner(game) == 1):  # Checks the winner of the game
        print('Congratulations Player RED ')
        return True
    if (connectfour.winner(game) == 2):
        print('Congratulations Player YELLOW')
        return True
    if (connectfour.winner(game) == 0):
        pass

def play():
    game = connectfour.new_game()  # creates a new game
    print('NEW GAME : CONNECT 4')
    printboard(game)  # prints out the new game board
    done = False
    while not done:                #the game part of the game
        try:
            if game.turn == 1:
                print('The Current Player is RED')
            elif game.turn == 2:
                print('The Current Player is YELLOW')
            command = input('Please enter type of move and column number(e.x. Drop 5): ')
            movetype = command[0:4]
            movetype = movetype.strip()

            if ((movetype == 'Drop' or movetype == 'drop') and connectfour.winner(game) == 0 and command[4:5] == ' '): # Checks the move type and if there is a winner already or not
                column = command[5:]
                column = column.strip()
                column = int(column)

                game = connectfour.drop(game, column - 1)
                printboard(game)

            elif (movetype == 'Pop' or movetype == 'pop' and connectfour.winner(game) == 0 and command[3:4] == ' '): #Checks the move type and if there is a winner already or not
                column = command[4:]
                column = column.strip()
                column = int(column)

                game = connectfour.pop(game, column - 1)
                printboard(game)

            if(winner_game(game)== True):
                done = True
        except connectfour.InvalidMoveError:                                                                             #Throws an error if the Move made was incorrect
            print('InValid Move Please Try Again')
        except ValueError:
            print('Please type ur response following format(Drop 5 or Pop 5): ')



def main(): #main function
    play()




if __name__ == "__main__":
    main()