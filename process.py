import csv
import os


def process_csv(file_name):
    # Concaténer le nom de fichier avec ".csv"
    csv_file = 'data/'+ file_name + '.csv'

    # Liste pour stocker les titres des colonnes et les données
    column_titles = []
    data = []

    # Lire le fichier CSV avec point-virgule comme séparateur
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')

        # Lire la première ligne pour obtenir les titres des colonnes
        column_titles = next(reader)[:2]

        # Lire les lignes suivantes pour obtenir les données des deux premières colonnes
        for row in reader:
            try:
                frequency = float(row[0].strip().replace(',', '.'))
                impedance = float(row[1].strip().replace(',', '.'))
                data.append([frequency, impedance])
            except ValueError as e:
                print(f"Conversion error on line : {row}, error: {e}")

    # Afficher les titres des colonnes
    #print("Titres des colonnes : ", column_titles)

    # Afficher les premières lignes des données pour vérifier
    for row in data[:5]:
        ...#print(row)

    # Appeler find_peaks pour trouver les fréquences correspondant aux pics d'impédance
    peak_frequencies = find_peaks(data)

    # Retourner les titres, les données, et les pics de fréquence
    return column_titles, data, peak_frequencies



def find_peaks(data):
    frequencies = []
    impedances = []

    # Séparer les fréquences et les impédances
    for row in data:
        frequencies.append(row[0])
        impedances.append(row[1])

    peaks = []

    # Identifier les pics d'impédance
    for i in range(1, len(impedances) - 1):
        if impedances[i] > impedances[i - 1] and impedances[i] > impedances[i + 1]:
            peaks.append((impedances[i], frequencies[i]))

    # Trier les pics par valeur d'impédance décroissante et prendre les 4 premiers
    peaks.sort(reverse=True, key=lambda x: x[0])
    peak_frequencies = [freq for _, freq in peaks[:4]]

    return peak_frequencies