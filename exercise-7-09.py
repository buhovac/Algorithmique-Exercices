'''
7.9. Augmentation
Écrivez un algorithme qui permette la saisie d’un nombre quelconque de valeurs, sur le
principe de l’exercice tableau positif et négatif. Toutes les valeurs doivent être ensuite
augmentées de 1 et le nouveau tableau sera affiché à l’écran.
'''

nb_valeurs = int(input("Combien de valeurs souhaitez-vous saisir ? "))
valeurs = []

for i in range(nb_valeurs):
    valeur = float(input(f"Saisir la valeur {i + 1} : "))
    valeurs.append(valeur)

# Augmentation de 1
valeurs_augmentees = [val + 1 for val in valeurs]

print("Valeurs originales :", valeurs)
print("Valeurs augmentées de 1 :", valeurs_augmentees)
