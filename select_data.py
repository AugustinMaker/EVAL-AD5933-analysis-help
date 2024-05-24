import csv


def select_data(file_path, col1, col2):
    selected_data = []

    # Lecture du fichier CSV
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=';')

        # Lecture et sélection des colonnes spécifiées
        for row in reader:
            # Vérification que les numéros de colonne sont valides
            if col1 < len(row) and col2 < len(row):
                selected_data.append((row[col1], row[col2]))
            else:
                print(f"Les numéros de colonne spécifiés ({col1}, {col2}) sont invalides pour cette ligne : {row}")

    return selected_data


# Exemple d'utilisation
file_path = 'chemin/vers/le/fichier.csv'
colonne1 = 0
colonne2 = 2

donnees_extraites = select_data(file_path, colonne1, colonne2)
print("Données extraites :", donnees_extraites)
