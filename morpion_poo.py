import numpy as np
import random


class morpion:

    # Définition des classes dont dépend la classe morpion
    class case:
        def __init__ (self, numero1, ligne1, colonne1):
            self.numero = numero1
            self.ligne = ligne1
            self.colonne = colonne1
            self.alignements = []
            self.valeur = 0

    class alignement:
        def __init__ (self, numero1, listeCases1):
            self.numero = numero1
            self.listeCases = listeCases1

        def alignCountifLambda(self, lambda1):
            return sum((1 if lambda1(case1.valeur) else 0) for case1 in self.listeCases)

        def alignJouable(self):
            return (self.alignCountifLambda( lambda x : x ==0) > 0)

        def scoreJoueur(self, joueur1: int):
            res = self.alignCountifLambda(lambda x : x==joueur1)
            if self.alignCountifLambda(lambda x : x==morpion.funcOtherPlayer(joueur1))>0:
                res = -1
            return res
    
    class joueur:
        def __init__ (self, numero1, nom1, isRobot1):
            self.numero = numero1
            self.nom = nom1
            self.estRobot = bool(isRobot1)

#--------------------------------------------------------------------------------
    # Constructeur
    def __init__(self):

        # Définition des cases
        self.case1 = morpion.case(1,1,1)
        self.case2 = morpion.case(2,1,2)
        self.case3 = morpion.case(3,1,3)
        self.case4 = morpion.case(4,2,1)
        self.case5 = morpion.case(5,2,2)
        self.case6 = morpion.case(6,2,3)
        self.case7 = morpion.case(7,3,1)
        self.case8 = morpion.case(8,3,2)
        self.case9 = morpion.case(9,3,3)

        # Définition des alignements : lignes, colonnes et diagonales
        # On fait le lien alignements --> cases
        self.ligne1 = morpion.alignement(1, [self.case1, self.case2, self.case3])
        self.ligne2 = morpion.alignement(1, [self.case4, self.case5, self.case6])
        self.ligne3 = morpion.alignement(1, [self.case7, self.case8, self.case9])
        self.colonne1 = morpion.alignement(1, [self.case1, self.case4, self.case7])
        self.colonne2 = morpion.alignement(1, [self.case2, self.case5, self.case8])
        self.colonne3 = morpion.alignement(1, [self.case3, self.case6, self.case9])
        self.diagonale1 = morpion.alignement(1, [self.case1, self.case5, self.case9])
        self.diagonale2 = morpion.alignement(1, [self.case7, self.case5, self.case3])

        # Définition de listes sur lesquelles on va itérer
        self.listeCases = [self.case1, self.case2, self.case3, self.case4, self.case5, self.case6, self.case7, self.case8, self.case9]
        self.listeAlignements = [self.ligne1, self.ligne2, self.ligne3, self.colonne1, self.colonne2, self.colonne3, self.diagonale1, self.diagonale2]
        self.listeLignes = [self.ligne1, self.ligne2, self.ligne3]

        # On établit les liens dans le sens cases --> alignements
        self.case1.alignements = [self.ligne1, self.colonne1, self.diagonale1]
        self.case2.alignements = [self.ligne1, self.colonne2]
        self.case3.alignements = [self.ligne1, self.colonne3, self.diagonale2]
        self.case4.alignements = [self.ligne2, self.colonne1]
        self.case5.alignements = [self.ligne2, self.colonne2, self.diagonale1, self.diagonale2]
        self.case6.alignements = [self.ligne2, self.colonne3]
        self.case7.alignements = [self.ligne3, self.colonne1, self.diagonale2]
        self.case8.alignements = [self.ligne3, self.colonne2]
        self.case9.alignements = [self.ligne3, self.colonne3, self.diagonale1]

        # Définition des joueurs
        self.joueur1 = morpion.joueur(1, "Humain", False)
        self.joueur2 = morpion.joueur(1, "NONO", True)
        self.listeJoueurs = [self.joueur1, self.joueur2]
        self.currentPlayer = 1

        # Définition du tour de jeu
        self.turn = 1

#--------------------------------------------------------------------------------

    # Getter/Setter de cases par leur numéro dans la classe morpion
    def getValeurCase(self, numCase1 = 1):
        res = 0
        for case1 in self.listeCases:
            if case1.numero == numCase1:
                res = case1.valeur
        return res

    def setValeurCase(self, numCase1 = 1, valeur1 = 0):
        for case1 in self.listeCases:
            if case1.numero == numCase1:
                case1.valeur = valeur1
        return

    def getListeCasesVides(self):
        return [case1 for case1 in self.listeCases if case1.valeur==0]


    # Méthodes pour passer au joueur ou tour suivant
    def nextTurn(self):
         self.turn += 1
         print("Nous sommes au %dème tour" % self.turn)
         print()
         return

    def funcOtherPlayer(num1):
        return (num1)%2 + 1

    def numOtherPlayer(self):
        return morpion.funcOtherPlayer(self.currentPlayer)

    def nextPlayer(self):
        self.currentPlayer = self.numOtherPlayer()
        if self.currentPlayer==1:
            self.nextTurn()
        return


    # Getter pour les joueurs liés à la classe morpion
    def joueurActif(self):
        return self.listeJoueurs[self.currentPlayer -1]

    def joueurInactif(self):
        return self.listeJoueurs[self.numOtherPlayer() -1]

    
    # Méthodes d'analyse des alignements pour le robot

    def listeAlignementsJouables(self):
        return [align1 for align1 in self.listeAlignements if align1.alignJouable()]

    def maxScoreAlign(self, numJoueur1):
        listeAlignJoueurActifScores = [align1.scoreJoueur(numJoueur1) for align1 in self.listeAlignementsJouables()]
        return max(listeAlignJoueurActifScores)

    def listeMaxScoreAlign(self, numJoueur1):
        return [align1 for align1 in self.listeAlignementsJouables() if align1.alignCountifLambda(lambda x : x==numJoueur1)==self.maxScoreAlign(numJoueur1)]

    # Méthodes d'affichage du plateau de jeu
    def num2Char(n):
        res = "_"
        if n == 1:
            res = "X"
        elif n == 2:
            res ="0"
        return res

    def display(self):
        for ligne1 in self.listeLignes:
            for case1 in ligne1.listeCases:
                print("\t", morpion.num2Char(case1.valeur), end="")
            print()
        print()
        return


    # Fonctions pour vérifier si le jeu se termine
    def isWinner(self):
        res = [align1.listeCases[0].valeur for align1 in self.listeAlignements if (align1.listeCases[0].valeur!=0)&(align1.alignCountifLambda(lambda x : x==align1.listeCases[0].valeur)==3)]
        return res

    def isFull(self):
        res = all([align1.alignCountifLambda(lambda x : x!=0)==3 for align1 in self.listeLignes])
        return res

    def jeuContinue(self):
        return (len(self.isWinner())==0)&(not self.isFull())


    # Méthodes pour déterminer le comportement des joueurs humains ou robots à chaque
    def tourHumain(self):
        instruct1 =''
        instruct1Num = 0
        while not (instruct1Num>0):
            instruct1 = input("Ou souhaitez vous placer votre pion? ")
            if not(instruct1.isdigit()):
                print("L'entrée doit être un nombre entier entre 1 et 9")
                instruct1Num = 0
            else:
                instruct1Num = int(instruct1)
                if not(instruct1Num in range(1,10)) :
                    print("L'entrée est bien un nombre entier, mais doit aussi être entre 1 et 9")
                    instruct1Num = 0
                else:
                    if self.getValeurCase(instruct1Num)!=0:
                        print("L'entrée est correcte, mais la case choisie est déjà occupée")
                        instruct1Num = 0
                    else:
                        print("Le pion à bien été posé")
        return instruct1Num


    def tourRobot(self):
        listeCasesVides = self.getListeCasesVides()

        # Choix de stratégie : aligner des pions ou bloquer l'autre
        if max(self.maxScoreAlign(self.currentPlayer))>=(self.maxScoreAlign(self.numOtherPlayer())):
            numJoueur = self.currentPlayer
        else:
            numJoueur = self.numOtherPlayer()

        listeAlignMax = self.listeMaxScoreAlign(numJoueur)
        listeCasesMax = [case1.numero for align1 in listeAlignMax for case1 in align1.listeCases if case1 in listeCasesVides]
        listeCasesMaxCount = [ (n, listeCasesMax.count(n)) for n in range(1,10)]
        maxCount = max([n for i, n in listeCasesMaxCount])
        listeFinale =[i for i, n in listeCasesMaxCount if n==maxCount]
        numCase1 = random.choice(listeFinale)

        print("Le joueur %s a joué son tour en case %d" % (self.listeJoueurs[self.currentPlayer-1].nom, numCase1))
        return numCase1

    # Méthode pour jouer une partie
    def partie(self):
        caseChoisie = 0
        print("Le jeu commence : 1er tour")
        print()
        self.display()

        while self.jeuContinue():
            joueurActif = self.listeJoueurs[self.currentPlayer -1]
            if joueurActif.estRobot:
                caseChoisie = self.tourRobot()
            else:
                caseChoisie =  self.tourHumain()
            
            self.setValeurCase(caseChoisie, self.currentPlayer)
            self.display()

            if len(self.isWinner())==0:
                self.nextPlayer()
        
        print("La partie est finie")
        if self.isFull():
            print("Toutes les cases sont occupées et personne n'a gagné")
        else:
            print("Le gagnant est le joueur %s" % joueurActif.nom)
        print()
    
# instanciation du jeu et démarrage de la partie
jeuMorp1 = morpion()
jeuMorp1.partie()