import random

class TicTacToe :

    def __init__(self):
        self.table = []

    # Générer la grille de jeu
    def generateTable(self):

        for i in range(3) :
            row = []
            for j in range(3):
                row.append("-")
            self.table.append(row)

    # Définir un premier joueur aléatoire
    def randomFirstPlayer(self):
        return random.randint(0, 1)

    # Définir player comme les coordonés d'une case dans la grille de jeu
    def fixSpot(self, row, col, player):
        self.table[row][col] = player

    # Vérifier si le joueur a gagné
    def playerWin(self, player):
        win = None

        n = len(self.table)

        # Vérifier les colonnes
        for i in range(n):
            win = True
            for j in range(n):
                if self.table[i][j] != player:
                    win = False
        if win:
            return win

        # Vérifier les lignes
        for i in range(n):
            win = True
            for j in range(n):
                if self.table[j][i] != player:
                    win = False
                    break
        if win:
            return win

        # Vérifier les diagonales
        win = True
        for i in range(n):
            if self.table[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.table[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.table:
            for item in row:
                if item == "-":
                    return False
        return True

    # Vérifier que la grille de jeu est vide
    def emptyTable(self):
        for row in self.table:
            for item in row:
                if item == '-':
                    return False
        return True
    
    # Changer de joueur
    def swapPlayer(self, player):
        return "X" if player == "0" else "O"

    # Afficher la grille de jeu
    def showTable(self):
        for row in self.table:
            for item in row:
                print(item, end=" ")
            print()

    # Commencer la partie
    def start(self):
        self.generateTable()

        if self.randomFirstPlayer() == 1:
            player = "X"
        else:
            player = "O"
        while True:
            print("Player {player}'s turn")

            self.showTable()

            # Le joueur va insérer une valeur à jouer
            row, col = list(
                int(input("Enter row and column of the spot you want to play : ")).split())

            # Vérifier si le joueur a gagné ou non
            if self.playerWin():
                print("Player {player} won !")
            break

            # Vérifier si il y a égalité
            if self.emptyTable():
                print("Egalité !")
            break
 
            # Changer de joueur
            player = self.swapPlayer(player)

            # Montrer la grille de jeu finale
            print()
            self.showTable()

# Lancer le jeu
tic_tac_toe = TicTacToe()
tic_tac_toe.start()