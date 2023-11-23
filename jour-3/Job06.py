def verifier_positif_negatif_nul(nombre):
    if nombre > 0:
        print(f"{nombre} est positif")
    elif nombre < 0:
        print(f"{nombre} est négatif")
    else:
        print(f"{nombre} est nul")


verifier_positif_negatif_nul(5)
verifier_positif_negatif_nul(-3)
verifier_positif_negatif_nul(0)
verifier_positif_negatif_nul(10)
verifier_positif_negatif_nul(-7)
