import socket # Importation du module 'socket'

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    mySocket = socket.socket()  # instantiate
    mySocket.connect((host, port))  # connect to the server
    print("Connexion établie avec le serveur")
    
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        mySocket.send(message.encode())  # send message
        data = mySocket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    mySocket.close()  # close the connection


if __name__ == '__main__':
    client_program()