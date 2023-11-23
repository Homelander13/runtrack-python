def compter_multiples_de_trois(liste):

    compte = 0
    

    for nombre in liste:

        if nombre % 3 == 0:
            compte += 1  

    return compte

L = [8, 24, 48, 9, 16]

resultat = compter_multiples_de_trois(L)
print("Le nombre de multiples de 3 dans la liste  :", resultat)