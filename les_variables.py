# Job 4

for letter in range(ord('A'), ord('Z') + 1):
    print(chr(letter), end=" ")
print()

# Job 5
for letter in range(ord('Z'), ord('A') - 1, -1):
    print(chr(letter), end=" ")
print()

# Job 6
ma_string = "Je suis une String"
print(ma_string)

# Job 7
num1 = 40
num2 = 2
somme = num1 + num2
print("La somme de num1 et num2 est :", somme)

# Job 8
# Définition des variables
nom_produit = "Clavier Gaming"
prix_unitaire = 79.99
quantite_en_stock = 120

# Affichage des informations du produit de manière formatée
print(f"Produit : {nom_produit}")
print(f"Prix Unitaire : {prix_unitaire} EUR")
print(f"Quantité en Stock : {quantite_en_stock} unités")

# Ajout de produits en stock
quantite_ajoutee = int(input("Entrez la quantité de produits ajoutés en stock : "))
quantite_en_stock += quantite_ajoutee
print(f"Nouvelle Quantité en Stock : {quantite_en_stock} unités")

# Demande à l'utilisateur de saisir la quantité de produits qu’il souhaite acheter
quantite_achetee = int(input("Entrez la quantité de produits souhaitée pour l'achat : "))
if quantite_achetee <= quantite_en_stock:
    quantite_en_stock -= quantite_achetee
    print(f"Quantité restante en Stock après l'achat : {quantite_en_stock} unités")
else:
    print("Quantité insuffisante en stock")

# Ajustement du prix en fonction de l'inflation
prix_unitaire *= 1.10
print(f"Nouveau Prix Unitaire après inflation : {prix_unitaire:.2f} EUR")

# Affichage final des informations du produit de manière formatée
print("\nMise à jour des informations du produit :")
print(f"Produit : {nom_produit}")
print(f"Nouveau Prix Unitaire : {prix_unitaire:.2f} EUR")
print(f"Quantité en Stock : {quantite_en_stock} unités")

# Job 10
# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Calcul du gain annuel initial
gain_annuel_initial = montant_initial * (taux_rendement_annuel / 100)
print(f"Gain annuel initial : {gain_annuel_initial:.2f} EUR")

# Augmentation du capital de 5 000 euros et augmentation du taux de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Nouveau gain annuel après augmentation : {nouveau_gain_annuel:.2f} EUR")

# Retrait de 10% du montant total et diminution du taux de 1%
montant_apres_retrait = montant_initial * 0.9
taux_rendement_annuel -= 1

# Calcul du gain final après retrait
gain_final = montant_apres_retrait * (taux_rendement_annuel / 100)
print(f"Gain final après retrait : {gain_final:.2f} EUR")

# Job 11
# Demander à l'utilisateur de saisir une chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Vérifier si la chaîne contient le caractère 'e'
if 'e' in chaine:
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
