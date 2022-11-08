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
# while pour paramètre indéfini (ex: tant que beryl a pas pick heimer)

# En C
# for (x=0, x<5; x=x+1)
# selon : for (valeur de début, jusqu'à quel valeur, que faire)