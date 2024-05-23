import csv

def conversion(input_file, output_file, modification_function):
    # Lire le fichier CSV
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Modifier les données
    modified_rows = modification_function(rows)

    # Réenregistrer les données modifiées dans un nouveau fichier CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(modified_rows)


def modification_function(rows):
    modified_rows = []

    # Traiter la première ligne
    first_row = rows[0]
    first_line = ','.join(first_row)
    modified_first_line = first_line.replace(',', ';')
    modified_rows.append(modified_first_line.split(';'))

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
