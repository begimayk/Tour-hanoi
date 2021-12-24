import datetime
import os
import os.path
from PartieC import *
from PartieA import *
from PartieB import *
from PartieD import *
#os.remove('Les tours de Hanoi.txt') # pour reinitialiser le fichier à chaque test

def enregistrer(nom_joueur, nb_disques,nb_coups,duree):
    # verification de l'existance du fichier
    # initialisation du tableau ; avec leur longueurs pour bien trier les informations
    if not(os.path.exists('Les tours de Hanoi.txt')):
        fichier = open('Les tours de Hanoi.txt', 'w')
        fichier.write('Nom du joueur   ')
        fichier.write('Nombre de disques   ')
        fichier.write('Nombre de coups   ')
        fichier.write('La durée de la partie (secondes)' + '\n')
    else:
        fichier = open('Les tours de Hanoi.txt', 'a')
    # rajouter les informations
    # le nombre des espaces egal au nombre des espace occuper par le titre
    # moins celui du nom
    Lnj = len('Nom du joueur   ')
    Lnd = len('Nombre de disques   ')
    Lnc = len('Nombre de coups   ')

    espnj = ' ' * (Lnj - len(nom_joueur))
    espnd = ' ' * (Lnd - len(str(nb_disques)))
    espnc = ' ' * (Lnc - len(str(nb_coups)))

    fichier.write(nom_joueur + espnj)
    fichier.write(str(nb_disques) + espnd)
    fichier.write(str(nb_coups) + espnc)
    # récuperation du temps
    fichier.write(str(duree) + '\n')

    fichier.close()

# programme qui test
'''print(enregistrer('Emilia', 3, 8,145))
print(enregistrer('Abdessalem', 9, 550,546))
print(enregistrer('Ludovic',10,1040,345))
print(enregistrer('Sophie',6,65,120))'''
#fichier = open('Les tours de Hanoi.txt')
#partie = fichier.read()
#print(partie)

#3
def meilleur_score(nom_fichier):
    #ouverture de fichier
    fichier = open(nom_fichier)
    tableau = fichier.readlines() # recuperation des lignes de fichier

    # on récupere la liste des parties
    i = 0
    d = {}
    for ligne in tableau:
        if i != 0: # car quand i = 0 on prend la 1ère ligne (le titre du tableau)
            liste_partie = ligne.split()
            d[i] = liste_partie
        i = i + 1
    # on n'a plus besoin de fichier on le ferme
    fichier.close()

    # on veut récuperer le score + la ligne de la partie
    liste_score =[]
    for e in d:
        # depuis le résultat on peut obtenir les pourcentages des coups en fonction des nb des disques
        # la partie parfaite est de pourcentage 100%
        # plus de coups --> le pourcentage augmente --> une partie pire
        pourcentage = int(d[e][2]) * 100 / (2 ** int(d[e][1]) - 1)
        listex = [pourcentage, d[e]]
        liste_score.append(listex)

    # on recupere le dictionnaire des partie en format decroissante
    d_decroit = {}
    liste_score_copie = list(liste_score)
    for i in range(len(liste_score_copie)):
        #initialisation des pourcentages et la liste à afficher et la liste à suprrimer
        c = liste_score[0][0]
        liste_partie2 = liste_score[0][1]
        liste_pop = liste_score[0]
        for z in range(len(liste_score)):
            # plus que le pourcentage est petit plus que le score est meilleur
            if liste_score[z][0] < c:
                c = liste_score[z][0]
                liste_partie2 = liste_score[z][1]
                liste_pop = liste_score[z]
        liste_score.remove(liste_pop)
        d_decroit[i] = liste_partie2

    #affichage du tableau des résultat décroissante
    i = 1
    for key in d_decroit:
        print(i, end =' - ')
        for colonne in d_decroit[key]:
            print(colonne,end ='  ')
        print()
        i = i + 1
# test de la fonction meilleur_score
#print(meilleur_score('Les tours de Hanoi.txt'))

# Programme principal Partie E

'''print('Bienvenue dans les Tours de Hanoi')
nm_disque = int(input('Combien de disques?'))
print('ramarque :')
print('pour abondonner ou annuler un coup entrez: "-1" ')

# ouverture de la fenetre turtle
loadwindo = turtle.Screen()
turtle.setup(1400,1200)
turtle.bgcolor("pink")
turtle.title('Les tours de Hanoi')

plateau = init(nm_disque)
dessine_plateau(nm_disque)  #dessin du plateau et des disque
dessine_config(plateau, nm_disque)
victoire, ct_coup, duree = boucle_jeu2(plateau,nm_disque)

if victoire != True:
    print('T.T')
    print('Abondon de la partie après', ct_coup, 'coups.')
    print('Au revoir')
else:
    print('Vous avez gagné!')
    print('Félicitation')
    nom = input('entrez votre nom: ')
    print(enregistrer(nom,nm_disque,ct_coup,duree))
    print("C'est noté! Merci, Au revoir!")

fichier = open('Les tours de Hanoi.txt')
partie = fichier.read()
print(partie)'''

# prog prin E.3-4
#print(meilleur_score('Les tours de Hanoi.txt'))

def moyenne_temps(nom_fichier):
    fichier = open(nom_fichier)
    Parties = fichier.readlines() # recupération des lignes

    Parties_liste = []
    i = 0
    for ligne in Parties:
        if i != 0:
            liste = ligne.split()
            Parties_liste.append(liste)
        i = i + 1
    # mtn parties_liste est une liste des listes des parties

    for ligne in Parties_liste:
        ligne[3] = int(ligne[3])

    d = {}
    d_fois = {}
    for i in range(len(Parties_liste)):
        if Parties_liste[i][0] in d:
            d[Parties_liste[i][0]] = int(d[Parties_liste[i][0]]) + Parties_liste[i][3]
            d_fois[Parties_liste[i][0]] = d_fois[Parties_liste[i][0]] + 1
        else:
            d[Parties_liste[i][0]] = Parties_liste[i][3]
            d_fois[Parties_liste[i][0]] = 1
    # dictionnaire des moyennes
    d_moyenne = {}
    for joueur in d:
        d_moyenne[joueur] = d[joueur]/d_fois[joueur]

    #affichage des moyennes
    for joueur in d_moyenne:
        print('la duree moyenne par partie de',joueur,'est:',d_moyenne[joueur])

#test de la fonction qui calcule et affiche le temps moyen
#print(moyenne_temps('Les tours de Hanoi.txt'))

# une fonction qui classe les joueurs daprès leur duree de jeu
# elle ressemble dans sa structure à la fonction pmeilleur_score
def classement_duree(nom_fichier):
    # ouverture de fichier
    fichier = open(nom_fichier)
    tableau = fichier.readlines()  # recuperation des lignes de fichier

    # on récupere la liste des parties
    i = 0
    # on va creer un dictionnaire pour classer les joueurs
    Parties = {}
    for ligne in tableau:
        if i != 0:  # car quand i = 0 on prend la 1ère ligne (le titre du tableau)
            liste = ligne.split()
            Parties[i] = liste
        i = i + 1
    # on n'a plus besoin de fichier on le ferme
    fichier.close()

    # on veut un dictionnaire ou ces cles sont les durees et les valeurs sont les noms des joueurs
    joueur_duree = {}
    for i in Parties:
        joueur_duree[int(Parties[i][3])] = Parties[i][0]

    # on copie le dictionnaire joueur_duree parce qu'on va le modifier
    # pour avoir à chaque fois le minimum du dictionnaire.
    joueur_duree_copie = dict(joueur_duree)
    liste_triee = []
    for i in joueur_duree:
        # on utilise la fonction min() pour recuperer la duree la plus courte
        mini_duree = min(joueur_duree_copie)
        # listex est une liste de deux element: le nom et la duree
        listex = [joueur_duree[mini_duree],mini_duree]
        liste_triee.append(listex)
        # on supprime cette duree pour que on peut trouver la prochaine.
        del joueur_duree_copie[mini_duree]

    for i in range(1,len(liste_triee)+1):
        print(i,'.',liste_triee[i-1][0],'-',liste_triee[i-1][1],'secondes')

# test de la fonction classement_duree
#print(classement_duree('Les tours de Hanoi.txt'))