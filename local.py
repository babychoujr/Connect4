from socket import *
from connectfour_console import *

# step 1 make a connection
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 15000))
s.listen(5)
c, a = s.accept()
print(c)
print(a)
#
hello = c.recv(1024)
hello = hello.decode('utf8')
print("Client: ", hello)
hello = hello.split()
welcome = "WELCOME " + hello[1] + "\r\n"
c.send(bytes(welcome, 'utf8'))
ai = c.recv(1024)
print(ai.decode('utf8'))
c.send(bytes("READY\r\n", 'utf8'))

# entering playing mode
done = False
while not done:
    m = c.recv(1024)
    m = m.decode('utf8')
    print("Client: ", m)
    movetype, column = get_movetype_column(m)

    if m.upper() == "WINNER_RED" or m.upper() == "WINNER_YELLOW":  # winner condition
        done = True
    elif (movetype.upper() != "DROP" and movetype.upper() != "POP") or (column < 1 or column > 7):  # invalid format
        invalid = "INVALID\r\n"
        c.send(bytes(invalid, "utf8"))
        print("Server: ", invalid)
        ready = "READY\r\n"
        c.send(bytes(ready, 'utf8'))
        print("Server: ", ready)
    else:  # valid format
        ok = "OKAY\r\n"
        c.send(bytes(ok, "utf8"))
        print("Server: ", ok)
        command = input("Enter Server's move: \n")
        command = command + "\r\n"
        c.send(bytes(command, "utf8"))
        print("Server: ", command)
        ready = "READY\r\n"
        c.send(bytes(ready, 'utf8'))
        print("Server: ", ready)

c.close()
s.close()
