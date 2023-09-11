import socket # Importation du module 'socket'

    client_socket = socket.socket()
    client_socket.connect((host, port))

    mySocket = socket.socket()  # instantiate
    mySocket.connect((host, port))  # connect to the server
    print("Connexion établie avec le serveur")
    
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        mySocket.send(message.encode())  # send message
        data = mySocket.recv(1024).decode()  # receive response

        message = input(" -> ")

    client_socket.close()

    mySocket.close()  # close the connection

if __name__ == '__main__':
    client_program()
