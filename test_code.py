from random import randint

tableau = ["pierre", "feuille", "ciseau"]

def pierreFeuilleCiseau():
    continuer = True

    while continuer:
        chiffreAleatoire = randint(0,2)
        jeuJoueur = int(input("Entrez un chiffre entre 0 et 2 : "))

        print(chiffreAleatoire, jeuJoueur)

        if chiffreAleatoire == jeuJoueur:
            print("Egalité, essaye encore")

        elif chiffreAleatoire == tableau.index("pierre"):
            if jeuJoueur == tableau.index("feuille"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")

        elif chiffreAleatoire == tableau.index("feuille"):
            if jeuJoueur == tableau.index("pierre"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")

        elif chiffreAleatoire == tableau.index("ciseau"):
            if jeuJoueur == tableau.index("pierre"):
                print("Bravo tu as gagné !")
                continuer == False
            else:
                print("Game over, try again")

pierreFeuilleCiseau()