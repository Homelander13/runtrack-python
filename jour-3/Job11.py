def time_to_text(minutes):
   
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60  
        minutes_restantes = minutes % 60  

        if heures == 0:
            resultat = f"{minutes} minutes"
        elif heures == 1:
            resultat = f"{heures} heure et {minutes_restantes} minutes"
        else:
            resultat = f"{heures} heures et {minutes_restantes} minutes"

        # Afficher le résultat
        print(resultat)
    else:
        print("Veuillez entrer un nombre entier positif.")


time_to_text(-160)
time_to_text(634)
time_to_text(45)
time_to_text(-30)  
time_to_text(90.5)  
