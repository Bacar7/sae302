import socket                   # Importation du module 'socket'

def client_program() :
    host = socket.gethostname()
    port = 5000                 # Port du serveur socket

    mySocket = socket.socket()                  # Instance
    mySocket.connect((host, port))                  # Connecte au serveur
    print("Connexion établie avec le serveur")
    
    message = input(" -> ")                 # Ajoute d'un entrée de clavier

    while message.lower().strip() != 'Aurevoir' :                   # Tant que le message est différent de "Aurevoir"
        mySocket.send(message.encode())                 # Envoie le message
        data = mySocket.recv(1024).decode()                 # Reçoit la réponse

        print('Reçu depuis le serveur : ' + data)                  # Affiche dans le terminal

        message = input(" -> ")                 # Réajoute de l'entrée de clavier

    mySocket.close()                    # Ferme la connexion

if __name__ == '__main__' :
    client_program()