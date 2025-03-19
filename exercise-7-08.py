'''
7.8. Schtroumpf de tableau
À partir des deux tableaux précédents, écrivez un algorithme qui calcule le Schtroumpf des
deux tableaux. Pour calculer le Schtroumpf, il faut multiplier chaque élément du tableau
1 par chaque élément du tableau 2 et additionner le tout.
'''

tableau1 = [4, 8, 7, 9, 1, 5, 4, 6]
tableau2 = [7, 6, 5, 2, 1, 3, 7, 4]

schtroumpf = 0

for val1 in tableau1:
    for val2 in tableau2:
        schtroumpf += val1 * val2

print("Le Schtroumpf est :", schtroumpf)
