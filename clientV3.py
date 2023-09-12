import socket                   # Importation du module 'socket'

def client_game() :
    host = socket.gethostname()
    port = 5000                 # Port du serveur socket

    mySocket = socket.socket()                  # Instance
    mySocket.connect((host, port))                  # Connecte au serveur
    print("Connexion établie avec le serveur")

    mySocket.close()                    # Ferme la connexion

if __name__ == '__main__' :
    client_game()
