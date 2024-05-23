import csv
import matplotlib.pyplot as plt
import matplotlib
from conversion import conversion
import os
from mosaique import plot_graphs
from process import process_csv

# Utiliser le backend 'Agg' de Matplotlib
matplotlib.use('Agg')

def interface ():
    print("analysis aid for data from the EVAL AD5933 software")
    print("___________________________________________________")
    print("1 - Format the data")
    print("2 - Isolate impedance peaks ")
    print("3 - Plot impedance graphs ")
    print("___________________________________________________")

    x = input()

    if x == "1" :
        print("(format : test.csv)")
        input_file = input("name input file : ")
        output_file = input("name output file : ")
        conversion(input_file, output_file)

    if x == "2" :
        visualize_results()
    if x == "3" :
        plot_graphs()
    else:
        print("invalid value")
'''
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
'''




def visualize_results():
    num_files = int(input("Enter the number of files to scan : "))
    print('files available')
    for root, dirs, files in os.walk('data'):
        for file in files:
            print(os.path.join(root, file))
    print('(file name in the form: filename)')
    file_names = [input(f"Enter the file name {i + 1} : ") for i in range(num_files)]

    results = []

    for file_name in file_names:
        _, _, peak_frequencies = process_csv(file_name)
        results.append((file_name, peak_frequencies))

    # Création du tableau de visualisation avec matplotlib
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # Préparation des données pour le tableau
    table_data = []
    headers = ["File"] + [f"Peak {i + 1}" for i in range(4)]

    for result in results:
        row = [result[0]] + result[1]
        table_data.append(row)
        # Création du tableau avec taille de police agrandie
    table = ax.table(cellText=table_data, colLabels=headers, cellLoc='center', loc='center')

    # Ajuster la taille de police
    table.auto_set_font_size(False)
    table.set_fontsize(14)  # Définir la taille de la police à 14
    table.scale(1.5, 1.5)  # Augmenter la taille du tableau

    # Ajuster la mise en page pour éviter les coupures
    fig.tight_layout()
    title = input('table title : ')
    png_title ='png/'+ title + '.png'
    plt.savefig(png_title, bbox_inches='tight')  # Sauvegarder l'image du tableau
    print('png file create')




