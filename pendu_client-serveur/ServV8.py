import socket
import threading 
import random

clients = 0
 
def choisir_niveau(niveau):
    mots_faciles = ["moto", "avion", "chat", "camion", "lapin", "chien"]
    mots_moyens = ["ordinateur", "programmation", "éléphant", "intelligence", "algorithme"]
    mots_difficiles = ["rhinopharyngitolaryngographologiquement", "cyclopentanoperhydrophénanthrène", "hippopotomonstrosesquippedaliophobie"]

    if niveau == "facile":
        return random.choice(mots_faciles)
    elif niveau == "moyen":
        return random.choice(mots_moyens)
    elif niveau == "difficile":
        return random.choice(mots_difficiles)

def jeu_pendu(mySocket):
    
    niveaux = ["facile", "moyen", "difficile"]
    mySocket.send("\nBienvenue au jeu du pendu ! Vous avez 3 niveaux de difficulté (facile, moyen, difficile): ".encode())
    niveau_choisi = mySocket.recv(1024).decode().lower()  
    
    while niveau_choisi not in niveaux:
        mySocket.send("Niveau invalide. Fermeture de la connexion.".encode())
        mySocket.close()
        return

    lettre_trouvée = "" 
    lettre_utilisée = [] 
    Mot = "" 
    b = True 
    c = True 
    n = True
    j = ""
    solution = choisir_niveau(niveau_choisi) 
    
    tentative = 7
    
    for i in solution :
        Mot = Mot + "_ "
    
    print(f"Le mot à trouver est : {solution}")
    print ("Mot à deviner :",Mot)
    mySocket.send(f"Mot à deviner : {Mot}\n".encode())
    
    while b : 
        
        while n :
            a = mySocket.recv(1024).decode() 
            print(f"lettre choisi : {a}")

            if len(lettre_utilisée) == 0 :  
                n = False

            if len(lettre_utilisée) != 0 : 
                for w in range(len(lettre_utilisée)) : 
                    if a == lettre_utilisée[w] : 
                        j = True
                        n = True 
                        break
                    else : 
                        j = False 
                        n = False 
            
            if j == True : 
                mySocket.send(f"La lettre {a} a déjà été utilisé.\nMot à deviner : {Mot}\n".encode())
                print("La lettre",a,"a déjà été utilisé.")

        d = len(a) 
        
        if d <= 1: 
            
            for l in solution : 
                if a == l : 
                    c = True 
                    break
                else :
                    c = False 
                    
            if c == True :
                lettre_trouvée = lettre_trouvée + " " + a 
                lettre_utilisée.append(a) 
                Mot = ""  
                for x in solution:
                    if x in lettre_trouvée : 
                        Mot += x + " " 
                    else:
                        Mot += "_ " 
                if "_" not in Mot:
                    mySocket.send("Bravo".encode())
                    mySocket.send(f"La lettre {a} est correct !\nLes lettres {lettre_trouvée} sont correct.\nIl vous reste {tentative} tentative.\nBravo vous avez trouvé le mot à deviner {solution} en {tentative} tentative !\n".encode())
                    print(f">>> Bravo vous avez trouvé le mot à deviner en {tentative} tentative ! <<<")
                    break
                else : 
                    mySocket.send(f"La lettre {a} est correct !\nLes lettres {lettre_trouvée} sont correct.\nIl vous reste {tentative} tentative.\nMot à deviner : {Mot}\n".encode())
                    print("La lettre",a,"est correct !")
                    print("Les lettres",lettre_trouvée,"sont correct.")
                    print("Il vous reste",tentative,"tentative.")

            else : 
                lettre_utilisée.append(a)
                tentative = tentative - 1 
                
                if tentative==0: 
                    b = False
                    mySocket.send("Perdu".encode())
                    mySocket.send(f"La lettre {a} est incorrect !\nVous n'avez plus de tentative, vous avez perdu.\nLe mot à deviner était, {solution} .\n==========Y=\n ||/       |  \n ||        0  \n ||       /|\ \n ||       / \  \n/||           \n==============\n".encode())
                    print("Vous n'avez plus de tentative, vous avez perdu.")
                    print("La lettre",a,"est incorrect !")
                    print("Le mot à deviner était",solution,".")
                    print(" ==========Y= ")
                if tentative ==1: 
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n ||/       |  \n ||        0  \n ||       /|\ \n ||       / \  \n/||           \n==============\nMot à deviner : {Mot}\n".encode())
                    print(" ||/       |  ")
                if tentative ==2: 
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n ||        0  \n ||       /|\ \n ||       / \  \n/||           \n==============\nMot à deviner : {Mot}\n".encode())
                    print(" ||        0  ")
                if tentative ==3:
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n ||       /|\ \n ||       / \  \n/||           \n==============\nMot à deviner : {Mot}\n".encode())
                    print(" ||       /|\ ")
                if tentative ==4: 
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n ||       / \  \n/||           \n==============\nMot à deviner : {Mot}\n".encode())
                    print(" ||       / \  ")
                if tentative ==5:              
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n/||           \n==============\nMot à deviner : {Mot}\n".encode())
                    print("/||           ")
                if tentative ==6: 
                    mySocket.send(f"La lettre {a} est incorrect !\nIl vous reste {tentative} tentative.\n==============\nMot à deviner : {Mot}\n".encode())
                    print("==============\n") 
        
        else : 
            if a == solution : 
                mySocket.send("Bravo".encode())
                print("Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !")
                mySocket.send(f"Bravo vous avez trouvé le mot à deviner en {tentative} tentative !\n".encode())
                break
            else : 
                tentative = tentative - 1
                print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")
                mySocket.send(f"Dommage ce n'est pas le bon mot. Il vous reste {tentative} tentatives.\nMot à deviner : {Mot}\n".encode())
        n = True 

def main():
    global clients  
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket()  
    server_socket.bind((host, port)) 
    server_socket.listen(2)  
    
    print(f"Le serveur écoute sur le port {port}...")

    while True:
        client_socket, addr = server_socket.accept()  

        if clients < 2: 
            clients += 1  
            
            client_pendu = threading.Thread(target=jeu_pendu, args=(client_socket,))
            
            client_pendu.start() 
        else:
            print("Nombre maximal de clients atteint. Refus de la connexion.")
            client_socket.close()  

if __name__ == "__main__":
    main()