def tri_a_bulles_recursif(liste, n=0, taille=None):
    if taille is None:
        taille = 0
        while True:
            try:
                _ = liste[taille]
                taille += 1
            except IndexError:
                break
    if n == taille - 1:
        return liste
    if liste[n] > liste[n + 1]:
        liste[n], liste[n + 1] = liste[n + 1], liste[n]
        return tri_a_bulles_recursif(liste, 0, taille)
    else:
        return tri_a_bulles_recursif(liste, n + 1, taille)

# Test du programme
print(tri_a_bulles_recursif([4, 3, 2, 1]))
