import connectfour
#Eric Chou
#10/29/2017
#connectfour_similar.py
#ICS 32A
#UCI ID: 95408627
# Project #2: Send Me On My Way
#this module contains the functions that are in both of the user interfaces of connectfour_network.py and connectfour_console.py

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