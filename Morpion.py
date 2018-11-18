from math import inf
import random
import turtle as t

#clavier ou souris


ORDI = -1
HUM = 1

def grille():
    t.hideturtle()
    t.speed(0)
    t.width(10)
    t.penup()
    t.goto(-60,180)
    t.right(90)
    t.pendown()
    t.forward(360)
    t.penup()
    t.goto(60,180)
    t.pendown()
    t.forward(360)
    t.penup()
    t.left(90)
    t.goto(-180,60)
    t.pendown()
    t.forward(360)
    t.penup()
    t.goto(-180,-60)
    t.pendown()
    t.forward(360)
    t.penup()
    return
    
    
def croix(x,y):
    #turtle.penup()
    #On laisse du temps pour que le rond se fasse ou on fait tous en instantané
    Hyp=20000**(1/2)
    t.penup()
    t.speed(0)
    t.width(5)
    t.pencolor("red")
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(Hyp)
    t.right(45)
    t.backward(100)
    t.left(135)
    t.backward(Hyp)
    t.penup()
    t.right(45)
    t.goto(x,y)
    t.forward(200)
    return

def rond(x,y):
    #turtle.penup()
    #On laisse du temps pour que le rond se fasse ou on fait tous en instantané
    t.penup()
    t.speed(0)
    t.width(5)
    t.pencolor("blue")
    t.goto(x,y)
    t.pendown()
    t.circle(50)
    t.penup()
    return

def clique(): #mettre une valeur pour choisir forme
    #return int
    t.speed(0)
    t.showturtle()
    t.goto(0,0)
    t.penup()
    t.onscreenclick(condition_clique)
    return 

def condition_clique(x,y):
    if x >= -180 and x <= -60: #1er colonne
        if y >= 60 and y <= 180: #1er ligne
            rond(-120,70)
            return 0
        elif y >= -60 and y <= 60: #2er ligne
            rond(-120,-50)
            return 3
        elif y >= -180 and y <= -60: #3er ligne
            croix(-170,-70)
            return 6
    elif x >= -60 and x <= 60: #2er colonne
        if y >= 60 and y <= 180: #1er ligne
            rond(0,70)
            return 1
        elif y >= -60 and y <= 60: #2er ligne
            rond(0,-50)
            return 4
        elif y >= -180 and y <= -60: #3er ligne
            rond(0,-170)
            return 7
    elif x >= -60 and x <= 180: #3er colonne
        if y >= 60 and y <= 180: #1er ligne
            rond(120,70)
            return 2
        elif y >= -60 and y <= 60: #2er ligne
            rond(120,-50)
            return 5
        elif y >= -180 and y <= -60: #3er ligne
            rond(120,-170)
            return 8
    
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
grille()
A=t.onscreenclick(condition_clique)
print(A)
t.mainloop()
