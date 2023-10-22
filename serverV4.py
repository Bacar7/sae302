#Importation des bibliothèque 
import socket
import threading 
import random

#Variable contenant le nombre de client
clients = 0
#variable contenant les utilisateurs
utilisateurs = []

#Déclaration de la fonction "choisir_niveau"
def choisir_niveau(niveau):
    faciles = ["moto", "avion", "chat", "camion", "lapin", "chien"]
    moyens = ["ordinateur", "programmation", "éléphant", "intelligence", "algorithme"]
    difficiles = ["rhinopharyngitolaryngographologiquement", "cyclopentanoperhydrophénanthrène", "hippopotomonstrosesquippedaliophobie"]
 
    if niveau == "facile":
        return random.choice(faciles)
    elif niveau == "moyen":
        return random.choice(moyens)
    elif niveau == "difficile":
        return random.choice(difficiles)
#Fonction permettant de générer un mot aléatoire parmi les niveaux de difficultés

#Déclaration de la fonction "jeu_pendu"
def jeu_pendu(mySocket):
    
    niveaux = ["facile", "moyen", "difficile"]
    mySocket.send("\n> Bienvenue au jeu du pendu !".encode())
    
    while True:
        nom_user = mySocket.recv(1024).decode().lower()
        # Reçoit les données du socket, les décode, puis convertit tout en minuscules.
        #lower() normalise les noms d'utilisateur ce qui pert par exmple que les noms "BaCaR", 
        #"Bacar" et "BACAR" soient traités de la même manière, ce qui garanti de ne pas avoir le meme nom
        if nom_user in utilisateurs:
           mySocket.send("\nNom déjà utilisé. Veuillez en choisir un autre.".encode())
           # Si le nom d'utilisateur est déjà dans la liste, on envoi le message.
        else:
           utilisateurs.append(nom_user)
           mySocket.send("Nom libre".encode())
           # Sinon, ajout du nom dans la liste utilisateurs et envoie le message.
           break
            
    mySocket.send("\n> Vous avez 3 niveaux de difficulté (facile, moyen, difficile):".encode())
    niveau_choisi = mySocket.recv(1024).decode().lower()
    #Variables qui annoncent aux joueurs le jeu
    
    while niveau_choisi not in niveaux:
        mySocket.send("> Niveau invalide. Fermeture de la connexion.".encode())
        mySocket.close()
        return
    #Boucle while permettant couper la connexion si le niveau de difficulté choisi ne correspond pas au niveau proposé

    lettre_trouvée = "" 
    lettre_utilisée = [] 
    Mot = "" 
    b = True 
    c = True 
    n = True
    j = ""
    solution = choisir_niveau(niveau_choisi) 
    tentative = 7
    #Variables utilisées pour le jeu
    
    for i in solution :
        Mot = Mot + "_ "
    #Boucle for permettant de cacher les lettres du mot à trouver 
    
    print(f"\n> {nom_user} doit trouver le mot : {solution}")
    mySocket.send(f"> Mot à deviner : {Mot}\n".encode())
    
    #Boucle while permettant de faire fonctionner le jeu
    while b : 
        
        #Boucle while permettant de vérifier la donnée envoyée du client 
        while n :
            a = mySocket.recv(1024).decode() 
            print(f"\n> {nom_user} a choisi la lettre {a}")

            if len(lettre_utilisée) == 0 :  
                n = False
            #Condition if permettant de vérifier si le tableau "lettre_utilisée" est vide

            #Condition if permettant de vérifier si le joueur a utilisé 2 fois la même lettre
            if len(lettre_utilisée) != 0 : 
                for w in range(len(lettre_utilisée)) : #Boucle for permettant de parcourir le tableau "lettre_utilisée"
                    if a == lettre_utilisée[w] : 
                        j = True
                        n = True 
                        break
                    else : 
                        j = False 
                        n = False 
                    #Condition if permettant de vérifier si la lettre choisi se trouve dans "lettre_utilisée"
            
            if j == True : 
                mySocket.send(f"> La lettre {a} a déjà été utilisé.\n> Mot à deviner : {Mot}\n".encode())
            #Condition if annonçant au joueur qu'il a utilisé 2 fois la même lettre

        d = len(a) 
        #Variable permettant de connaître la taille de la donnée envoyée par le joueur
        
        if d <= 1: 
            
        #Condition if permettant de gérer les lettres 
            
            for l in solution : 
                if a == l : 
                    c = True 
                    break
                else :
                    c = False 
            #Boucle for permettant vérifier si la lettre choisi se trouve dans le mot à deviner

            #Condition if permettant d'avertir le joueur que la lettre choisi est correcte      
            if c == True :
                lettre_trouvée = lettre_trouvée + " " + a #Ajout de la lettre correcte dans le tableau "lettre_trouvée"
                lettre_utilisée.append(a) #Ajout de la lettre choisi dans le tableau "lettre_utilisée"
                
                Mot = ""  
                for x in solution:
                    if x in lettre_trouvée : 
                        Mot += x + " " 
                    else:
                        Mot += "_ " 
                #Boucle for permettant de remplacer les lettres cachées par les lettres trouvées
                
                if "_" not in Mot:
                    mySocket.send("Bravo".encode())
                    mySocket.send(f"> La lettre {a} est correcte !\n> Les lettres {lettre_trouvée} sont correcte.\n> Il vous reste {tentative} tentative.\n> Bravo vous avez trouvé le mot à deviner {solution} en {tentative} tentative !\n".encode())
                    break
                else : 
                    mySocket.send(f"> La lettre {a} est correcte !\n> Les lettres {lettre_trouvée} sont correcte.\n> Il vous reste {tentative} tentative.\n> Mot à deviner : {Mot}\n".encode())
                #Condition if permettant de vérifier si le mot cachées est deviné

            #Condition else permettant d'avertir le joueur que la lettre choisi est incorrecte
            else : 
                lettre_utilisée.append(a) #Ajout de la lettre choisi dans le tableau "lettre_utilisée"
                tentative = tentative - 1 #Retire une tentative 
                
                #Condition if permettant d'avertir le joueur sur le nombre de tentative qu'il lui reste 
                if tentative==0: 
                    b = False
                    mySocket.send("Perdu".encode())
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Vous n'avez plus de tentative, vous avez perdu.\n> Le mot à deviner était, {solution} .\n> ==========Y=\n  ||/       |  \n  ||        0  \n  ||       /|\ \n  ||       / \  \n /||           \n ==============\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n  ==========Y=\n  ||/       |  \n  ||        0  \n  ||       /|\ \n  ||       / \  \n /||           \n ============== \n \n> {nom_user} a perdu\n__________________\n\n")
                if tentative ==1: 
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> ||/       |  \n  ||        0  \n  ||       /|\ \n  ||       / \ \n /||           \n ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n  ||/       |  \n  ||        0  \n  ||       /|\ \n  ||       / \ \n /||           \n ==============\n__________________\n\n")
                if tentative ==2: 
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> ||        0  \n  ||       /|\ \n  ||       / \ \n /||           \n ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n  ||        0  \n  ||       /|\ \n  ||       / \ \n /||           \n ==============\n__________________\n\n")
                if tentative ==3:
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> ||       /|\ \n  ||       / \ \n /||           \n ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n  ||       /|\ \n  ||       / \ \n /||           \n ==============\n__________________\n\n")
                if tentative ==4: 
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> ||       / \ \n /||           \n ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n  ||       / \ \n /||           \n ==============\n__________________\n\n")
                if tentative ==5:              
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> /||           \n ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n /||           \n ==============\n__________________\n\n")
                if tentative ==6: 
                    mySocket.send(f"> La lettre {a} est incorrecte !\n> Il vous reste {tentative} tentative.\n> ==============\n> Mot à deviner : {Mot}\n".encode())
                    print(f"__________________\n\n> Pendu de {nom_user} :\n\n ==============\n__________________\n\n")
               
        #Condition else permettant de gérer les mots
        else : 
            if a == solution : 
                mySocket.send("Bravo".encode())
                mySocket.send(f"> Bravo vous avez trouvé le mot à deviner en {tentative} tentative !\n".encode())
                break
            else : 
                tentative = tentative - 1
                mySocket.send(f"> Dommage ce n'est pas le bon mot. Il vous reste {tentative} tentatives.\n> Mot à deviner : {Mot}\n".encode())
            #Condition if permettant de vérifier si le mot est correct
        
        n = True 
        #Variable n permettant de faire fonctionner la boucle while n


#Déclaration de la fonction main
def main():
    global clients  #Utilise une variable globale pour suivre le nombre de clients connectés
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket()  #Créer un socket pour le serveur
    server_socket.bind((host, port)) #Attache l'adresse de l'hôte et le port au socket
    server_socket.listen(2)  #Limite à 2 clients simultanés
    
    #"f" indique à Python d'évaluer les expressions à l'intérieur des accolades {} et de les remplacer par leurs valeurs respectives
    print(f"> Le serveur écoute sur le port {port}...")
    
    while True:
        client_socket, addr = server_socket.accept() #Accepte une nouvelle connexion cliente
        if clients < 2: #Vérifie s'il y a de la place pour un nouveau client
            clients += 1  #Incrémente le nombre de clients connectés

            #threads: permet au programme d'accomplir plusieurs tâches en même temps,
            #on crée un nouvel objet de type thread avec la classe Thread du module threading.
            #target spécifie la fonction que le thread exécutera. 
            #args spécifie les arguments à passer à la fonction (jeu_pendu)
            client_pendu = threading.Thread(target=jeu_pendu, args=(client_socket,))
            #On crée un nouveau thread (client_pendu) qui exécutera la fonction jeu_pendu 
            #avec le socket spécifique du client en tant qu'argument.
            
            client_pendu.start() 
            #On démarre le thread, la fonction jeu_pendu 
            #commence à s'exécuter de manière indépendante dans ce thread. 
            #cela permet au serveur de continuer à accepter d'autres connexions pendant 
            #que chaque client est géré.
            
        else:
            print(f"> Nombre maximal de clients (2) atteint. Refus de la connexion.")
            client_socket.close() #Ferme la connexion du client si le nombre maximal est atteint

if __name__ == "__main__":
    main()
