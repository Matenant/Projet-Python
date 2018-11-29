from math import inf
import random
import turtle as t

#clavier ou souris

ORDI = -1
HUM1 = 1
HUM2 = 2

#############################################
#############################################
#######            Affichage          #######
#############################################
#############################################

 
def grille():   #Affiche la grille
    t.hideturtle()
    t.speed(0)
    t.width(10)
    t.pencolor('black')
    t.penup()
    
    t.goto(-60,180)     #Va en haut du premier trait vertical
    t.right(90)         #se place à la verticale
    t.pendown()
    t.forward(360)      #Trace le trait
    t.penup()
    t.goto(60,180)      #Va en haut du deuxième trait vertical
    t.pendown()
    t.forward(360)      #Trace le trait
    t.penup()
    t.left(90)          #reprend l'angle initial
    t.goto(-180,60)     #Va tout à gauche du trait horizontale supérieur
    t.pendown()
    t.forward(360)      #Trace le trait
    t.penup()
    t.goto(-180,-60)    #Va tout à gauche du trait horizontale inférieur
    t.pendown()
    t.forward(360)      #Trace le trait
    t.penup()
    return

#############################################
#######       Choix difficultée       #######
#############################################
       
def texteChoixDifficulté(): #Mise en place du texte et des croix grises en dessous
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
    t.goto(-10,210)
    t.write("Jouer", font=(40))

    croixDiffGrey(-165,290) #Impossible
    croixDiffGrey(-74,290)  #Difficile
    croixDiffGrey(5,290)    #Moyen
    croixDiffGrey(83,290)   #Facile
    croixDiffGrey(160,290)  #Rand
    croixDiffGrey(-165,230) #Commencer
    croixDiffGrey(160,230)  #2 Joueurs
    return

def croixDiffGrey(x,y): #Créer les croix grises pour initialisation et réécriture
    Hyp=800**(1/2)  #Pythagore pour avoir la longueur des diagonales
    t.penup()
    t.speed(0)
    t.width(2)
    t.pencolor("#F5F5F5")   #gris très très clair
    
    t.goto(x,y)     #va au sommet gauche de la croix
    t.right(45)     #tourne de -45° (cercle trigonométrique)
    t.pendown()
    t.forward(Hyp)  #trace la première diagonal (de gauche à droite)
    t.penup()
    t.left(135)     #tourne de 135° (cercle trigonométrique) = 90° par rapport à 0
    t.forward(20)   #monte de 20px
    
    #est au sommet droit de la croix
    
    t.left(135)     #tourne de 135° (cercle trigonométrique) = 225° par rapport à 0
    t.pendown()
    t.forward(Hyp)  #trace la deuxième diagonal (de droite à gauxhe)
    t.penup()
    t.right(225)    #repend l'angle initiale soit 0°
    t.goto(x,y)     #reprend la position initial
    return

def conditionsDifficulte(table,i):  #retourne l'état des choix de difficultée
    if table[5] == 1:   #si veux commencer en premier
        if table[7] == 1:   #et que on clique sur "jouer"
            if table[6] == 1:   #mais que "2 joueurs" est coché
                return 0, False, False, False   #ne commence pas le jeu
            else:               #si "2 joueurs" pas coché
                return i, True, False, True     #commence le jeu avec la difficultée voulue, et le paramètre commencer
        else:               #mais si pas de clique sur "jouer"
            return 0, False, False, False   #sort de la fonction mais reste dans la boucle infinie
    else:               #si ne veux pas commencer
        if table[7] == 1:   #et que on clique sur "jouer"
            if table[6] == 1:   #mais que "2 joueurs" est coché
                return 0, False, False, False   #ne commence pas le jeu
            else:               #si "2 joueurs" pas coché
                return i, False, False, True    #commence le jeu avec la difficultée voulue, sans le paramètre commencer
        else:               #mais si pas de clique sur "jouer"
            return 0, False, False, False    #sort de la fonction mais reste dans la boucle infinie

def difficulte(table):  #élimine les choix de difficultée multiples
    i = 0   #tableau commence à 0
    tmp = -1    #il faux que ce soit différent de [0,5[
    while i != 4:    #parcours les 5 premiers éléments (difficultées)
        if table[i] == 1:   #quand rencontre un 1
            tmp = i         #sauvegarde l'index de la cellule
        if tmp != -1 and table[i+1] == 1:   #puis si tmp a été modifié et que 2 difficultées ont été cochées
            return 0, False, False, False   #sort de la fonction, mais reste dans la boucle infinie
        i = i +1
        
    if table[0] == 1:   #Impossible
        return conditionsDifficulte(table,1)
    elif table[1] == 1: #Difficile
        return conditionsDifficulte(table,2)
    elif table[2] == 1: #Moyen
        return conditionsDifficulte(table,3)
    elif table[3] == 1: #Facile
        return conditionsDifficulte(table,4)
    elif table[4] == 1: #Random
        return conditionsDifficulte(table,5)
    elif table[6] == 1: #2 joueur mais aucun autre mode de difficultée
        if table[7] == 1:   #si clique sur "jouer"
            if table[5] == 1:   #et veux commencer
                return 0, False, False, False   #sort de la fonction, mais reste dans la boucle infinis
                                                #pas besoin de dire qui commence, les joueurs doivent se mettre d'accord
            else:               #si veux pas commencer
                return 0, False, True, True     #commence le jeu entre les deux joueurs
    return 0, False, False, False   #si rien n'est coché, sort de la fonction, mais reste dans la boucle infinie
 

def choixDifficulte(tableauEtat):
    x, y = 400, 400         #Initialise x,y pour réaliser une boucle infinie
    t.onscreenclick(t.goto) #Va à l'emplacement du clique mais ne sauvegarde pas les coordonnées
    x,y = coordonnee(x,y)   #prend les coordonnée du clique
    
    #Test si les cliques sont sur les croix sinon sort, jusqu'à ce qu'un clique soit bon
    
    if y >= 270 and y <= 290:                   #1er ligne
        if x >= -165 and x <= -145:                 #Impossible
            if verifChoix(tableauEtat,0) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(-165,290)                
                return 1                    #retourne le mod de difficulté
            else:
                croixDiffGrey(-165,290)
                return -1                   #retourne l'inverse du mod de difficulté
        elif x >= -74 and x <= -54:                 #Difficile
            if verifChoix(tableauEtat,1) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(-74,290)
                return 2                    #retourne le mod de difficulté
            else:
                croixDiffGrey(-74,290)
                return -2                   #retourne l'inverse du mod de difficulté
        elif x >= 5 and x <= 25:                    #Moyen
            if verifChoix(tableauEtat,2) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(5,290)
                return 3                    #retourne le mod de difficulté
            else:
                croixDiffGrey(5,290)
                return -3                   #retourne l'inverse du mod de difficulté
        elif x >= 83 and x <= 103:                  #Facile
            if verifChoix(tableauEtat,3) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(83,290)
                return 4                    #retourne le mod de difficulté
            else:
                croixDiffGrey(83,290)
                return -4                   #retourne l'inverse du mod de difficulté
        elif x >= 160 and x <= 180:                 #Random
            if verifChoix(tableauEtat,4) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(160,290)
                return 5                    #retourne le mod de difficulté
            else:
                croixDiffGrey(160,290)
                return -5                   #retourne l'inverse du mod de difficulté
        else:                               
            return 0                        #si clique dans le vide, reste dans la boucle infinie
    elif y >= 210 and y <= 230:
        if x >= -165 and x <= -145:                 #Commencer
            if verifChoix(tableauEtat,5) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(-165,230)
                return 6                    #retourne le mod de difficulté
            else:
                croixDiffGrey(-165,230)
                return -6                   #retourne l'inverse du mod de difficulté
        elif x >= 160 and x <= 180:                 #2 Joueurs
            if verifChoix(tableauEtat,6) == True:       #Si la croix et grise, crée une croix noire
                croixDiffBlack(160,230)
                return 7                    #retourne le mod de difficulté
            else:
                croixDiffGrey(160,230)                  
                return -7                   #retourne l'inverse du mod de difficulté
        elif x >= -10 and x <= 20:                  #Jouer
            return 8                        #retourne la valeur assigner au clique sur jouer
    return 0    #sort de la fonction pour la re-exécuter dans la boucle infinie

def coordonnee(x,y):    #prend les coordonnée des cliques
    t.goto(x,y)     #va aux coordonnées du cliques
    x = t.xcor()    #x prend la valeur sur l'axe des abscisses
    y = t.ycor()    #y prend la valeur sur l'axe des ordonnées
    return x, y
   
def verifChoix(tableChoix,choix):   #regarde si la croix sur laquelle on clique et noir ou grise
    if tableChoix[choix] == 0:  #si gris retourne True sinon False
        return True
    else:
        return False
    
def croixDiffBlack(x,y):    #Créer les croix noires pour choix de difficulté et réécriture
    Hyp=800**(1/2)  #Pythagore pour avoir la longueur des diagonales
    t.penup()
    t.speed(0)
    t.width(2)
    t.pencolor("black")
    
    t.goto(x,y)     #va au sommet gauche de la croix
    t.right(45)     #tourne de -45° (cercle trigonométrique)
    t.pendown()
    t.forward(Hyp)  #trace la première diagonal (de gauche à droite)
    t.penup()
    t.left(135)     #tourne de 135° (cercle trigonométrique) = 90° par rapport à 0
    t.forward(20)   #monte de 20px
    
    #est au sommet droit de la croix
    
    t.left(135)     #tourne de 135° (cercle trigonométrique) = 225° par rapport à 0
    t.pendown()
    t.forward(Hyp)  #trace la deuxième diagonal (de droite à gauxhe)
    t.penup()
    t.right(225)    #repend l'angle initiale soit 0°
    t.goto(x,y)     #reprend la position initial
    return

#############################################
#######         Choix case Tour       #######
#############################################

def CliqueHumain(plateau, joueur):    #affiche une croix ou un rond en fonction du joueur humain
    x, y = 400, 400         #Initialise x,y pour réaliser une boucle infinie
    t.onscreenclick(t.goto) #Va à l'emplacement du clique mais ne sauvegarde pas les coordonnées
    x,y = coordonnee(x,y)   #prend les coordonnée du clique

    #Test si les cliques sont dans les cases de la grille sinon sort, jusqu'à ce qu'un clique soit bon

    # 0|1|2
    # ―――――
    # 3|4|5
    # ―――――
    # 6|7|8
    
    if x >= -180 and x <= -60: #1er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,0) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(-120,70)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-170,170)
                return 0, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 0, False     #sinon reste dans la boucle infinie
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,3) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(-120,-50)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-170,50)
                return 3, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 3, False     #sinon reste dans la boucle infinie
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,6) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(-120,-170)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-170,-70)
                return 6, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 6, False     #sinon reste dans la boucle infinie
    elif x >= -60 and x <= 60: #2er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,1) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(0,70)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-50,170)
                return 1, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 1, False     #sinon reste dans la boucle infinie
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,4) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(0,-50)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-50,50)
                return 4, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 4, False     #sinon reste dans la boucle infinie
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,7) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(0,-170)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(-50,-70)
                return 7, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 7, False     #sinon reste dans la boucle infinie
    elif x >= -60 and x <= 180: #3er colonne
        if y >= 60 and y <= 180: #1er ligne
            if verifCoup(plateau,2) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(120,70)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(70,170)
                return 2, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 2, False     #sinon reste dans la boucle infinie
        elif y >= -60 and y <= 60: #2er ligne
            if verifCoup(plateau,5) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(120,-50)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(70,50)
                return 5, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 5, False     #sinon reste dans la boucle infinie
        elif y >= -180 and y <= -60: #3er ligne
            if verifCoup(plateau,8) == True:    #J'intègre verifCoup pour que le joueur ne puisse pas écrire par dessus l'adversaire
                if joueur == 1:     #si un joueur ou alors si le premier joueur, affiche un rond
                    rond(120,-170)
                else:               #sinon, si 2 joueur et le tour de celui-ci, affiche une croix
                    croix(70,-70)
                return 8, True      #si la case est vide, retourne le numéro de la case, et True afin de sortir de la boucle infinie
            else:
                return 8, False     #sinon reste dans la boucle infinie
    else:
        return -1, False    #Si en dehors de la grille, ne retourne aucune case valide et reste dans la boucle infinie
    
def croix(x,y): #Trace les croix sur la grille
    Hyp=20000**(1/2)    #Pythagore pour avoir la longueur des diagonales
    t.penup()
    t.speed(0)
    t.width(5)
    t.pencolor("red")
    
    t.goto(x,y)         #va au sommet gauche de la croix
    t.right(45)         #tourne de -45° (cercle trigonométrique)
    t.pendown()
    t.forward(Hyp)      #trace la première diagonal (de gauche à droite)
    t.penup()
    t.left(135)         #tourne de 135° (cercle trigonométrique) = 90° par rapport à 0
    t.forward(100)      #monte de 100px

    #est au sommet droit de la croix
    
    t.left(135)         #tourne de 135° (cercle trigonométrique) = 225° par rapport à 0
    t.pendown()
    t.forward(Hyp)      #trace la deuxième diagonal (de droite à gauxhe)
    t.penup()
    t.right(225)        #repend l'angle initiale soit 0°
    t.goto(x,y)         #reprend la position initial
    return

def rond(x,y):  #Trace les ronds sur la grille
    t.penup()
    t.speed(0)
    t.width(5)
    t.pencolor("blue")
    
    t.goto(x,y)     #va en bas du futur cercle, mais reste centré
    t.pendown()
    t.circle(50)    #trace un cercle de rayon 50px
    t.penup()
    return

def CroixOrdi(x):  #Trace les croix du tour ordi

    # 0|1|2
    # ―――――
    # 3|4|5
    # ―――――
    # 6|7|8
        
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
        
#############################################
#######       Affichage gagnant       #######
#############################################
        
def affichageGagnant(plateau):  #Affiche les barres de victoires quand celle ci a lieu
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
    elif plateau[0]==plateau[4] and plateau[4]==plateau[8] and plateau[4] != 0: #diagonale coin supérieur Gauche - diagonale coin inférieur Droit
        barreDiaGD(-180,180)
        return 
    elif plateau[2]==plateau[4] and plateau[4]==plateau[6] and plateau[4] != 0: #diagonale coin supérieur Droit - diagonale coin inférieur Gauche
        barreDiaDG(180,180)
        return
    else:
        return

def barreHori(x,y): #Affiche les barres de victoire dans le cas horizontale
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)     #ce centre verticalement et ce place le plus a gauche sur la ligne où victoire est
    t.pendown()
    t.forward(360)  #Trace un trait horizontale le long de la ligne
    t.penup()
    t.goto(x,y)     #Se repositionne au début
    return
    
def barreVerti(x,y): #Affiche les barres de victoire dans le cas verticale
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)     #ce centre horizontalement et ce place le plus en haut sur la colonne où victoire est
    t.right(90)     #Tourne pour se mettre à la verticale
    t.pendown()
    t.forward(360)  #Trace un trait verticale le long de la ligne
    t.penup()
    t.left(90)      #retourne à l'angle de base
    t.goto(x,y)     #Se repositionne au début
    return
    
def barreDiaGD(x,y): #Affiche les barres de victoire dans le cas d'une victoire diagonale commençant dans le coin supérieur gauche
    Hyp=259200**(1/2)    #Pythagore pour avoir la longueur des diagonales
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)     #place sur le coin supérieur gauche de la grille si victoire est
    t.right(45)     #tourne de -45° (cercle trigonométrique)
    t.pendown()
    t.forward(Hyp)  #trace la diagonale complète
    t.penup()
    t.left(45)      #retourne à l'angle de base
    t.goto(x,y)     #Se repositionne au début
    return
    
def barreDiaDG(x,y): #Affiche les barres de victoire dans le cas d'une victoire diagonale commençant dans le coin supérieur droit
    Hyp=259200**(1/2)    #Pythagore pour avoir la longueur des diagonales
    t.speed(0)
    t.width(5)
    t.pencolor('green')
    
    t.goto(x,y)     #place sur le coin supérieur droit de la grille si victoire est
    t.right(135)    #tourne de 225° (cercle trigonométrique)
    t.pendown()
    t.forward(Hyp)  #trace la diagonale complète
    t.penup()
    t.left(135)     #retourne à l'angle de base
    t.goto(x,y)     #Se repositionne au début
    return

#############################################
#############################################
#######         Algorithmique         #######
#############################################
#############################################

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

# 0|1|2
# ―――――
# 3|4|5
# ―――――
# 6|7|8

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
		
def tourHum1(plateau):                      
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:
        return plateau
    coup = -1
    verif = False
    while verif == False:   #Boucle infinie, sort si le coup est vérifié (dans la fonction clique)
        coup, verif = CliqueHumain(plateau, 1)    #"Attend" un clique de l'utilisateur
    plateau[coup] = 1
    return plateau

def tourHum2(plateau):
    profondeur = len(caseVide(plateau))
    if profondeur == 0 or fini(plateau) == True:
        return plateau
    coup = -1
    verif = False
    while verif == False:   #Boucle infinie, sort si le coup est vérifié (dans la fonction clique)
        coup, verif = CliqueHumain(plateau, 2)    #"Attend" un clique de l'utilisateur
    plateau[coup] = 2
    return plateau

def tourOrdi(plateau, niveau):
    profondeur = len(caseVide(plateau))
    if niveau == -1:
        niveau = profondeur
    if profondeur == 9 or niveau == 0:
        verif = False
        while verif == False:
            coup = random.randint(0,8)
            verif = verifCoup(plateau, coup)    
        CroixOrdi(coup) #affiche la croix une fois que l'ordinateur a joué son premier coup
        plateau[coup] = -1
        return plateau
    else:
        coup = minimax(plateau, niveau, ORDI)
        caseCoup = coup[0]
    CroixOrdi(caseCoup) #affiche la croix une fois que l'ordinateur a joué
    plateau[caseCoup] = -1
    return plateau

def modifTableChoix(table,i):   #modifie le tableau des choix de difficultée
    if i == 0:      #si rien ne change, rien n'est fait
        return table
    elif i > 0:     #si une croix grise devient noir, donne la valeur 1 à la case correspondante du tableau
        table[i-1] = 1
        return table
    elif i == -1:   #si Impossible devient gris, la case correspondante se réinitialise
        table[0] = 0
        return table
    elif i == -2:   #si Difficile devient gris, la case correspondante se réinitialise
        table[1] = 0
        return table
    elif i == -3:   #si Moyen devient gris, la case correspondante se réinitialise
        table[2] = 0
        return table
    elif i == -4:   #si Facile devient gris, la case correspondante se réinitialise
        table[3] = 0
        return table
    elif i == -5:   #si Random devient gris, la case correspondante se réinitialise
        table[4] = 0
        return table
    elif i == -6:   #si Commencer devient gris, la case correspondante se réinitialise
        table[5] = 0
        return table
    elif i == -7:   #si 2 Joueurs devient gris, la case correspondante se réinitialise
        table[6] = 0
        return table
               
        
		
plateau = [0, 0, 0, 0, 0, 0, 0, 0, 0]

t.title("Morpion 1.4.52")   #Titre
texteChoixDifficulté()      #Affiche texte/croix pour choix difficulté
grille()                    #La grille du morpion

dif = [0,0,0,0,0,0,0,0] #initialise le tableau de choix de difficultée
jouer = False           #initialise la variable de sortie de boucle
while jouer == False:   #boucle infinie, sort une foi qu'il n'y a qu'un mode de difficultée sélectionner
    i = choixDifficulte(dif)    #demande un clique sur les croix pour choisir le mode de difficultée
    dif = modifTableChoix(dif,i)    #modifie le tableau en fonction du choix
    typeJeu, commencer, deuxJoueurs, jouer = difficulte(dif)    #la difficultée, veux commencer ou non, 2 joueurs ou non, clique sur jouer ou non
    dif[7] = 0  #réinitialise le bouton jouer
                #important si clique sur "jouer" alors que plusieurs modes de difficultée
    

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
