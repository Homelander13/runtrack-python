def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur :  La Division par zéro ne fonctionne pas"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur :La Division par zéro ne fonctionne pas"
    else:
        return "Désoler l'Opérateur que vous avez entrer n'a pas été reconnu"
    
  
resultat1 = calcule(5, '+', 3)
resultat2 = calcule(10, '*', 2)
resultat3 = calcule(8, '/', 4)


print("Résultat 1 :", resultat1)
print("Résultat 2 :", resultat2)
print("Résultat 3 :", resultat3)