import socket                   # Importation du module 'socket'

def server_program() :                   # Définition du programme serveur (fonction)
    host = socket.gethostname()                 # Obtient le nom d'hôte
    port = 5000                 # Initialise le numéro de port au-dessus de 1024

    maSocket = socket.socket()                  # Obtient l'instance
    maSocket.bind((host, port))                 # Lie ensemble l'adresse de l'hôte et son port 

    maSocket.listen(5)                  # Configure le nombre de clients possible à l'écoute simultanément
    conn, address = maSocket.accept()                   # Accepte la nouvelle connexion
    print("Connexion de : " + str(address))
    while True :    
        data = conn.recv(1024).decode()                 # Reçoit les données en direct. Il n'accepte pas les paquets de données plus grand que 1024 bits.
        if not data :
            break                   # Si les données ne sont pas reçus, on stoppe
        print("Depuis un utilisateur connecté : " + str(data))
        data = input(' -> ')
        conn.send(data.encode())                    # Envoie les données au(x) client(s)

    conn.close()                    # Ferme la connexion

if __name__ == '__main__' :
    server_program()                    # Exécute la fonction