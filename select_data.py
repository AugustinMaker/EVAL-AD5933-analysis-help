import csv


def select_data(file_path, col1, col2):
    selected_data = []

    # Lecture du fichier CSV
    with open(file_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=';')

        # Lire la première ligne pour les titres des colonnes
        headers = next(reader)

        # Ajouter les titres des colonnes à selected_data
        selected_data.append((headers[col1], headers[col2]))

        # Lecture et sélection des colonnes spécifiées
        for row in reader:
            # Vérification que les numéros de colonne sont valides
            if col1 < len(row) and col2 < len(row):
                # Suppression des espaces superflus et remplacement des virgules par des points
                cleaned_values = []
                for value in (row[col1], row[col2]):
                    cleaned_value = value.strip().replace(',', '.')  # Remplacement des virgules par des points
                    try:
                        cleaned_value = float(cleaned_value)
                    except ValueError:
                        pass  # Laisser les titres de colonne en tant que chaînes
                    cleaned_values.append(cleaned_value)
                selected_data.append((cleaned_values[0], cleaned_values[1]))
            else:
                print(f"Les numéros de colonne spécifiés ({col1}, {col2}) sont invalides pour cette ligne : {row}")

    return selected_data
