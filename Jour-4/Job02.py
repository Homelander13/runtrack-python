def deuxieme_fruits():
    fruits = ["pomme", "cerise", "orange"]

    
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print("Le deuxième fruits de la liste est:", deuxieme_element)
    else:
        print("La liste ne contient pas suffisamment d'éléments.")

deuxieme_fruits()
