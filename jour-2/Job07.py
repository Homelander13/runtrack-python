
chaine_base = "abcdefghijklmnopqrstuvwxyz" * 10


nb_lignes = 15


for i in range(1, nb_lignes *2, 2):
 
    partie_chaine = chaine_base[:i]


    print(partie_chaine.center(nb_lignes * 2 - 1))
