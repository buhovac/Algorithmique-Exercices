# Demander le nombre d'élèves
nombre_eleves = int(input("Combien d'élèves y a-t-il dans la classe ? "))

# Liste des listes pour stocker les notes de chaque élève
notes_classe = []

# Remplir la liste
for i in range(nombre_eleves):
    print(f"\n--- Élève {i + 1} ---")
    nombre_notes = int(input(f"Combien de notes pour l'élève {i + 1} ? "))

    notes_eleve = []
    for j in range(nombre_notes):
        note = float(input(f"Entrez la note {j + 1} : "))
        notes_eleve.append(note)

    # On ajoute les notes de cet élève dans la liste principale
    notes_classe.append(notes_eleve)

# Calculer la moyenne de chaque élève et afficher
moyenne_total = 0

for i in range(len(notes_classe)):
    notes_eleve = notes_classe[i]
    moyenne_eleve = sum(notes_eleve) / len(notes_eleve)
    print(f"Moyenne de l'élève {i + 1} : {moyenne_eleve:.2f}")
    moyenne_total += moyenne_eleve

# Moyenne générale de la classe
moyenne_classe = moyenne_total / nombre_eleves
print("\n======================")
print(f"Moyenne générale de la classe : {moyenne_classe:.2f}")
print("======================")
