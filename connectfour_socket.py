import socket
#Eric Chou
#10/29/2017
#connectfour_socket.py
#ICS 32A
#UCI ID: 95408627
# Project #2: Send Me On My Way

def read_host() -> str: #reads the host
    while True:
        host = input('Host: ').strip()
        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host

def read_port() -> int: #reads the port
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def read_message() -> str: #reads message
    return input('Message: ')

def print_response(resp: str) -> None: #prints the response
    print('Response: ' + resp)


def connect(host: str, port: int) -> 'connection': #connect to server
    s = socket.socket()
    s.connect((host, port))
    s_input = s.makefile('r')
    s_output = s.makefile('w')
    return s, s_input, s_output

def close(con: 'connection') -> None: #close the connection to server
    s, s_input, s_output = con
    s_input.close()
    s_output.close()
    s.close()

def send_message(con: 'connection', m: str) -> None: #sends message
    s, s_input, s_output = con
    s_output.write(m + '\r\n')
    s_output.flush()

def receive_response(con: 'connection') -> None: #receives the response
    s, s_input, s_output = con
    return s_input.readline()[:-1]

def user_interface() -> None:
    host = read_host()
    port = read_port()
    print('Connecting to {} (port {})...'.format(host, port))
    con = connect(host, port)
    print('Connected!')
    while True:
        m = read_message()
        if m == '':
            break
        else:
            send_message(con, m)
            resp = receive_response(con)
            print_response(resp)
    print('Closing connection...')
    close(con)
    print('Closed!')

if __name__ == '__main__':
    user_interface()
