import socket # Importation du module 'socket'

def client_program():
    host = socket.gethostname()  # car les deux codes s'exécutent sur le même PC
    port = 5000  # numéro de port du serveur socket

    mySocket = socket.socket()  # instancier
    mySocket.connect((host, port))  # se connecter au serveur
    print("Connexion établie avec le serveur")
    
    message = input(" -> ")  # prendre des notes

    while message.lower().strip() != 'bye':
        mySocket.send(message.encode())  # envoyer le message
        data = mySocket.recv(1024).decode()  # recevoir une réponse

        print('Received from server: ' + data)  # afficher dans le terminal

        message = input(" -> ")  # prenez à nouveau votre contribution

    mySocket.close()  # fermer la connexion

if __name__ == '__main__':
    client_program()
