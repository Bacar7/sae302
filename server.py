import socket

host = 'localhost'
port = 9000


#serveur (mySocket)
#
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
	#on lance le serveur sur le mot bind avec les deux paramettre
        mySocket.bind((host, port))

#utilisation du modurle erreur socket.error
except socket.error :
        print("le serveur non fonctionnel")
        exit()

#nombre de personne max possible
mySocket.listen(5)
print("le serveur est mis en route")

continuer = true

#boucle pour maintenir le serveur allumer
while continuer :

	#verifie si une personne est connecter, la fonction retourne le port et
        #l'adresse du client
        connexion, adresse = mySocket.accept()

        #affichage lors d'une connexion
        print("une personne est connecter avec l'ip {0} et le port {1}".format(adresse[0], adresse[1]))


