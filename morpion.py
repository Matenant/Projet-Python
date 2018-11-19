from math import inf
import random
import turtle as t

#clavier ou souris

ORDI = -1
HUM1 = 1
HUM2 = 2

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
    t.penup()
    t.right(45)
    t.backward(100)
    t.left(135)
    t.pendown()
    t.backward(Hyp)
    t.penup()
    t.right(-45)
    t.forward(100)
    t.right(90)
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

def cliqueOrdi(x):
    if x == 0:
        croix(-170,170)
    elif x == 1:
        croix(-50,170)
    elif x == 2:
        croix(70,170)
    elif x == 3:
        croix(-170,50)
    elif x == 4:
        croix(-50,50)
    elif x == 5:
        croix(70,50)
    elif x == 6:
        croix(-170,-70)
    elif x == 7:
        croix(-50,-70)
    elif x == 8:
        croix(70,-70)

def coordonnee(x,y):
    t.goto(x,y)
    x = t.xcor()
    y = t.ycor()
    return (x,y)

def clique(x,y,plateau):    #J'integre verifCoup pour que le joueur ne puisse pas ecrire par dessus l'adversqaire
    t.onscreenclick(t.goto)
    x,y = coordonnee(x,y)
    if x >= -180 and x <= -60: #1er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,0) == True:
                rond(-120,70)
                return 0, True
            else:
                return 0, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,3) == True:
                rond(-120,-50)
                return 3, True
            else:
                return 3, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,6) == True:
                rond(-120,-170)
                return 6, True
            else:
                return 6, False
    elif x >= -60 and x <= 60: #2er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,1) == True:
                rond(0,70)
                return 1, True
            else:
                return 1, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,4) == True:
                rond(0,-50)
                return 4, True
            else:
                return 4, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,7) == True:
                rond(0,-170)
                return 7, True
            else:
                return 7, False
    elif x >= -60 and x <= 180: #3er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,2) == True:
                rond(120,70)
                return 2, True
            else:
                return 2, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,5) == True:
                rond(120,-50)
                return 5, True
            else:
                return 5, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,8) == True:
                rond(120,-170)
                return 8, True
            else:
                return 8, False
    else:
        return -1, False

def barreHori(x,y):
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)
    t.pendown()
    t.forward(360)
    t.penup()
    t.goto(x,y)
    return
    
def barreVerti(x,y):
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)
    t.right(90)
    t.pendown()
    t.forward(360)
    t.penup()
    t.left(90)
    t.goto(x,y)
    return
    
def barreDiaGD(x,y):
    Hyp=259200**(1/2)
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.left(45)
    t.goto(x,y)
    return
    
def barreDiaDG(x,y):
    Hyp=259200**(1/2)
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)
    t.right(135)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.left(135)
    t.goto(x,y)
    return

def affichageGagnant(plateau):
    if plateau[0]==plateau[1] and plateau[1]==plateau[2] and plateau[1] != 0: #1er ligne
        barreHori(-180,120)
        return
    elif plateau[3]==plateau[4] and plateau[4]==plateau[5] and plateau[4] != 0: #2e ligne
        barreHori(-180,0)
        return 
    elif plateau[6]==plateau[7] and plateau[7]==plateau[8] and plateau[7] != 0: #3e ligne
        barreHori(-180,-120)
        return 
    elif plateau[0]==plateau[3] and plateau[3]==plateau[6] and plateau[3] != 0: #1er colonne
        barreVerti(-120,180)
        return 
    elif plateau[1]==plateau[4] and plateau[4]==plateau[7] and plateau[4] != 0: #2e colonne
        barreVerti(0,180)
        return 
    elif plateau[2]==plateau[5] and plateau[5]==plateau[8] and plateau[5] != 0: #3e colonne
        barreVerti(120,180)
        return 
    elif plateau[0]==plateau[4] and plateau[4]==plateau[8] and plateau[4] != 0: #dia G-D
        barreDiaGD(-180,180)
        return 
    elif plateau[2]==plateau[4] and plateau[4]==plateau[6] and plateau[4] != 0: #dia D-G
        barreDiaDG(180,180)
        return 

def gagnant(plateau, joueur):   #Regarde le gagnant de la partie
    if joueur == plateau[0] and plateau[0]==plateau[1] and plateau[1]==plateau[2] and plateau[1] != 0: #1er ligne
        return joueur
    elif joueur == plateau[3] and plateau[3]==plateau[4] and plateau[4]==plateau[5] and plateau[4] != 0: #2e ligne
        return joueur
    elif joueur == plateau[6] and plateau[6]==plateau[7] and plateau[7]==plateau[8] and plateau[7] != 0: #3e ligne
        return joueur
    elif joueur == plateau[0] and plateau[0]==plateau[3] and plateau[3]==plateau[6] and plateau[3] != 0: #1er colonne
        return joueur
    elif joueur == plateau[1] and plateau[1]==plateau[4] and plateau[4]==plateau[7] and plateau[4] != 0: #2e colonne
        return joueur
    elif joueur == plateau[2] and plateau[2]==plateau[5] and plateau[5]==plateau[8] and plateau[5] != 0: #3e colonne
        return joueur
    elif joueur == plateau[0] and plateau[0]==plateau[4] and plateau[4]==plateau[8] and plateau[4] != 0: #dia G-D
        return joueur
    elif joueur == plateau[2] and plateau[2]==plateau[4] and plateau[4]==plateau[6] and plateau[4] != 0: #dia D-G
        return joueur
    else:
        return 0

def fini(plateau):  #Regarde si la partie est finie
    if gagnant(plateau,ORDI) == -1:
        return True
    elif gagnant(plateau, HUM1) == 1:
        return True
    elif gagnant(plateau, HUM2) == 2:
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
    elif gagnant(plateau, HUM1) == 1:
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
		
def tourHum1(plateau):
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:
        return plateau
    coup = -1
    verif = False
    while coup == None or verif == False:
        coup, verif = clique(400,400,plateau)
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
    plateau[coup] = 2
    return plateau

def tourOrdiImpossible(plateau):
    profondeur = len(caseVide(plateau))   #On définit la profondeur selon le niveau de difficulté choisi imbattable (8), difficile (5), moyen (3), facile (1), car premier coup aléatoire donc on enlève 1
    if profondeur == 9:
        RAND = random.randint(0,8)
        plateau[RAND] = -1
        cliqueOrdi(RAND)        
        return plateau
    else:
        coup = minimax(plateau, profondeur, ORDI)
        caseCoup = coup[0]
    cliqueOrdi(caseCoup)
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

grille()

print("Voulez-vous jouer contre:")
print("1) Un ordinateur")
print("2) Un autre humain")
typeJeu = int(input("Votre choix: "))

while typeJeu < 1 or typeJeu > 3:
    typeJeu = int(input("Votre saisie est incompréhensible. Saissisez à nouveau: "))


if typeJeu == 1:
    print("Choissisez un niveau de difficulté:")
    print("1) Un ordinateur imbattable")
    print("2) Un ordinateur difficile")
    print("3) Un ordinateur moyen")
    print("4) Un ordinateur facile")
    print("5) Un ordinateur aléatoire")
    difficulté =  int(input("Votre choix: "))
    while difficulté < 1 or difficulté > 5:
        difficulté = int(input("Votre saisie est incompréhensible. Saissisez à nouveau: "))
        
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

#   afficher(plateau)
    while len(caseVide(plateau)) > 0 and fini(plateau) == False:
        if commencer == False:
            if difficulté == 1:
                plateau = tourOrdiImpossible(plateau)
            elif difficulté == 5:
                plateau = tourOrdiRandom(plateau)
            print("Ordinateur:")
            afficher(plateau)
            commencer = True
                
        plateau = tourHum1(plateau)
        afficher(plateau)
            
        if typeJeu == 1:
            plateau = tourOrdiImpossible(plateau)
        elif typeJeu == 5:
            plateau = tourOrdiRandom(plateau)
        print("Ordinateur:")
        afficher(plateau)


    affichageGagnant(plateau)
    
    if gagnant(plateau, ORDI) == ORDI:
        print("L'ordinateur a gagné.")
    elif gagnant(plateau, HUM1) == HUM1:
        print("L'humain a gagné.")
    else:
        print("Egalité.")
        
elif typeJeu == 2:
    while len(caseVide(plateau)) and fini(plateau) == False:
        plateau = tourHum1(plateau)
        print("Humain n°1:")
        afficher(plateau)
        if len(caseVide(plateau)) and fini(plateau) == False:
            plateau = tourHum2(plateau)
            print("Humain n°2:")
            afficher(plateau)

    if gagnant(plateau, HUM1) == HUM1:
        print("L'humain n°1 a gagné")
    elif gagnant(plateau, HUM2):
        print("L'humain n°2 a gagné")
    else:
        print("Il y a égalité")
