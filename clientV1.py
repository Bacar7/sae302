import socket # Importation du module "socket"

host = 'localhost'                  # Définition de l'hôte et du port de connexion
port = 6000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                    # Fonction de socket

try :
    mySocket.connect((host, port))                 # Tentative de connexion
except socket.error :
    print("Connexion échouée avec le serveur")                 # Si erreur, connexion échouée sinon réussie
    exit()

print("Connexion établie avec le serveur")