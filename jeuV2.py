solution = "chat" #variable contenant le mot à deviner
tentative = 10 #variable contenant le nombre de tentative disponible
lettre_trouvée = "" #variable permetant de répertorier les lettres correctes trouvées
lettre_incorrect = "" #variable permetant de répertorier les lettres incorrectes
Mot = "" #variable permettant d'afficher au fur et à mesure le mot à deviner
b = True #les variables b et c sont des variables utilisées pour vérifier une condition
c = True  

for i in solution :
    Mot = Mot + "_ "
#boucle permettant d'afficher des "_" en fonction du nombre de lettre à trouver

while b : 
    print ("Mot à deviner :",Mot)
#boucle permettant d'afficher des "_" en fonction du nombre de lettre à trouver

    if "_" not in Mot:
        print(">>> Bravo vous avez trouvé le mot à deviner en",tentative, "tentative ! <<<")
        break #break permet de sortir directement du programme 
    #condition if permettant de vérifier si la variable Mot ne contient plus de "_". 
    # Si Mot n'a plus de "_", affichage victoire
    
    a = str(input("Choisir une lettre ou un mot : ")) #affichage d'un champ permettant à l'utilisateur de choisir une lettre
    print ("Vous avez choisi :", a) #Affichage de la lettre choisi
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
            lettre_trouvée = lettre_trouvée + " " + a #ajout de la lettre choisi dans la variable lettre_trouvée
            print("Les lettres",lettre_trouvée,"sont correct.")
            print("Il vous reste",tentative,"tentative.")
            Mot = ""
            for x in solution: #boucle for permettant de parcourir toutes les lettres dans solution
                if x in lettre_trouvée : #conditions if permettant de vérifier si les lettres dans la variable lettre_trouvée correspondent aux lettres dans solution
                    Mot += x + " " #remplace les "_" par la lettre trouvée
                else:
                    Mot += "_ " #ne remplace rien

        else : #condition else permettant d'afficher que la lettre est incorrecte si la lettre choisi ne se trouve pas dans la variable solution
            print("La lettre",a,"est incorrect !")
            lettre_incorrect = lettre_incorrect + " " + a #ajout de la lettre choisi dans la variable lettre_incorrecte 
            tentative = tentative - 1 #on retire une tentative si la lettre est incorrecte
            print("Les lettres",lettre_incorrect,"sont incorrect.")
            print("Il vous reste",tentative,"tentative.")

        if tentative==0: #condition if permettant d'afficher que l'utilisateur n'a plus de tentative
            print("Vous n'avez plus de tentative, vous avez perdu.")
            b = False 
    
    else : #condition else permettant de vérifier si la variable a est un mot
        if a == solution : #condition if permettant de vérifier si le mot choisi est le mot à deviner
            print(">>> Bravo vous avez trouvé le mot à deviner en",tentative, "tentative ! <<<")
            b = False
        else : #condition else permettant de vérifier si le mot choisi est incorrecte
            tentative = tentative - 1 #on retire une tentative si le mot est incorrecte
            print("Dommage ce n'est pas le bon mot. Il vous reste",tentative, "tentative.")