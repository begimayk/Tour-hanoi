# question 1
def init(n):
    # Initialisation des listes
    plateau = []
    source = []
    auxiliary = []
    destination =[]
    for i in range(n,0,-1):
        # i prend les valeurs de n inclus jusqu'à 1 inclus
        source.append(i)

    plateau.append(source)
    plateau.append(auxiliary)
    plateau.append(destination)
    return plateau

#print(init(3))

# question 2
def nombre_disques(plateau,numtour):
    plateau_copie = list(plateau)  # pour ne pas modifier la liste plateau
    liste_numtour = plateau_copie.pop(numtour)  # On prend la liste d'indice numtour, appelons la plateau_copie
    nb_dis_tour = len(liste_numtour)  #La longueur de cette liste est le nombre de disque sur cette tour
    return nb_dis_tour

#plateau = init(3)
#print(nombre_disques(plateau , 0 ))


# question 3
def disque_superieur(plateau, numtour):
    plateau_copie = list(plateau)
    liste_numtour = plateau_copie.pop(numtour)
    if len(liste_numtour)!=0:  # verification si la liste est vide ou nn.
        superieur = liste_numtour[0]  # parce que le disque de l'indice 0 est le plus grands toujours.
        return superieur
    return -1
#print(disque_superieur(plateau,0))

# question 4
def position_disque(plateau,numdisque):
    for e in range(3):  # boucle pour verifie les listes des indices: 0, 1 et 2
        liste = plateau[e]
        for i in range(len(liste)):  # boucle pour verifie tout les éléments de la liste d'indice e
            if liste[i] == numdisque:
                position = e  # récuperation du numero de la tour si on trouve le disque
    return position

#plateau = [[12,11,10],[8,7,6],[5,4,3,2,1]]
#print(position_disque(plateau,5))

# question 5
def verifier_deplacement(plateau, nt1 , nt2):
    # on utilise la fonction nombre_disque pour verifier s'il y en a des disques dans la tour nt1
    # on utilise la fonction disque_superieur pour verifie que le disque superieur de la tour nt1 est inferieur au
    # disque le plus petit dans la tour nt2
    plateau_copie = list(plateau)
    liste_nt2 = plateau_copie.pop(nt2)
    disque_petit = liste_nt2[len(liste_nt2)-1]  # on récupere le disque le plus petit dans la liste nt2
    return (nombre_disques(plateau,nt1)!= 0) and (disque_petit > disque_superieur(plateau,nt1))

#print(verifier_deplacement(plateau,1,0))

# question 6
def verifier_victoire(plateau,n):
    plateau_copie = list(plateau)
    destination = plateau_copie.pop()  # signifie la derniere liste dans la liste des listes, plateau.
    resultat = True
    if len(destination) == n:
        for e in range(0,n-1):
            if destination[e] < destination[e+1]:  # verification de la décroissance
                resultat = False
    else:
        resultat = False
    return resultat

'''plateau = [[],[],[12,11,10,9,8,7,6,5,4,3,2,1]]
print(verifier_victoire(plateau,12))
plateau2 = [[],[2],[12,11,10,9,8,7,6,5,4,3,1]]
print(verifier_victoire(plateau2,12))'''