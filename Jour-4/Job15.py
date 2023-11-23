def tri_et_arrondi_liste(liste):
    # Arrondir les nombres dans la liste
    i = 0
    while i < longueur_liste_recursive(liste):
        liste[i] = arrondir_nombre(liste[i])
        i += 1

    # Trier la liste dans l'ordre croissant avec l'algorithme de tri à bulles
    n = longueur_liste_recursive(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échanger les éléments si nécessaire
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

# Fonction récursive pour calculer la longueur d'une liste
def longueur_liste_recursive(liste):
    # Cas de base : une liste vide a une longueur de 0
    if not liste:
        return 0
    # Cas récursif : la longueur est de 1 plus la longueur du reste de la liste
    else:
        return 1 + longueur_liste_recursive(liste[1:])

# Fonction récursive pour arrondir un nombre
def arrondir_nombre(nombre):
    entier = int(nombre)
    decimal = nombre - entier

    if decimal >= 0.5:
        return entier + 1
    else:
        return entier

# Fonction pour afficher la liste en ordre croissant
def afficher_liste_croissante(liste):
    i = 0
    while i < longueur_liste_recursive(liste):
        print(liste[i], end=" ")
        i += 1
    print()

# Exemple d'utilisation
ma_liste = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

# Affichage de la liste initiale
print("Liste initiale :", ma_liste)

# Appel de la fonction pour trier et arrondir la liste
tri_et_arrondi_liste(ma_liste)

# Affichage de la liste triée et arrondie en ordre croissant
print("Liste triée et arrondie (ordre croissant) : ", end="")
afficher_liste_croissante(ma_liste)
