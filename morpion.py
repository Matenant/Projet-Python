from math import inf
import random
import turtle as t

#clavier ou souris

ORDI = -1
HUM1 = 1
HUM2 = 2

def DebutGraph():   #Regroupe l'affichage graphique de base
    t.title("Morpion 1.0")  #Titre
    texteChoixDifficulté()  #Affiche texte/croix pour choix difficulté
    grille()    #La grille du morpion
    return
    
def texteChoixDifficulté():
    t.hideturtle()
    t.speed(0)
    t.width(10)
    t.penup()
    
    t.goto(-200,350)
    t.write("Choisissez la difficulté :", font=(15))
    t.goto(-180,300)
    t.write("Impossible")
    t.goto(-80,300)
    t.write("Difficile")
    t.goto(0,300)
    t.write("Moyen")
    t.goto(80,300)
    t.write("Facile")
    t.goto(150,300)
    t.write("Random")
    t.goto(-180,240)
    t.write("Commencer")
    t.goto(150,240)
    t.write("2 joueurs")

    croixDiffGrey(-165,290) #impo
    croixDiffGrey(-74,290)  #Diff
    croixDiffGrey(5,290)   #Moy
    croixDiffGrey(83,290)  #fac
    croixDiffGrey(160,290)  #rand
    croixDiffGrey(-165,230) #comm
    croixDiffGrey(160,230) #2j

    t.pencolor("black")
    t.goto(-10,210)
    t.write("Jouer", font=(40))
    return

def croixDiffGrey(x,y):
    Hyp=800**(1/2)
    t.penup()
    t.speed(0)
    t.width(2)
    t.pencolor("darkgrey")
    
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.left(135)
    t.forward(20)
    t.left(135)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.right(225)
    t.goto(x,y)
    return

def croixDiffBlack(x,y):
    Hyp=800**(1/2)
    t.penup()
    t.speed(0)
    t.width(2)
    t.pencolor("black")
    
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.left(135)
    t.forward(20)
    t.left(135)
    t.pendown()
    t.forward(Hyp)
    t.penup()
    t.right(225)
    t.goto(x,y)
    return

def verifChoix(tableChoix,choix):
    if tableChoix[choix] == 0:
        return True
    else:
        return False
    
def choixDifficulte(tableauEtat,xdel,ydel):
    x, y = 400, 400
    t.onscreenclick(t.goto)
    x,y = coordonnee(x,y)
    if y >= 270 and y <= 290: #1er ligne
        if x >= -165 and x <= -145: #imp
            if verifChoix(tableauEtat,0) == True:
                croixDiffBlack(-165,290)
                return 1, -165, 290
            else:
                croixDiffGrey(-165,290)
                return -1, -165, 290
        elif x >= -74 and x <= -54: #diff
            if verifChoix(tableauEtat,1) == True:
                croixDiffBlack(-74,290)
                return 2, -74, 290
            else:
                croixDiffGrey(-74,290)
                return -2, -74, 290
        elif x >= 5 and x <= 25: #moy
            if verifChoix(tableauEtat,2) == True:
                croixDiffBlack(5,290)
                return 3, 5, 290
            else:
                croixDiffGrey(5,290)
                return -3, 5, 290
        elif x >= 83 and x <= 103: #fac
            if verifChoix(tableauEtat,3) == True:
                croixDiffBlack(83,290)
                return 4, 83, 290
            else:
                croixDiffGrey(83,290)
                return -4, 83, 290
        elif x >= 160 and x <= 180: #random
            if verifChoix(tableauEtat,4) == True:
                croixDiffBlack(160,290)
                return 5, 160, 290
            else:
                croixDiffGrey(160,290)
                return -5, 160, 290
        else:
            return 0, 0, 0
    elif y >= 210 and y <= 230:
        if x >= -165 and x <= -145: #comm
            if verifChoix(tableauEtat,5) == True:
                croixDiffBlack(-165,230)
                return 6, -165, 230
            else:
                croixDiffGrey(-165,230)
                return -6, -165, 230
        elif x >= 160 and x <= 180: #2p
            if verifChoix(tableauEtat,6) == True:
                croixDiffBlack(160,230)
                return 7, 160, 230
            else:
                croixDiffGrey(160,230)
                return -7, 160, 230
        elif x >= -10 and x <= 20: #jouer
            return 8, 0, 0
        else:
            return 0, 0, 0
    else:
        return 0, 0, 0
    
def grille():
    t.hideturtle()
    t.speed(0)
    t.width(10)
    t.pencolor('black')
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

def clique(plateau, joueur):    #J'integre verifCoup pour que le joueur ne puisse pas ecrire par dessus l'adversqaire
    x, y = 400, 400
    t.onscreenclick(t.goto)
    x,y = coordonnee(x,y)
    if x >= -180 and x <= -60: #1er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,0) == True:
                if joueur == 1:
                    rond(-120,70)
                else:
                    croix(-170,170)
                return 0, True
            else:
                return 0, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,3) == True:
                if joueur == 1:
                    rond(-120,-50)
                else:
                    croix(-170,50)
                return 3, True
            else:
                return 3, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,6) == True:
                if joueur == 1:
                    rond(-120,-170)
                else:
                    croix(-170,-70)
                return 6, True
            else:
                return 6, False
    elif x >= -60 and x <= 60: #2er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,1) == True:
                if joueur == 1:
                    rond(0,70)
                else:
                    croix(-50,170)
                return 1, True
            else:
                return 1, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,4) == True:
                if joueur == 1:
                    rond(0,-50)
                else:
                    croix(-50,50)
                return 4, True
            else:
                return 4, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,7) == True:
                if joueur == 1:
                    rond(0,-170)
                else:
                    croix(-50,-70)
                return 7, True
            else:
                return 7, False
    elif x >= -60 and x <= 180: #3er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,2) == True:
                if joueur == 1:
                    rond(120,70)
                else:
                    croix(70,170)
                return 2, True
            else:
                return 2, False
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,5) == True:
                if joueur == 1:
                    rond(120,-50)
                else:
                    croix(70,50)
                return 5, True
            else:
                return 5, False
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,8) == True:
                if joueur == 1:
                    rond(120,-170)
                else:
                    croix(70,-70)
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

def affichageGagnant(plateau):  #!=0 en premier
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
    else:
        return

def gagnant(plateau, joueur):   #Regarde le gagnant de la partie
    #Première ligne
    if joueur == plateau[0] and plateau[0]==plateau[1] and plateau[1]==plateau[2]:#On vérifie chaque cas pour voir si il y a un gagnant en fonction du joueur passé en paramètre
        return joueur       #On retourne le joueur qu'on a passé en paramètre si il a gagné
    #Deuxième ligne
    elif joueur == plateau[3] and plateau[3]==plateau[4] and plateau[4]==plateau[5]:
        return joueur
    #Troisième ligne
    elif joueur == plateau[6] and plateau[6]==plateau[7] and plateau[7]==plateau[8]:
        return joueur
    #Première colonne
    elif joueur == plateau[0] and plateau[0]==plateau[3] and plateau[3]==plateau[6]:
        return joueur
    #Deuxième colonne
    elif joueur == plateau[1] and plateau[1]==plateau[4] and plateau[4]==plateau[7]:
        return joueur
    #Troisième colonne
    elif joueur == plateau[2] and plateau[2]==plateau[5] and plateau[5]==plateau[8]:
        return joueur
    #Première diagonale
    elif joueur == plateau[0] and plateau[0]==plateau[4] and plateau[4]==plateau[8]:
        return joueur
    #Deuxième diagonale
    elif joueur == plateau[2] and plateau[2]==plateau[4] and plateau[4]==plateau[6]:
        return joueur
    #IL n'a pas gagné
    else:
        return 0

#0|1|2
#―――――
#3|4|5
#―――――
#6|7|8

def fini(plateau):  #Regarde si la partie est finie
    if gagnant(plateau,ORDI) == -1: #On voit si quelqu'un a gagné et on retourne vrai si c'est le cas car la partie est fini
        return True
    elif gagnant(plateau, HUM1) == 1:
        return True
    elif gagnant(plateau, HUM2) == 2:
        return True
    else:                           #Sinon elle n'est pas fini (On gère le cas de l'égalité plus tard dans le code)
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
    if gagnant(plateau, ORDI) == -1: #Si l'ordinateur gagne alors il a un score positif
        score = 1
    elif gagnant(plateau, HUM1) == 1: #Si l'humain gagne alors c'est un score négatif pour l'ordinateur
        score= -1
    else:
        score = 0               #Sinon c'est 0 qui indique une égalité ou le jeu n'est pas fini et donc elle n'est pas évaluable
    return score



                
def caseVide (plateau): #Retourne un tableau avec les indices de case vide
    case = []
    i = 0
    for i, valeur in enumerate(plateau, 0): #On parcourt le plateau avec enumerate qui permet de mettre dans i l'indice de la case et la valeur de cette case dans case
        if valeur == 0:         #Si la valeur est égal à 0 alors c'est une case vide
            case.append(i)      #On ajoute l'indice dans notre tableau case
    return case


    
def verifCoup(plateau, coup):   #Vérifie le coup si il est bon
    if coup in caseVide(plateau):   #On vérifie que la case est disponible avec la fonction caseVide
        return True         #Elle est libre
    else:
        return False        #Elle n'est pas libre
        


def minimax(plateau, profondeur, joueur):   #Fonction minimax qui parcourt l'arbre des possibilités et choisi le meilleur coup
    if joueur == ORDI:              #Si c'est le coup de l'ordinateur
        meilleurCoup = [-1, -inf]   #On initialise meilleurCoup avec une case à -1 et le score à -inf pour qu'il se fasse remplacé par la suite
    else:                           #De même pour le tour de l'humain
        meilleurCoup = [-1, inf]    #On initialise meilleurCoup avec une case à -1 et le score à inf pour qu'il se fasse remplacé par la suite
	
    #Condition d'ârret
    if profondeur == 0 or fini(plateau) == True:    #On regarde si on arrive à la fin du la profondeur demandé ou si la partie est fini
        score = evaluer(plateau)            #On évalue le score de la position
        return [-1, score]                  #On retourne une position et le score
    for i in caseVide(plateau):             #On parcourt les cases vides du plateau
        plateau[i] = joueur                 #On pose un jeton du joueur en cours de traitement dans la première case vide
        score = minimax(plateau, profondeur - 1, -joueur)       #On envoie l'état du plateau dans minimax pour qu'il puisse recalculer le coup suivant avec l'autre joueur
        plateau[i] = 0                      #On annule le coup qu'on vient de faire
        score[0] = i                        #On met le coup dans la première case de score
        if joueur == ORDI:                  #Si c'est le tour du joueur
            if score[1] > meilleurCoup[1]:  #On compare le score de score et le score de meilleurCoup pour que le coup de l'ordinateur soit meilleur que le coup d'avant
                meilleurCoup = score
        else:                               #Si c'est le tour de l'humain
            if score[1] < meilleurCoup[1]:  #On compare le score de score et le score de meilleurCoup pour que le coup de l'humain soit le meilleur pour lui et donc le moins bon pour nous
                meilleurCoup = score
    return meilleurCoup                     #On retourne le meilleur coup
		
def tourHum1(plateau):                      	#Fonction qui fait jouer le premier humain
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:#On regarde si il reste des cases vides ou si il y a un gagnant
        return plateau
    coup = -1				#On initialise le coup à -1 pour rentrer dans la boucle
    verif = False			#De même pour la vérification du coup qu'on met à faux
    while (coup < 0 or coup > 8) or verif == False:#On demande à l'utilisateur de saisir tant qu'il ne saisit pas une bonne case
        coup, verif = clique(plateau, 1)	#On vérifie son coup
    plateau[coup] = 1			#On place le jeton à la case qu'il demande
    return plateau			#On retourne le plateau

def tourHum2(plateau):				#Fonction qui fait jouer le deuxième humain
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:#On regarde si il reste des cases vides ou si il y a un gagnant
        return plateau
    coup = -1				#On initialise le coup à -1 pour rentrer dans la boucle
    verif = False			#De même pour la vérification du coup qu'on met à faux
    while (coup < 0 or coup > 8) or verif == False:#On demande à l'utilisateur de saisir tant qu'il ne saisit pas une bonne case
        coup, verif = clique(plateau, 2)	#On vérifie son coup
    plateau[coup] = 2			#On place le jeton à la case qu'il demande
    return plateau			#On retourne le plateau

def tourOrdi(plateau, niveau):		#Fonction qui fait jouer l'ordinateur
    profondeur = len(caseVide(plateau))	#On prend le nombre de case vide
    if niveau == -1:		#Si le niveau est imbattable on prend le nombre de case vide an tant que profondeur
        niveau = profondeur
    if profondeur == 9 or niveau == 0:	#Le premier coup ou le choix de l'ordinateur aléatoire donne le premier coup ou tous les autres aléatoires
        verif = False
        while verif == False:	#On vérifie que le coup n'écrase pas un autre coup
            coup = random.randint(0,8)	#On génère le coup aléatoire
            verif = verifCoup(plateau, coup)    #On le vérifie
        cliqueOrdi(coup)    
        plateau[coup] = -1	#On place le coup
        return plateau		#On retourne le plateau
    else:
        coup = minimax(plateau, niveau, ORDI)	#On utilise la fonction minimax pour trouver le meilleur coup à jouer selon l'état du jeu
        caseCoup = coup[0]		#On sauvegarde le coup dans une variable
    cliqueOrdi(caseCoup)
    plateau[caseCoup] = -1		#On place le coup de l'ordinateur
    return plateau

def modifTableChoix(table,i):
    if i == 0:
        return table
    elif i > 0:
        table[i-1] = 1
        return table
    elif i == -1:
        table[0] = 0
        return table
    elif i == -2:
        table[1] = 0
        return table
    elif i == -3:
        table[2] = 0
        return table
    elif i == -4:
        table[3] = 0
        return table
    elif i == -5:
        table[4] = 0
        return table
    elif i == -6:
        table[5] = 0
        return table
    elif i == -7:
        table[6] = 0
        return table

def conditionsDifficulte(table,i):
    if table[5] == 1:
        if table[7] == 1:
            if table[6] == 1:
                return 0, False, False, False
            else:
                return i, True, False, True
        else:
            return 0, False, False, False
    else:
        if table[7] == 1:
            if table[6] == 1:
                return 0, False, False, False
            else:
                return i, False, False, True
        else:
            return 0, False, False, False

def difficulte(table):
    if table[0] == 1:
        return conditionsDifficulte(table,1)
    elif table[1] == 1:
        return conditionsDifficulte(table,2)
    elif table[2] == 1:
        return conditionsDifficulte(table,3)
    elif table[3] == 1:
        return conditionsDifficulte(table,4)
    elif table[4] == 1:
        return conditionsDifficulte(table,5)
    elif table[6] == 1:
        if table[7] == 1:
            if table[5] == 1:
                return 0, False, False, False
            else:
                return 0, False, True, True
    return 0, False, False, False
                        
        
		
plateau = [0, 0, 0, 0, 0, 0, 0, 0, 0]

DebutGraph()

dif = [0,0,0,0,0,0,0,0]
xdel, ydel = 0, 0
jouer = False
while jouer == False:
    i, xdel, ydel = choixDifficulte(dif,xdel,ydel)
    dif = modifTableChoix(dif,i)
    typeJeu, commencer, deuxJoueurs, jouer = difficulte(dif)
    dif[7] = 0  #réinitialise le bouton jouer
    

if deuxJoueurs == False:
    if typeJeu == 1:     #Imbattable
        niveau = -1
    elif typeJeu == 2:   #Difficile
        niveau = 5
    elif typeJeu == 3:   #Moyen
        niveau = 3
    elif typeJeu == 4:   #Facile
        niveau = 1
    elif typeJeu == 5:   #Random
        niveau = 0

    afficher(plateau)

    while len(caseVide(plateau)) > 0 and fini(plateau) == False:
        if commencer == False:
            plateau = tourOrdi(plateau, niveau)
            print("Ordinateur:")
            afficher(plateau)
            commencer = True
                
        plateau = tourHum1(plateau)
        afficher(plateau)
        if len(caseVide(plateau))> 0 and fini(plateau) == False:
            plateau = tourOrdi(plateau, niveau)
            print("Ordinateur:")
            afficher(plateau)



    affichageGagnant(plateau)
    if gagnant(plateau, ORDI) == ORDI:
        print("L'ordinateur a gagné.")
    elif gagnant(plateau, HUM1) == HUM1:
        print("L'humain a gagné.")
    else:
        print("Egalité.")
        
else:
    while len(caseVide(plateau)) > 0 and fini(plateau) == False:
        plateau = tourHum1(plateau)
        print("Humain n°1:")
        afficher(plateau)
        if len(caseVide(plateau)) > 0 and fini(plateau) == False:
            plateau = tourHum2(plateau)
            print("Humain n°2:")
            afficher(plateau)

    affichageGagnant(plateau)
    if gagnant(plateau, HUM1) == HUM1:
        print("L'humain n°1 a gagné")
    elif gagnant(plateau, HUM2):
        print("L'humain n°2 a gagné")
    else:
        print("Il y a égalité")
