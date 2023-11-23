def supprimer_doublons(liste):
    i = 0
    n = longueur_liste_recursive(liste)  
    while i < n:
        j = i + 1
        while j < n:
           
            if liste[i] == liste[j]:
                del liste[j]
                n -= 1 
            else:
                j += 1
        i += 1


def longueur_liste_recursive(liste):

    if not liste:
        return 0
   
    else:
        return 1 + longueur_liste_recursive(liste[1:])


ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


print("Liste initiale :", ma_liste)


supprimer_doublons(ma_liste)


print("Liste sans doublons :", ma_liste)
