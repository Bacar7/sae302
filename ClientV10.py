#Importation des bibliothèque 
import socket

#Déclaration de la fonction main
def main():
    host = socket.gethostname() 
    port = 12345
    #Définition de l'hôte et du port de connexion

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(client_socket.recv(1024).decode()) 
    #Affichage de la réception d'une donnée envoyée par le serveur
    
    nom_user = input("> Choisir un nom d'utilisateur :")
    client_socket.send(nom_user.encode())

    print(client_socket.recv(1024).decode()) 

    niveau_choisi = input("> ")
    client_socket.send(niveau_choisi.encode())
    #Variable permettant d'envoyer au serveur le niveau de difficulté choisi

    #Boucle while permettant de faire fonctionner le programme du joueur
    while True:
        message = client_socket.recv(1024).decode()
        print(message)
        #Réception des données envoyées par le serveur

        if "Fin de la partie" in message:
            break
        #Condition if permettant de vérifier que la partie continue

        if "Bravo" in message :
            message = client_socket.recv(1024).decode()
            print(message)
            break
        #Condition if permettant de vérifier si le joueur a gagné la partie

        if "Perdu" in message :
            message = client_socket.recv(1024).decode()
            print(message)
            break
        #Condition if permettant de vérifier si le joueur a perdu la partie

        lettre_proposee = input("> Proposez une lettre : ")
        client_socket.send(lettre_proposee.encode())
        #Variable permettant d'envoyer la lettre ou le mot choisi par le joueur 

    client_socket.close() #Ferme la connexion

if __name__ == "__main__":
    main()