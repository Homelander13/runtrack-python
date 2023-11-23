def my_long_word(taille_minimale, phrase):
    i = 0
    resultat = ""

    while i < longueur_liste_recursive(phrase.split()):
        mot = phrase.split()[i]

        if longueur_chaine_recursive(mot) > taille_minimale:
            if i == 0:
                resultat += mot
            else:
                resultat += " " + mot

        i += 1

    return resultat

# Fonction récursive pour calculer la longueur d'une liste
def longueur_liste_recursive(liste):
    # Cas de base : une liste vide a une longueur de 0
    if not liste:
        return 0
    # Cas récursif : la longueur est de 1 plus la longueur du reste de la liste
    else:
        return 1 + longueur_liste_recursive(liste[1:])

# Fonction récursive pour calculer la longueur d'une chaîne de caractères
def longueur_chaine_recursive(chaine):
    # Cas de base : une chaîne vide a une longueur de 0
    if not chaine:
        return 0
    # Cas récursif : la longueur est de 1 plus la longueur du reste de la chaîne
    else:
        return 1 + longueur_chaine_recursive(chaine[1:])

# Exemple d'utilisation
taille_minimale = 3
phrase = "Ce que l'on fait dans une bonne intention est toujours  profitable"

# Appel de la fonction et affichage du résultat
resultat = my_long_word(taille_minimale, phrase)
print("Output :", resultat)
