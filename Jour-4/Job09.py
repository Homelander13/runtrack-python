def recuperer_info_liste(liste):
    if not liste: 
        print("La liste est vide.")
        return None

    valeur = liste[0]  
    minimum = min(liste)
    maximum = max(liste)

    return valeur, minimum, maximum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = recuperer_info_liste(L)
print(" la valeur, le minimum et le maximum est :", resultat)
