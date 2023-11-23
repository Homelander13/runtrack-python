def somme_valeurs_paires(liste):
    somme = 0
    
    for nombre in liste:
    
        if nombre % 2 == 0:
            somme += nombre  

    return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]


resultat = somme_valeurs_paires(L)
print(resultat)
