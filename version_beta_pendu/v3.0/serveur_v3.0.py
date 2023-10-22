import socket                   # Importation du module "socket"
from pendu/jeu_pendu_v7.0 import jeu_pendu 

host = 'localhost'                  # Définition de l'hôte et du port de connexion
port = 6000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                    # Fonction de socket

try :
    mySocket.bind((host, port))                 # Tentative de connexion
except socket.error :
    print("Erreur : Le serveur ne s'est pas lancé !")                 # Si erreur, connexion échouée sinon réussie
    exit()

mySocket.listen(5)
print("Le serveur est mis en route...")

while True :                   # Tant que la fonction est vraie
    connexion, adresse = mySocket.accept()                  # Le serveur établit la connexion et reste connecter
    print("Une personne s'est connectée avec l'adresse IP {0} et sur le port {1}".format(adresse[0], adresse[1]))                    # Affiche un log de connexions clientes
    game = jeu_pendu()
    connexion.send(game)

