import connectfour
#Eric Chou
#10/29/2017
#connectfour_console.py
#ICS 32A
#UCI ID: 95408627
# Project #2: Send Me On My Way
#console version of connectfour
def printboard(game: 'GameState'): #prints out the Connect Four board
    for x in range(connectfour.BOARD_COLUMNS):
        print(((x+1)%10), end = ' ')
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
    print()

def game_over(game):
    if (connectfour.winner(game) == 1):  # Checks the winner of the game
        print('Congratulations Player RED ')
        return True
    if (connectfour.winner(game) == 2):
        print('Congratulations Player YELLOW')
        return True
    if (connectfour.winner(game) == 0):
        pass

def get_movetype_column(command:str)-> (str, int):
    commands = command.split()
    if (len(commands)!= 2):  # illegal format
        return " ", 0
    movetype = commands[0]
    movetype = movetype.upper()
    movetype = movetype.strip()
    column=""
    if   (movetype == 'DROP' and command[4:5] == " "):
        column = command[5:]
    elif (movetype == 'POP'  and command[3:4] == " "):
        column = command[4:]
    else:
        return " ", 0
    column = column.strip()
    column = int(column)
    return movetype, column

def move(game: 'GameState', column: int, movetype: str)->'GameState':
    movetype = movetype.strip()
    movetype = movetype.upper()
    if movetype == "DROP":
        game = connectfour.drop(game, column - 1)
    elif movetype == "POP":
        game = connectfour.pop(game, column - 1)
    return game

def main(): #main function
    game = connectfour.new_game()  # creates a new game
    print('NEW GAME : CONNECT 4')
    printboard(game)  # prints out the new game board
    done = False
    while not done:                #the game part of the game
        try:
            if game.turn == 1:     # going to be user mode in network version
                print('The Current Player is RED')
            elif game.turn == 2:   # going to be AI mode in network version
                print('The Current Player is YELLOW')

            command = input('Please enter type of move and column (e.x. DROP 5 or POP 4): \n')
            movetype, column = get_movetype_column(command)
            if (movetype==" " and column==0): raise(connectfour.InvalidMoveError)
            game     = move(game, column, movetype)
            printboard(game)

            if(game_over(game)== True):
                done = True
        except connectfour.InvalidMoveError:                                                                             #Throws an error if the Move made was incorrect
            print('Invalid Move Please Try Again')
        except connectfour.GameOverError:
            print('This game is over already.')
        except ValueError:
            print('Please type ur response following format(DROP 5 or POP 5): ')

if __name__ == "__main__":
    main()