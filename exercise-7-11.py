'''
7.11. Moyenne de classe
Écrivez un algorithme permettant à l’utilisateur de saisir les notes d’une classe.
L’algorithme, une fois la saisie terminée, renvoie le nombre de ces notes supérieures à la
moyenne de la classe.
'''

nombre_eleves = int(input("Nombre eleves? "))

moyennes_eleves = []

for i in range(nombre_eleves):
    print(f"Élève {i + 1}")

    nombre_notes = int(input(f"Combien de notes pour l'élève {i + 1} ? "))

    notes = []

    for j in range(nombre_notes):
        note = float(input(f"Note {j + 1} : "))
        notes.append(note)

    moyenne = sum(notes) / nombre_notes
    moyennes_eleves.append(moyenne)

    print(f"Moyenne de l'élève {i + 1} : {moyenne:.2f}")

moyenne_classe = sum(moyennes_eleves) / nombre_eleves


print(f"Moyenne générale de la classe : {moyenne_classe:.2f}")

