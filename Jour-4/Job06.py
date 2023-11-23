def echanger_premiere_derniere(liste):

    if len(liste) > 0:

        liste[0], liste[-1] = liste[-1], liste[0]
    else:
        print("La liste est vide.")


ma_liste = [1, 2, 3, 4, 5]


print(ma_liste)


echanger_premiere_derniere(ma_liste)


print( ma_liste)

print("et voila le travail !")
