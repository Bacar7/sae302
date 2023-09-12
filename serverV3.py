import socket                   # Importation du module 'socket'

def server_game() :                   # Définition du jeu du pendu du serveur (fonction)
    host = socket.gethostname()                 # Obtient le nom d'hôte
    port = 5000                 # Initialise le numéro de port au-dessus de 1024

    maSocket = socket.socket()                  # Obtient l'instance
    maSocket.bind((host, port))                 # Lie ensemble l'adresse de l'hôte et son port 

    maSocket.listen(2)                  # Configure le nombre de clients possible à l'écoute simultanément
    conn, address = maSocket.accept()                   # Accepte la nouvelle connexion
    print("Connexion de : " + str(address))
    
    conn.close()                    # Ferme la connexion

if __name__ == '__main__' :
    server_game()                    # Exécute la fonction
