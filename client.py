import socket # Importation du module 'socket'

# Définition de l'hôte et du port pour établir la connexion
host = 'localhost'
port = 9000

mysSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Création de la socket

try :
    mysSocket.connect((host, port))                                     # Connexion avec le serveur
except socket.error :                                                   # Si la connexion n'est pas établie il renvoie un message d'erreur et sort du programmme
    print("Connexion échouée avec le serveur") 
    exit() 

print("Connexion établie avec le serveur")


