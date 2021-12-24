from PartieC import *
from PartieA import *
from PartieB import *
import datetime
from random import choice
import turtle
import time

# ---------- pour verifier l'animation enlever le # des 4 lignes suivants ----------
#loadwindo = turtle.Screen()
#turtle.setup(1400,1200)
#turtle.bgcolor("pink")
#turtle.title('Les tours de Hanoi')

def dernier_coup(coups, drn_c):
    tour_depart = None
    tour_arrivee = None
    for i in range(3):
        # si la tour de composition précédente est plus petite que la nouvelle
        # ça veut dire que cette tour est la tour d'arriver
        if len(coups[drn_c - 1][i]) < len(coups[drn_c][i]):
            tour_arrivee = i
        # si elle est plus grande donc c'est la tour de départ
        elif len(coups[drn_c-1][i]) > len(coups[drn_c][i]):
            tour_depart = i

    return tour_depart,tour_arrivee

#coups = {1 : [[3,2],[],[1]], 2:[[3],[2],[1]],3:[[3,2],[],[1]]}
#print(dernier_coup(coups,3))

def annuler_dernier_coup(coups, drn_c):
    # il faut inverser les coordonnées pour inverser le coups jouer

    nb_tour_arrivee , nb_tour_depart = dernier_coup(coups, drn_c)

    #après récuperer le numero de la tour
    # on récupere sa liste pour avoir le disque déplacer

    tour_arrivee = coups[drn_c][nb_tour_arrivee]
    tour_depart = coups[drn_c][nb_tour_depart]
    disque = tour_depart.pop(-1) # on l'enleve et on le remet dans la liste précédante
    tour_arrivee.append(disque)
    # supprission du dernier coup
    del coups[drn_c]
    # modification du numero du coups
    # on récupere la plus grande clé
    maxi_cle = 1
    for cle in coups:
        if cle > maxi_cle:
            maxi_cle = cle
    drn_c = maxi_cle

    return coups,drn_c  # test

#programme de test de la fonction 'annuler_dernier_coup(coups, drn_c)'
#coups ={1:[[3,2],[7,4,1],[6,5]], 2:[[3],[7,4,1],[6,5,2]],3:[[3],[7,4],[6,5,2,1]]}
#print(annuler_dernier_coup(coups,3))


def boucle_jeu2(plateau, n):
    victoire = verifier_victoire(plateau, n)
    # pour recuperer la duree de jeu on utilise la fonction time() du module time
    start_time = time.time()
    dictionnaire_coups = {0:plateau}

    ct_coup = 1  # compteur des coups au cas d'abondon
    while not (victoire):
        coup, plateau = jouer_un_coup(plateau, n)
        if coup != -1:
            dictionnaire_coups[ct_coup] = plateau

        elif coup == -1:  # cas d'abondon 2eme option
            confirmation = input('vous souhaitez abondonner ou annuler ? ')
            if confirmation == 'abondonner':
                return False, ct_coup-1 , 0
            else:
                efface_tout(dictionnaire_coups[max(dictionnaire_coups)],n)
                dictionnaire_coups, ct_coup = annuler_dernier_coup(dictionnaire_coups, max(dictionnaire_coups))
                #print(dictionnaire_coups) # test
                dessine_config(dictionnaire_coups[max(dictionnaire_coups)],n)
                plateau = dictionnaire_coups[max(dictionnaire_coups)]
        if coup !=-1:
            ct_coup = ct_coup + 1
        #print(plateau) # test
        victoire = verifier_victoire(plateau, n)  # verification de la victoir
    # on veut juste la partie entiere du temps
    duree = int((time.time() - start_time))
    return victoire ,ct_coup-1, duree

# Programme principal
'''print('Bienvenue dans les Tours de Hanoi')
nm_disque = int(input('Combien de disques?'))
print('ramarque :')
print('pour abondonner ou annuler un coup entrez: "-1" ')
plateau = init(nm_disque)
dessine_plateau(nm_disque)  #dessin du plateau et des disque
dessine_config(plateau, nm_disque)
ct_coup, duree = boucle_jeu2(plateau,nm_disque)
if ct_coup != True:
    print('T.T')
    print('Abondon de la partie après', ct_coup, 'coups.')
    print('Au revoir')
else:
    print('Vous avez gagné!')
    print('Félicitation')

turtle.exitonclick()'''
