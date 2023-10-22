import socket                   # Importation du module 'socket'

host = socket.gethostname()
port = 5000                 # Port du serveur socket

mySocket = socket.socket()                  # Instance
mySocket.connect((host, port))                  # Connecte au serveur
print("Connexion établie avec le serveur")
                # Ajoute d'un entrée de clavier
message = str(input("Choisir une lettre ou un mot : ")) 

while message.lower().strip() != 'Aurevoir' :                   # Tant que le message est différent de "Aurevoir"
    mySocket.send(message.encode())                 # Envoie le message
    data = mySocket.recv(1024).decode()                 # Reçoit la réponse

    print('Reçu depuis le serveur : ' + data)                  # Affiche dans le terminal

    message = str(input("Choisir une lettre ou un mot : "))                 # Réajoute de l'entrée de clavier

mySocket.close()                    # Ferme la connexion
