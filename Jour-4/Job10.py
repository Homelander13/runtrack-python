def calculer_produit_intervalle(liste, borne_inf, borne_sup):
    produit = 1

    for nombre in liste:
        if borne_inf <= nombre <= borne_sup:
            produit *= nombre

    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


borne_inf = 25
borne_sup = 90


resultat = calculer_produit_intervalle(L, borne_inf, borne_sup)
print(f"Le produit des valeurs comprises entre {borne_inf} et {borne_sup} est :", resultat)
