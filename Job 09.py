class Produit:
    def __init__(self, nom, prix_unitaire, quantite):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite

    def afficher_informations(self):
        print(f"Produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} €")
        print(f"Quantité en stock : {self.quantite}")

    def mettre_a_jour_prix(self):
        
        self.prix_unitaire *= 1.1



produit_initial = Produit("Ordinateur", 800, 10)


print("Informations initiales du produit :")
produit_initial.afficher_informations()


quantite_achat = int(input("Combien d'unités souhaitez-vous acheter ? "))


produit_initial.quantite -= quantite_achat


print("\nInformations après l'achat :")
produit_initial.afficher_informations()


produit_initial.mettre_a_jour_prix()


print("\nInformations après l'augmentation du prix :")
produit_initial.afficher_informations()
