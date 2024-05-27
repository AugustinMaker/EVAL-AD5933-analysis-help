import csv
import os
from file_choice import file_choice

def conversion():
    # Appeler la fonction file_choice pour obtenir la liste des fichiers à modifier
    input_files = file_choice('data')
    if not input_files:
        return

    # Créer le dossier 'format_data' s'il n'existe pas
    output_folder = 'format_data'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_file in input_files:
        # Lire le fichier CSV
        input_path = os.path.join('data', input_file)
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = list(reader)

        # Modifier les données
        modified_rows = modification_function(rows)

        # Réenregistrer les données modifiées dans un nouveau fichier CSV
        output_file = f'F_{input_file}'
        output_path = os.path.join(output_folder, output_file)
        with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(modified_rows)

        print(f"Fichier '{input_file}' modifié et enregistré sous '{output_path}'.")


def modification_function(rows):
    modified_rows = []

    first_row = rows[0]

    # Ajouter la première ligne modifiée à la liste des lignes modifiées
    line = ','.join(first_row)
    new_line = ''
    for char in line:
        if char == ',':
            new_line += ';'
        else:
            new_line += char
    new_line = new_line[:-1]
    modified_row = new_line.split(',')
    modified_rows.append(modified_row)

    # Indices des virgules à remplacer pour les autres lignes
    indices_to_replace = [0, 2, 4, 5, 6]

    # Traiter les autres lignes
    for row in rows[1:]:
        line = ','.join(row)
        new_line = ''
        comma_count = 0

        for i, char in enumerate(line):
            if char == ',':
                if comma_count in indices_to_replace:
                    new_line += ';'
                else:
                    new_line += ','
                comma_count += 1
            else:
                new_line += char

        modified_row = new_line.split(',')
        modified_rows.append(modified_row)
    return modified_rows


