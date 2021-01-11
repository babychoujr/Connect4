import socket
import connectfour
import connectfour_console
import connectfour_socket
#Eric Chou
#10/29/2017
#connectfour_network.py
#ICS 32A
#UCI ID: 95408627
# Project #2: Send Me On My Way
#network version of connect4

def read_name():  #reads whatever the user enters for username
    n = input("Enter your username: \n")
    n = n.strip()
    return n

def run_game(con: 'connection')->None:
    game = connectfour.new_game()  # creates a new game
    print('NEW GAME : CONNECT 4')
    connectfour_console.printboard(game)  # prints out the new game board
    done = False
    while not done:  # the game part of the game
        try:
            if game.turn == 1:  # going to be user mode in network version
                print('The Current Player is RED')
                m = connectfour_socket.receive_response(con)
                print("Server RED:", m)
                if (m.upper()=="READY"):
                    send = False
                    while not send:
                        command = input('Please enter type of move and column (e.x. DROP 5 or POP 4): \n')
                        movetype, column = connectfour_console.get_movetype_column(command)

                        if (movetype != " " and column !=0):
                            command_to_server = movetype + " " + str(column)
                            connectfour_socket.send_message(con, command_to_server)
                            print("Client: ", command_to_server)
                            send = True

                        else:
                            print("Client(Wrong Input): ", command)


                    ok = connectfour_socket.receive_response(con)
                    print("Server: ", ok)
                    if (ok.upper() != 'INVALID'):
                        game = connectfour_console.move(game, column, movetype)
                        connectfour_console.printboard(game)
                        if ok.upper() == "WINNER_RED":
                            print("Server: ", "WINNER_RED")
                else:
                    raise("Error")

            elif game.turn == 2:  # going to be AI mode in network version
                print('The Current Player is YELLOW')
                print("Wait for server...")
                command = connectfour_socket.receive_response(con)
                command = command.upper()
                print("Server: ", command)
                movetype, column = connectfour_console.get_movetype_column(command)
                game = connectfour_console.move(game, column, movetype)
                connectfour_console.printboard(game)

            if (connectfour_console.game_over(game) == True):
                done = True
        except connectfour.InvalidMoveError:  # Throws an error if the Move made was incorrect
            print('Invalid Move Please Try Again')
        except connectfour.GameOverError:
            print('This game is over already.')
        except ValueError:
            print('Please type ur response following format(DROP 5 or POP 5): ')
        except:
            print('Error Occurs')

def main() -> None:
    # connection -> may need login information here
    host = connectfour_socket.read_host()
    port = connectfour_socket.read_port()
    name = read_name()
    print('Connecting to {} (port {})...'.format(host, port))
    con = connectfour_socket.connect(host, port)
    print('Connected!')

    print('Client-Server Communication Starts...')
    hello_message = "I32CFSP_HELLO "+name  #send the message + username to the server
    connectfour_socket.send_message(con, hello_message)
    m = connectfour_socket.receive_response(con)
    print("Server:", m)
    connectfour_socket.send_message(con, "AI_GAME")

    run_game(con)  #runs the game

    # closing up the connection
    print('Closing connection...')
    connectfour_socket.close(con)
    print('Closed!')

if __name__ == '__main__':
    main()
