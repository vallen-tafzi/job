# Job 1
for number in range(21):  # Parcourt les nombres de 0 à 20
    print(number)  # Affiche chaque nombre

# Job 2
for number in range(0, 21, 2):  # Parcourt les nombres de 0 à 20 avec un pas de 2
    print(number)  # Affiche chaque nombre

# Job 3
for number in range(1, 21):  # Parcourt les chiffres de 1 à 20
    carre = number ** 2  # Calcule le carré du nombre
    print(f"Le carré de {number} est {carre}")  # Affiche le résultat

# Job 4
# Demande à l'utilisateur de saisir la valeur de N
N = int(input("Saisissez un entier supérieur à zéro pour N : "))

if N <= 0:
    print("Veuillez saisir un entier supérieur à zéro.")
else:
    # Parcourt chaque nombre de 1 à N
    for i in range(1, N + 1):
        print(f"\nTable de multiplication pour {i} :")
        # Affiche la table de multiplication pour chaque nombre
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

# Job 5
for N in range(1, 13):
    print(N)

N = 1  # Initialisation de la variable N
while N < 13:  # Condition de boucle pour parcourir de 1 à 12 inclus
    print(N)
    N += 1  # Incrémentation de N à chaque itération

# Job 6
# Demander à l'utilisateur de saisir la valeur de N
N = int(input("Saisissez un entier pour N : "))

# Initialisation des variables
i = 1

# Utilisation de la boucle while pour afficher les premiers résultats de la multiplication de N par 7
while i <= 10:  # Affiche les 10 premiers résultats
    resultat = N * 7 * i
    print(f"{N} x 7 x {i} = {resultat}")
    i += 1  # Incrémentation de i

# Job 7
for tour in range(1, 13):  # Parcourt les tours de 1 à 12
    resultat = 3 * tour - 2  # Calcule le triple du tour moins 2
    print(f"Tour {tour} : {resultat}")  # Affiche le résultat

# Job 8
# Initialisation de la variable pour le tour précédent
tour_precedent = 0

# Boucle pour effectuer 12 tours
for tour in range(1, 13):
    resultat = tour_precedent + 2  # Calcule le résultat
    print(f"Tour {tour} : {resultat}")  # Affiche le résultat
    tour_precedent = resultat  # Met à jour le tour précédent pour le tour suivant

# Job 9
# Initialisation de la variable pour le tour précédent
tour_precedent = 0

# Boucle pour effectuer 12 tours
for tour in range(1, 13):
    resultat = tour_precedent + 2  # Calcule le résultat
    print(f"Tour {tour} : {resultat}")  # Affiche le résultat
    tour_precedent = resultat  # Met à jour le tour précédent pour le tour suivant