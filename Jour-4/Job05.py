def main():
    # Création de la liste d'au moins 5 entiers
    L = [1, 2, 3, 4, 5]

    print(L)


    print( L[1])

    
    remplacer_par_somme_voisins(L)


    print(L)

    print(L[-1])

def remplacer_par_somme_voisins(liste):
 
    if len(liste) >= 5:
      
        somme_voisins = liste[2] + liste[4]
        

        liste[3] = somme_voisins
    else:
        print("La liste ne contient pas suffisamment d'éléments.")


main()
