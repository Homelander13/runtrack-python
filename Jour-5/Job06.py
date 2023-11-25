def distance_pour_faire_caca(marches, hauteur_marche):
    hauteur_totale = marches * hauteur_marche * 2  
    distance_m_par_jour = hauteur_totale / 100  
    distance_m_par_semaine = distance_m_par_jour * 7  

    print(f'Pour {marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_m_par_semaine:.2f} m par semaines.')


distance_pour_faire_caca(15, 30)
