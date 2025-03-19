'''
7.7. Somme tableaux
Écrivez un algorithme constituant un tableau à partir des deux tableaux suivants. Le
nouveau tableau contiendra la somme des éléments des deux tableaux de départ.
4 8 7 9 1 5 4 6
7 6 5 2 1 3 7 4
11 14 12 11 2 8 11 10
'''

tableau1 = [4, 8, 7, 9, 1, 5, 4, 6]
tableau2 = [7, 6, 5, 2, 1, 3, 7, 4]

# Création du nouveau tableau avec la somme
somme_tableaux = [tableau1[i] + tableau2[i] for i in range(len(tableau1))]

print("Tableau 1 :", tableau1)
print("Tableau 2 :", tableau2)
print("Somme des tableaux :", somme_tableaux)
