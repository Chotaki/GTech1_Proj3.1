from random import randint

tableau = ["pierre", "feuille", "ciseau"]

def pierrFeuilleCiseau():
    continuer = True

    while continuer == True:
        chiffreAleatoire = randint(0,2)
        jeuJoueur = input("Entrez un chiffre entre 0 et 2 : ")

        if chiffreAleatoire == jeuJoueur:
            print("Egalité, essaye encore")
        
        elif chiffreAleatoire == tableau["pierre"]:
            if jeuJoueur == tableau["feuille"]:
                print("Bravo tu as gagné !")
                continuer == False
            elif jeuJoueur == tableau["ciseau"]:
                print("Game over, try again")

        elif chiffreAleatoire == tableau["feuille"]:
            if jeuJoueur == tableau["ciseau"]:
                print("Bravo tu as gagné !")
                continuer == False
            elif jeuJoueur == tableau["pierre"]:
                print("Game over, try again")

        elif chiffreAleatoire == tableau["ciseau"]:
            if jeuJoueur == tableau["pierre"]:
                print("Bravo tu as gagné !")
                continuer == False
            elif jeuJoueur == tableau["feuille"]:
                print("Game over, try again")

pierrFeuilleCiseau()