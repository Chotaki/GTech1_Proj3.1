from random import randint

tableau = ["pierre", "feuille", "ciseau"]

def pierreFeuilleCiseau():

    continuer = True

    while continuer:
        chiffreAleatoire = randint(0,2)
        jeuJoueur = None
        # Boucle vérifiant si l'action du joueur et conforme au format demandé
        while jeuJoueur == None:
            action = input("Entrez un chiffre entre 0 et 2 : ")
            try:
                # Vérifier si l'action du joueur est bien un chiffre
                action = int(action)
                # Vérifier si l'action du joueur se situe entre 0 et 2
                if 0 <= action <= 2:
                    jeuJoueur = action
                else:
                    print("Erreur, valeur incorrecte")
            except(ValueError):
                print("Erreur, valeur incorrecte")

        # Afficher les actions de l'ordinateur et du joueur
        print(tableau[jeuJoueur], tableau[chiffreAleatoire])

        # Vérifier si il y a une égalité
        if chiffreAleatoire == jeuJoueur:
            print("Egalité, essaye encore")

        # Vérifier si le joueur gagne ou perd en faisant pierre
        elif chiffreAleatoire == tableau.index("pierre"):
            if jeuJoueur == tableau.index("feuille"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")

        # Vérifier si le joueur gagne ou perd en faisant feuille
        elif chiffreAleatoire == tableau.index("feuille"):
            if jeuJoueur == tableau.index("pierre"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")

        # Vérifier si le joueur gagne ou perd en faisant ciseau
        elif chiffreAleatoire == tableau.index("ciseau"):
            if jeuJoueur == tableau.index("pierre"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")      

pierreFeuilleCiseau()