
montant_initial = 20000  
taux_rendement_annuel = 8  


gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Le gain annuel initial est de {gain_annuel} euros.")


montant_initial += 7000
taux_rendement_annuel += 3

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Après l'augmentation du capital et du taux, le nouveau gain annuel est de {nouveau_gain_annuel} euros.")


retrait = 0.15 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 2


montant_final = montant_initial + nouveau_gain_annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_final
print(f"Après le retrait et la diminution du rendement, le montant final de l'investissement est de {montant_final} euros.")
print(f"Le nouveau gain annuel est de {nouveau_gain_annuel} euros.")
