from math import inf
import random

ORDI = -1
HUM = 1

def gagnant(plateau, joueur):   #A voir comment optimiser cette fonction elle est pas fini
    if j and tableau[0]==tableau[1] and tableau[1]==tableau[2]:
        return joueur
    elif tableau[3]==1 and tableau[4]==1 and tableau[5]==1:
        return 
    elif tableau[6]==1 and tableau[7]==1 and tableau[8]==1:
        return 1
    elif tableau[0]==1 and tableau[3]==1 and tableau[6]==1:
        return 1
    elif tableau[1]==1 and tableau[4]==1 and tableau[7]==1:
        return 1
    elif tableau[2]==1 and tableau[5]==1 and tableau[8]==1:
        return 1
    elif tableau[0]==1 and tableau[4]==1 and tableau[8]==1:
        return 1
    elif tableau[2]==1 and tableau[4]==1 and tableau[6]==1:
        return 1

#―

def afficher(plateau):  #Affiche le plateau
        print("",plateau[0],"|",plateau[1],"|",plateau[2])
        print("―――|―――|―――")
        print("",plateau[3],"|",plateau[4],"|",plateau[5])
        print("―――|―――|―――")
        print("",plateau[6],"|",plateau[7],"|",plateau[8])


def evaluer(plateau):   #Regarde qui a gagné et attribut une note
        if gagnant(plateau, ORDI):
                score = 1
        elif gagnant(plateau, HUM):
                score= -1
        else:
                score = 0
        return score

def tourHum(plateau):   #Fonction qui fait jouer l'humain
        profondeur = len(caseVide(plateau))
        if profondeur == 0 or gagnant(plateau):
                return 0
        coup = -1
        verif = False
        while (coup < 0 or coup > 8) and verif:
                coup = int(input("Saisir une case entre 1 et 9")) - 1
                verif = verifCoup(plateau, coup)
        plateau[coup] = 2
        return plateau

def tourOrdi(plateau):  #Fonction qui fait jouer l'ordinateur
        profondeur = len(caseVide(plateau))
        if prodondeur == 9:
                plateau[random.randint(0,9)] = 1
        else:
                coup = minimax(plateau, profondeur, ORDI)
                case = coup[0]
        plateau[case] = 1
        return plateau
                
def caseVide (plateau): #Fonction qui permet de savoir ou sont le case vide
        case = []
        k = 0
        for i in plateau:
                if i == 0:
                        case.append(k)
                k = k + 1
        return case


def minimax(plateau, profondeur, joueur):   #Fonction minimax
	if joueur == ORDI:
		meilleurCoup = [-1, -inf]
	else:
		meilleurCoup = [-1, inf]
	
	#Condition d'ârret
	
	if profondeur == 0 or gagnant(plateau) == True:
		score = evaluer(plateau)
		return [-1, score]
	for i in caseVide(plateau):
		plateau[i] = joueur
		score = minimax(plateau, profondeur - 1, -joueur)
		score[0] = i
		if joueur == ORDI:
			if score[1] > meileurCoup[1]:
				meilleurCoup = score
		else:
			if score[1] < meilleurCoup[1]:
				meilleurCoup = score
		return meilleurCoup
		
		
plateau = [0, 1, 0, 0, 0, 0, 0, 0, 0]

afficher(plateau)
