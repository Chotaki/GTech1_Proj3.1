def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Si mon dénominateur est égal à 0, la division est impossible
    if y == 0
    # Alors écrire un message d'erreur dans le terminal
        print("Error: x cannot be divided by 0")
    # Renvoyer rien pour sortir de la fonction
    return
    # Sinon retourner le résultat de la division
    else return x / y

def modulo(x, y):
    return x % y

#calculer revenue par seconde sur 1 an (salaire/h, h/JourOuvrable - 5j/semaine, JO/an)

def revenuePerSecond(SH, Hjo, JOa):
    return ((JOa * Hjo * SH) / (365 * 24 * 60 * 60))

#correction

def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable #Je calcule le salaire annuel
    nbSecondeParAn = 365 * 24 * 60 * 60 #Je calcule le nombre de secondes par an
    return salaireAnnuel / nbSecondeParAn #Je divise le salaire annuel par le nombre de secondes dans une année

#convertir salaire brut en salaire net

def calculNet(SB, public):
    if public: return SB * 15/100 #Je calcule le salaire net pour un employé de la fonction publique
    return SB * 23/100 #Je calcule le salaire net pour un employé d'entreprise privée

#correction

def withdrawFees(total, percent):
    #calcul du montant des taxes à retirer
    fees = total * (percent/100)
    # Je retourne mon total sans les taxes
    return total - fees

def calculSalaireNet(salaireBrut, public):
    # Si j'occupe un poste de la fonction publique
    if public:
        # Alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut, 15)
    # Sinon, c'est que je suis un opérateur privé
    else:
        # Alors je retourne le salaire brut - 23% de douille bien à l'ancienne
        return withdrawFees(salaireBrut, 23)

tour = 0
# Tant que je ne suis pas au tour 5
while tour != 5
    # Appeler la fonction jouerUnTour
    jouerUnTour()
    # J'effectur l'action de passer un tour
    tour = tour + 1

# Autre manière de faire (un peu mieux)
for tour in range(4):
    jouerUnTour()

# Explications
# for pour paramètre défini (ex: pour 5 tours)
# while pour paramètre indéfini (ex: tant que beryl a pas pick heimer) -> dangereux car peut boucler à l'infini

# En C
# for (x=0, x<5; x=x+1)
# selon : for (valeur de début, jusqu'à quel valeur, que faire)

# Exercice
    # Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
    # le caractère doit être paramétrable

def input():
    # Renvoie un caractère de type string au hasard

def miniGame(chosenLetter):
    # A l'appel de ma fonction je peux choisir ma lettre
    # Tant que mon caractère n'est pas le bon
    while chosenLetter != input()
        # Générer un nouveau caractère
        input()
    # Si mon caractère est le bon
    if chosenLetter == input()
        # Alors écrire un message dans le terminal
        print("Congrats, you found the right letter !")

# Correction

def miniGameDeux(chosenLetter):
    # Définir une lettre aléatoire
    actualLetter = input()
    # Tant que la lettre aléatoire n'est pas la même que la lettre choisie
    while actualLetter !== chosenLetter
        # Changer la lettre aléatoire
        actualLetter = input()
    # Afficher un message quand la lettre a été trouvée
    print("Braveau le vo")

# Tableau

tableau = [0,10,15,5,7,6,3,4,8,4,9,5,7,54,8,7,24,45,7]

# Pour recuperer 15 je prends dans le tableau l'index 3 - 1
print(tableau [2]) #Renvoie 15

# Combiner des variables

len(tableau) #Renvoie la longueur du tableau (nombre d'éléments qu'il y a dedans)

prenom = "Anaëlle"
nom = "Romanzin"

nomPrenom = nom + prenom # Renvoie AnaëlleRomanzin
nomPrenom = nom + " " + prenom # Renvoie Anaëlle Romanzin
integerValue = 342
integerValue = str(342) # Renvoie "342" au lieu de 342

# Exercice 1
# Faire une fonction qui concatene 2 chaines de caractère, les séparants par une virgule

motUn = bananes
motDeux = pommes

liste = motUn + ", " + motDeux #Renvoie bananes, pommes

# Correction

# Definir une fonction qui concatene avec comme parametres : une chaineA et chaineB
# qui retourne la concatenation de chaineA, une coma et enfin chaineB
def concatWithComma(chaineA, chaineB):
    # Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaineA)
    # Je m'assure que chaineB soit bien de type str
    stringifiedChaineB = str(chaineB)
    # Retourner chaineA concatenée avec une et chaineB
    return stringifiedChaineA + ", " + stringifiedChaineB

# Exercice 2
# Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
# avec l'ensembles des occurations d'un chiffre e.g.:
# Pour tableau = [0,1,1,1,0,1,1,0,1]
# la fonction(tableau, 0) doit renvoyer "0,4,7" n'hesitez pas à implementer la premiere fonction ;)

tableauExercice = [0,1,1,1,0,1,1,0,1]

def fonction(tableauExercice):
    for index in range(len(tableauExercice)):

# Correction

tableau = [0,1,1,1,0,1,1,0,1]
# Definir une fonction qui prend une liste tableau et une variable x quelconque
def findIndexes(tableau, x):
    # Initialiser i à 0
    i = 0
    # Definir chaineResultat en tant que string vide
    chaineResultat = ""
    # On determine firstTurn a true
    firstTurn = True
    # Tant que i est inferieur à la longueur de tableau
    while i < len(tableau):
        # Alors si l'elt d'index i de tableau est egal a x
        if tableau[i] == x:
            # Alors
            # Si je suis au premier tour (firstTurn est true)
            if firstTurn:
                # Alors j'assigne str(i) a chaine resultat
                chaineResultat = str(i)
                # On passe first turn a false
                firstTurn = False
            # Sinon on assigne a chaineResultat le retour de contactWithComma(chaineResultat, str(i))
            else chaineResultat = concatWithComma(chaineResultat, str(i))
        # On incremente i de 1
        i = i + 1
    # Renvoyer chaineResultat
    return chaineResultat
        
# Exercice 3
# Faire une fonction Afficher un message

def afficherMessage():
    print("J'affiche un message !")

# Exercice 4
# Tel que
listeUtilisateur ={
    "Anaëlle" : "motdepasse",
    "Michel" : "password",
    "Toto" : "12345",
    "JhonDoe" : "azerty"
}
# Ecrivez la fonction login(userName, password, listUser) permettant d'afficher un message de connexion si
# le combo userName/password est bon

# Definir la fonvtion login
def login(userName, password):
    # Si le mdp de la clé username est le même que le mdp entré, alors bon login
    if(mdp==liste[userName]):
        return "Bon login"
    # Sinon, il y a une erreur de mdp ou username
    else:
        return "Mauvais username ou mot de passe"

tableauMultiType = ["Anaëlle", true, tableau, 4 > 2, None]
tableauDim = [0,1,2,3]
tableauDim2 = [0,1,21,3]
tableauMultiDim = [tableauDimn tableauDim2] # En ajoutant un tableau dans un tableau on crée de la dimension (on a des colones en plus des lignes)
tableauMultiDim[1][2] # Renvoie 21

tableauClefVal = {"Clef" : "Valeur"}
tableauClefVal["Clef"] #Renvoie "Valeur"

# Existe pas en python (mais utile en js, php...) :
foreach key : valeur in tableauClefVal
    print(key) # Renvoie "Clef"
    print(valeur) # Renvoie "Valeur"