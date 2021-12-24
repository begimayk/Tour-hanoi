from PartieA import *
from PartieB import *
from PartieC import *
from PartieD import *
from PartieE import *
import turtle

print('Bienvenue dans les Tours de Hanoi')
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
    print('voulez vous voir le classemnt (oui/non) ?')
    reponse = input()
    if reponse == 'oui':
        print('1 - classement par les scores')
        print('2 - classement par les durees')
        print('3 - Les deux')
        rep2 = int(input('1, 2 ou 3? '))
        if rep2 == 1:
            meilleur_score('Les tours de Hanoi.txt')
        elif rep2 == 2:
            classement_duree('Les tours de Hanoi.txt')
        else:
            print('classement par score : ')
            meilleur_score('Les tours de Hanoi.txt')
            print()
            print('classement par duree:')
            classement_duree('Les tours de Hanoi.txt')
    print("Merci, Au revoir!")

# si vous voulez les moyennes des durees.
#print(moyenne_temps('Les tours de Hanoi.txt'))