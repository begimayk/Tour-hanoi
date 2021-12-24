from PartieA import *
from PartieB import *
import copy
import turtle
# creation de la
def hanoi(n, source = 0, auxiliary = 1, destination = 2, deplacements=[]):
    if n > 0:
        # recursivement deplace la tour des n-1 disques à l'auxiliary
        hanoi(n - 1, source, destination, auxiliary,deplacements)
        #print([source,destination])
        # ajoute ce deplacement à la liste des deplacements
        deplacements.append([source,destination])
        hanoi(n - 1, auxiliary, source, destination,deplacements)
    return deplacements


# rendre la foction jouer_un_coup automatique
def jouer_un_coup_auto(plateau, n, i, j): # où i et j sont les coordonnées de la liste 'deplacements'
    liste = copy.deepcopy(plateau)  #pour modifier la lise plateau sur chaque coup

    liste_dep = liste[i]  #récuperation des listes de depart et d'arrivée
    liste_arv = liste[j]

    disque = liste_dep[len(liste_dep)-1]  # sélection du disque qu'on va changer ça position
    efface_disque(disque,liste,n)  #on l'éfface du tour de depart
    disque = liste_dep.pop(len(liste_dep)-1)  # la nouvelle position dans la tour d'arrivée
    liste_arv.append(disque)

    dessine_disque(disque,liste,n)  # on le redessine dans ça position finale
    return liste


def solution_Tour_de_Hanoi(plateau,n):
    deplacements = hanoi(n)
    L = len(deplacements)
    # préparation du dessin de la base (plateau avec la configuration initial)
    dessine_plateau(n)
    dessine_config(plateau,n)
    for e in range(L):
        # jeu automatique
        plateau = jouer_un_coup_auto(plateau,n,deplacements[e][0],deplacements[e][1])


#programme principal
n = int(input('entre le nombre des disques: '))
# creation du plateau
plateau = init(n)

loadwindo = turtle.Screen()
turtle.setup(1400,1200)
turtle.bgcolor("pink")
turtle.title('Les tours de Hanoi')

solution_Tour_de_Hanoi(plateau,n)

turtle.exitonclick()