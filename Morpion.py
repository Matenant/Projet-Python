from math import inf
import random

ORDI = -1
HUM = 1

def gagnant(plateau, joueur):   #Regarde le gagnant de la partie
    if joueur == plateau[0] and plateau[0]==plateau[1] and plateau[1]==plateau[2]:
        return joueur
    elif joueur == plateau[3] and plateau[3]==plateau[4] and plateau[4]==plateau[5]:
        return joueur
    elif joueur == plateau[6] and plateau[6]==plateau[7] and plateau[7]==plateau[8]:
        return joueur
    elif joueur == plateau[0] and plateau[0]==plateau[3] and plateau[3]==plateau[6]:
        return joueur
    elif joueur == plateau[1] and plateau[1]==plateau[4] and plateau[4]==plateau[7]:
        return joueur
    elif joueur == plateau[2] and plateau[2]==plateau[5] and plateau[5]==plateau[8]:
        return joueur
    elif joueur == plateau[0] and plateau[0]==plateau[4] and plateau[4]==plateau[8]:
        return joueur
    elif joueur == plateau[2] and plateau[2]==plateau[4] and plateau[4]==plateau[6]:
        return joueur
    else:
        return 0

def fini(plateau):  #Regarde si la partie est finie
    if gagnant(plateau,ORDI) == -1:
        return True
    elif gagnant(plateau, HUM) == 1:
        return True
    else:
        return False

#―

def afficher(plateau):  #affiche le plateau
    print("")
    print(plateau[0],"|",plateau[1],"|",plateau[2])
    print("――|―――|――")
    print(plateau[3],"|",plateau[4],"|",plateau[5])
    print("――|―――|――")
    print(plateau[6],"|",plateau[7],"|",plateau[8])
    print("")
    

def evaluer(plateau):   #Evalue si la position est gagnante, perdante ou nulle
    if gagnant(plateau, ORDI) == -1:
        score = 1
    elif gagnant(plateau, HUM) == 1:
        score= -1
    else:
        score = 0
    return score
                
def caseVide (plateau): #Retourne un tableau avec les indices de case vide
    case = []
    i = 0
    for i, valeur in enumerate(plateau, 0):
        if valeur == 0:
            case.append(i)
    return case
    
def verifCoup(plateau, coup):   #Vérifie le coup si il est bon
    if coup in caseVide(plateau):
        return True
    else:
        return False
        


def minimax(plateau, profondeur, joueur):
    if joueur == ORDI:
        meilleurCoup = [-1, -inf]
    else:
        meilleurCoup = [-1, inf]
	
    #Condition d'ârret
	
    if profondeur == 0 or fini(plateau) == True:
        score = evaluer(plateau)
        return [-1, score]
    for i in caseVide(plateau):
        plateau[i] = joueur
        score = minimax(plateau, profondeur - 1, -joueur)
        plateau[i] = 0
        score[0] = i
        if joueur == ORDI:
            if score[1] > meilleurCoup[1]:
                meilleurCoup = score
        else:
            if score[1] < meilleurCoup[1]:
                meilleurCoup = score
    return meilleurCoup
		
def tourHum(plateau):
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:
        return plateau
    coup = -1
    verif = False
    while (coup < 0 or coup > 8) or verif == False:
        coup = int(input("Saisir une case entre 1 et 9: ")) - 1
        verif = verifCoup(plateau, coup)
    plateau[coup] = 1
    return plateau

def tourHum2(plateau):
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:
        return plateau
    coup = -1
    verif = False
    while (coup < 0 or coup > 8) or verif == False:
        coup = int(input("Saisir une case entre 1 et 9: ")) - 1
        verif = verifCoup(plateau, coup)
    plateau[coup] = -1
    return plateau

def tourOrdiImpossible(plateau):
    profondeur = len(caseVide(plateau))
    if profondeur == 9:
        plateau[random.randint(0,8)] = -1
        return plateau
    else:
        coup = minimax(plateau, profondeur, ORDI)
        caseCoup = coup[0]
    plateau[caseCoup] = -1
    return plateau

def tourOrdiRandom(plateau):
    verif = False
    while verif == False:
        coup = random.randint(0,8)
        verif = verifCoup(plateau, coup)
    plateau[coup] = -1
    return plateau
		
plateau = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Voulez-vous jouer contre:")
print("1) Un ordinateur imbattable")
print("2) Un ordinateur aléatoire")
print("3) Un autre humain")
typeJeu = int(input("Votre choix: "))

while typeJeu < 1 or typeJeu > 3:
    typeJeu = int(input("Votre saisie est incompréhensible. Saissisez à nouveau: "))

if typeJeu == 1 or typeJeu == 2:
    choix = input("Voulez-vous commencer ? (Y/N) ")
    erreur = True
    while erreur == True:
        if choix == 'Y' or choix == 'y':
            commencer = True
            erreur = False
        elif choix == 'N' or choix == 'n':
            commencer = False
            erreur = False
        else:
            print("Votre saisie est incompréhensible. Saissisez à nouveau: ")

    afficher(plateau)
    while len(caseVide(plateau)) > 0 and fini(plateau) == False:
        if commencer == False:
            
            if typeJeu == 1:
                plateau = tourOrdiImpossible(plateau)
            elif typeJeu == 2:
                plateau = tourOrdiRandom(plateau)
            print("Ordinateur:")
            afficher(plateau)
            commencer = True
            
        plateau = tourHum(plateau)
        afficher(plateau)
        
        if typeJeu == 1:
            plateau = tourOrdiImpossible(plateau)
        elif typeJeu == 2:
            plateau = tourOrdiRandom(plateau)
        print("Ordinateur:")
        afficher(plateau)




    if gagnant(plateau, ORDI) == ORDI:
        print("L'ordinateur a gagné.")
    elif gagnant(plateau, HUM) == HUM:
        print("L'humain a gagné.")
    else:
        print("Egalité.")
        
elif typeJeu == 3:
    while len(caseVide(plateau)) and fini(plateau) == False:
        plateau = tourHum(plateau)
        print("Humain n°1:")
        afficher(plateau)
        if len(caseVide(plateau)) and fini(plateau) == False:
            plateau = tourHum2(plateau)
            print("Humain n°2:")
            afficher(plateau)















