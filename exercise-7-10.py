'''
7.10. Plus grande valeur
Écrivez un algorithme permettant, toujours sur le même principe, à l’utilisateur de saisir
un nombre déterminé de valeurs. L’algorithme, une fois a saisie terminée, renvoie la plus
grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin
d’effectuer la saisie dans un premier temps et la recherche de la plus grande valeur du
tableau dans un second temps.
'''
nb_valeurs = int(input("Combien de valeurs souhaitez-vous saisir ? "))
valeurs = []

for i in range(nb_valeurs):
    valeur = float(input(f"Saisir la valeur {i + 1} : "))
    valeurs.append(valeur)

# Recherche de la plus grande valeur
max_val = valeurs[0]
position = 0

for i in range(1, len(valeurs)):
    if valeurs[i] > max_val:
        max_val = valeurs[i]
        position = i

print("Valeurs :", valeurs)
print(f"La plus grande valeur est {max_val} à la position {position} (indice {position})")
