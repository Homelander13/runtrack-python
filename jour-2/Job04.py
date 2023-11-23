

try:
  
    N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))

  
    if N > 0:
       
        for i in range(1, N+1):
            print(f"\nTable de multiplication de {i} :")
            for j in range(1, 11):
                resultat = i * j
                print(f"{i} x {j} = {resultat}")
    else:
        print("tie pas un monstre.")

except ValueError:
    print("Veuillez saisir un entier valide.")
