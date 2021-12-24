# question 1
# on veut definir d'abord une fonction qui déssine un disque.
import turtle
from random import choice

# ---------- pour verifier l'animation enlever le # des 4 lignes suivants ----------
#loadwindo = turtle.Screen()
#turtle.setup(1400,1200)
#turtle.bgcolor("pink")
#turtle.title('Les tours de Hanoi')

def disque(L,M): # elle prend en arqument la longueur et la lageur
    i = 0
    liste_color = ["salmon","plum","red", "purple", "aqua","blue","orange","beige","gold" ,"green","yellow", "coral", "light green",
                   "violet", "lime"]
    color = choice(liste_color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    while i <4:
        if i % 2 == 0:
            turtle.speed("fastest")  # pour les dessiner le plus rapide possible.
            turtle.forward(L)
            turtle.right(90)
        else:
            turtle.speed("fastest")
            turtle.forward(M)
            turtle.right(90)
        i = i + 1
    turtle.end_fill()


def white_disque(L,M):
    i = 0
    while i < 4:
        if i % 2 == 0:
            turtle.speed("fastest")  # pour les dessiner le plus rapide possible.
            turtle.forward(L)
            turtle.right(90)
        else:
            turtle.speed("fastest")
            turtle.forward(M)
            turtle.right(90)
        i = i + 1


def dessine_plateau(n):
    # positionnement du plateau en (-300,-200)
    turtle.up()
    turtle.goto(-450,-200)
    turtle.down()
    turtle.fillcolor("tan")
    turtle.begin_fill()
    # La base du plateau
    L_disque = 40 + 30*(n-1)  # le disque le plus petit 40 et à chaque disque on rajoute 30 à chaque fois
    epaisseur = 20
    L_plateau = 3 * L_disque + 4 * 20  # 3 fois la longueur du disque le plus grand plus 4 fois l'espace de 20
    white_disque(L_plateau,epaisseur)

    # maintenant les tours
    # la premiere tour
    turtle.forward(20 + L_disque/2 - 3)  # un espace de 20 + la moitie de la longueur du disque le plus grand -
    # la moitie de l'epaisseur de la tour

    # dessin de la premiere tour
    turtle.left(90)
    white_disque(20*n + 20 , 6)
    turtle.right(90)

    turtle.up()
    turtle.goto(-450, -200)
    turtle.down()

    #les deux tours restantes ont le meme décalage donc on utilise la boucle for
    for i in range(1,3):
        turtle.forward(20 * (2+i-1) + i*(L_disque) + L_disque/2 - (3/2)*(i+1))  # positionnement des tours
        turtle.left(90)
        white_disque(20 * n + 20,6)
        turtle.right(90)
        turtle.up()
        turtle.goto(-450, -200)
        turtle.down()
    turtle.end_fill()
    #positionnement de la fleche au point de depart
    turtle.up()
    turtle.goto(-450, -180)
    turtle.down()


# on utilise la fonction définie dans la partie A pour definir sa position
def position_disque(plateau,numdisque):
    position = 0
    for e in range(3):  # boucle pour verifie les listes des indices: 0, 1 et 2
        liste = list(plateau[e])
        L = len(liste)
        for i in range(L):  # boucle pour verifie tout les éléments de la liste d'indice e
            if liste[i] == numdisque:
                position = e  # récuperation du numero de la tour si on trouve le disque
    return position

def dessine_disque(nd,plateau,n):
        L_disque = 40 + 30*(n-1)
        plateau_copie = list(plateau)  # pour ne pas perdre la liste plateau

        if position_disque(plateau_copie,nd) == 0:
            turtle.up()
            turtle.forward(20)
            turtle.down()
            liste = plateau_copie.pop(0)
        elif position_disque(plateau_copie,nd) == 1:
            turtle.up()
            turtle.forward(20 * 2 + L_disque )
            turtle.down()
            liste = plateau_copie.pop(1)
        else:
            turtle.up()
            turtle.forward(20 * 3 + 2 * L_disque - 1)
            turtle.down()
            liste = plateau_copie.pop(2)

        i = 0
        while i < len(liste):
            if liste[i] == nd:
                turtle.up()
                turtle.left(90)
                turtle.forward(20*i)
                turtle.right(90)
                turtle.forward(15*(n-nd))
                turtle.down()
                L_disque = 40 + 30*(nd-1)
                disque(L_disque,20)
            i = i + 1

        turtle.up()
        turtle.goto(-450, -180)
        turtle.down()


def efface_disque(nd,plateau,n):
    L_disque = 40 + 30 * (n-1)
    plateau_copie = list(plateau)
    if position_disque(plateau_copie, nd) == 0:
        turtle.up()
        turtle.forward(20)
        turtle.down()
        liste = plateau_copie.pop(0)
    elif position_disque(plateau_copie, nd) == 1:
        turtle.up()
        turtle.forward(20 * 2 + L_disque)
        turtle.down()
        liste = plateau_copie.pop(1)
    else:
        turtle.up()
        turtle.forward(20 * 3 + 2 * L_disque - 1)
        turtle.down()
        liste = plateau_copie.pop(2)

    i = 0
    while i < len(liste):
        if liste[i] == nd:
            turtle.up()
            turtle.left(90)
            turtle.forward(20 * i)
            turtle.right(90)
            turtle.forward(15 * (n-nd))
            turtle.down()
            L_disque = 40 + 30 * (nd - 1)
            #partie couleur
            turtle.pencolor("pink")
            turtle.fillcolor("pink")
            turtle.begin_fill()
            white_disque(L_disque, 20)
            turtle.end_fill()
            turtle.pencolor('black')
        i = i + 1
    dessine_plateau(n)

    j = 1
    while j <= n:
        if j == nd:
            j = j + 1
        plateau_copie = plateau
        dessine_disque(j,plateau_copie,n)
        j = j + 1
    turtle.up()
    turtle.goto(-450, -180)
    turtle.down()


def efface_disque2(nd, plateau, n):
    L_disque = 40 + 30 * (n - 1)
    plateau_copie = list(plateau)
    if position_disque(plateau_copie, nd) == 0:
        turtle.up()
        turtle.forward(20)
        turtle.down()
        liste = plateau_copie.pop(0)
    elif position_disque(plateau_copie, nd) == 1:
        turtle.up()
        turtle.forward(20 * 2 + L_disque)
        turtle.down()
        liste = plateau_copie.pop(1)
    else:
        turtle.up()
        turtle.forward(20 * 3 + 2 * L_disque - 1)
        turtle.down()
        liste = plateau_copie.pop(2)

    i = 0
    while i < len(liste):
        if liste[i] == nd:
            turtle.up()
            turtle.left(90)
            turtle.forward(20 * i)
            turtle.right(90)
            turtle.forward(15 * (n - nd))
            turtle.down()
            L_disque = 40 + 30 * (nd - 1)
            turtle.pencolor("pink")
            turtle.fillcolor("pink")
            turtle.begin_fill()
            white_disque(L_disque, 20)
            turtle.end_fill()
            turtle.pencolor('black')
        i = i + 1
    dessine_plateau(n)

    turtle.up()
    turtle.goto(-450, -180)
    turtle.down()
# Programme principal
# verification des fonctions dessine_plateau, dessine_disque et efface_disque
'''plateau = [[10], [9, 8, 7, 6], [5, 4, 3, 2, 1]]
dessine_plateau(10)
for i in range(10,0,-1):
    dessine_disque(i,plateau,10)
efface_disque(1,plateau,10)'''

def dessine_config(plateau,n):
    turtle.up()
    turtle.goto(-450, -180)
    turtle.down()
    for i in range(n,0,-1):

        dessine_disque(i,plateau,n)

# programme de test
'''plateau = [[12,11,10,9,8,7,6,5,4,3,2,1],[],[]]
dessine_plateau(12)
dessine_config(plateau,12)'''

def efface_tout(plateau,n):
    turtle.up()
    turtle.goto(-450, -180)
    turtle.down()
    for i in range(1, n+1):

        efface_disque2(i, plateau, n)

# programme de test
#plateau = [[7,4,3,2],[10,9,5],[8,6,1]]
#dessine_plateau(10)
#dessine_config(plateau,10)
#efface_tout(plateau,10)

#turtle.exitonclick()




