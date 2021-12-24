from PartieA import *
from PartieB import *
import turtle
import copy
from random import choice


# ---------- pour verifier l'animation enlever le # des 4 lignes suivants ----------
#loadwindo = turtle.Screen()
#turtle.setup(1400,1200)
#turtle.bgcolor("pink")
#turtle.title('Les tours de Hanoi')

def lire_coords(plateau):
    incorrect = True
    while incorrect :
        nm_tour_dep = int(input('Tour de départ: '))
        if nm_tour_dep == -1:
            return -1,-1

        L = len(plateau)
        if nm_tour_dep >=0 and nm_tour_dep<=2 and 0 < len(plateau[nm_tour_dep]):
            incorrect = False
            liste1 = list(plateau[nm_tour_dep])
            L_liste1 = len(liste1)

            nm_tour_arv = int(input("Tour d'arrivée: "))
            if nm_tour_arv == -1:
                return -1,-1

            if nm_tour_arv >= 0 and nm_tour_arv <= 2 :
                liste2 = list(plateau[nm_tour_arv])
                L_liste2 = len(liste2)

                if liste2 == []:
                    incorrect = False
                    print('je déplace le disque', liste1[L_liste1 - 1], 'de la tour', nm_tour_dep, 'à la tour',
                          nm_tour_arv)
                elif liste2[L_liste2-1] > liste1[L_liste1-1]:
                    incorrect = False
                    print('je déplace le disque',liste1[L_liste1 - 1],'de la tour',nm_tour_dep,'à la tour',nm_tour_arv)
                else:
                    incorrect = True
            else:
                incorrect = True
        else:
            incorrect = True
    
    return nm_tour_dep, nm_tour_arv

'''plateau = [[6,5,3,2],[7,4],[8,1]]
print(lire_coords(plateau))'''

def jouer_un_coup(plateau,n):
    liste = copy.deepcopy(plateau)  #pour modifier la lise plateau sur chaque coup
    dep,arv = lire_coords(plateau)
    if dep == -1 and arv == -1:  # cas d'abondon
        return -1, liste

    liste_dep = liste[dep]  #récuperation des listes de depart et d'arrivée
    liste_arv = liste[arv]

    disque = liste_dep[len(liste_dep)-1]  # sélection du disque qu'on va changer ça position
    efface_disque(disque,liste,n)  #on l'éfface du tour de depart
    disque = liste_dep.pop(len(liste_dep)-1)  # la nouvelle position dans la tour d'arrivée
    liste_arv.append(disque)

    dessine_disque(disque,liste,n)  # on le redessine dans ça position finale
    return '',liste
plateau = [[6,5],[4],[3,2,1]]
# on dessine le plateau d’abord.
'''dessine_plateau(6)
dessine_config(plateau,6)
print(jouer_un_coup(plateau,6))
turtle.exitonclick()'''

def boucle_jeu(plateau, n):
    victoire = verifier_victoire(plateau, n)

    ct_coup = 0  # compteur des coups au cas d'abondon
    while not (victoire):
        coup , plateau = jouer_un_coup(plateau, n)

        if coup == -1:  # cas d'abondon 2eme option
            confirmation = input('vous souhaitez abondonner (o/n) ? ')
            if confirmation == 'o':
                return ct_coup
        ct_coup += 1
        victoire = verifier_victoire(plateau,n)  # verification de la victoir

    return True

#programe principal

'''print('Bienvenue dans les Tours de Hanoi')
nm_disque = int(input('Combien de disques?'))
print('ramarque :')
print('vous pouvez abondonner à tout moment en entrant "-1" ')
print()
plateau = init(nm_disque)
dessine_plateau(nm_disque)  #dessin du plateau et des disque
dessine_config(plateau, nm_disque)
ct_coup = boucle_jeu(plateau,nm_disque)
if ct_coup != True:
    print('T.T')
    print('Abandon de la partie après', ct_coup, 'coups.')
    print('Au revoir')
else:
    print('Vous avez gagné!')
    print('Félicitation')

turtle.exitonclick()'''
