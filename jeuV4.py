solution = "chat" #variable contenant le mot à deviner
tentative = 10 #variable contenant le nombre de tentative disponible
lettre_utilisé = [] #variable permetant de répertorier les lettres utilisées
Mot = "" #variable permettant d'afficher au fur et à mesure le mot à deviner
b = True #les variables b, c, n et j sont des variables utilisées pour vérifier une condition
c = True 
n = True
j = ""

for i in solution :
    Mot = Mot + "_ "
#boucle permettant d'afficher des "_" en fonction du nombre de lettre à trouver

while b : #Début du jeu avec la boucle while tant que b est vrai
    print ("Mot à deviner :",Mot) #Afficher la variable Mot
    
    while n : #Boucle permettant de vérifier si l'utilisateur n'utilise pas plusieurs fois la même lettre
        a = str(input("Choisir une lettre ou un mot : ")) #affichage d'un champ permettant à l'utilisateur de choisir une lettre
        print ("Vous avez choisi :", a) #Affichage de la lettre choisi

        if len(lettre_utilisé) == 0 : #conditions if permettant de vérifier si la variable lettre_utilisé est vide
            n = False 
        #si elle est vide, on sort de la boucle "while n"

        if len(lettre_utilisé) != 0 : #conditions if permettant de vérifier si la variable lettre_utilisé n'est pas vide
            for w in range(len(lettre_utilisé)) : #boucle for permettant de parcourir toutes les lettres que contient la variable lettre_utilisée
                if a == lettre_utilisé[w] : #conditions if permettant de vérifier si la lettre choisi a déjà été utilisé
                    j = True
                    n = True 
                    break
                else : 
                    j = False 
                    n = False 

        if j == True : #condition if permettant d'avertir l'utilisateur qu'il a déjà utilisé cettre lettre
            print("La lettre",a,"a déjà été utilisé.")

    d = len(a) #variable d contenant la longueur de la variable a
     
    if d <= 1: #condition if permettant de vérifier si la variable a est une lettre
        
        for l in solution : #boucle for permettant de parcourir les lettres dans solution
            if a == l : #condition if permettant de vérifier si la lettre choisi correspond à une lettre dans le mot à deviner
                c = True 
                break
            else :
                c = False 
                
        if c == True : #condition if permettant d'afficher que la lettre est correcte si la lettre choisi se trouve dans la variable solution
            print("La lettre",a,"est correct !")
            lettre_utilisé.append(a) #ajout de la lettre choisi dans le tableau lettre_utilisé
            print("Il vous reste",tentative,"tentative.")

        else : #condition else permettant d'afficher que la lettre est incorrecte si la lettre choisi ne se trouve pas dans la variable solution
            print("La lettre",a,"est incorrect !")
            lettre_utilisé.append(a) #ajout de la lettre choisi dans le tableau lettre_utilisé
            tentative = tentative - 1 #on retire une tentative si la lettre est incorrecte 
            print("Il vous reste",tentative,"tentative.")
        
        if tentative == 0 : #condition if permettant d'afficher que l'utilisateur n'a plus de tentative
            print("Vous n'avez plus de tentative, vous avez perdu.")
            b = False 
    
    else : #condition else permettant de vérifier si la variable a est un mot
        if a == solution : #condition if permettant de vérifier si le mot choisi est le mot à deviner
            print("Bravo vous avez trouvé le mot à deviner en",tentative, "tentative !")
            b = False
        else : #condition else permettant de vérifier si le mot choisi est incorrecte
            tentative = tentative - 1 #on retire une tentative si le mot est incorrecte 
            print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")
    n = True #variable n remit a True pour pouvoir effecture vérifier si l'utilisateur n'utilise pas une lettre déjà utilisée