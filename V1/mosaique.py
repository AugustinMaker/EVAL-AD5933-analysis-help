import csv
import matplotlib.pyplot as plt
import matplotlib
from process import process_csv
from file_choice import file_choice
from select_data import select_data
from graph  import graph



def mosaique():
    list_file = file_choice('format_data')
    print(list_file)
    print('___________________________________')
    print('1 - Standard analysis')
    print('2 - Specific analysis')
    print('___________________________________')
    x = input()

    if x == '1' :
        name = input('Enter analysis name ')
        data_dict = {}

        # Remplir le dictionnaire avec les données de select_data
        for file in list_file:
            file_path = 'format_data/'+ file
            freqImp = select_data(file_path, 0, 1)
            print(freqImp)
            data_dict[file] = freqImp
        nameFI = name + 'FI'
        graph(data_dict, nameFI, name)








'''
def process_csv(file_name):
    csv_file = file_name + '.csv'
    data = []

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Ignorer la première ligne contenant les titres des colonnes

        for row in reader:
            try:
                frequency = float(row[0].strip().replace(',', '.'))
                impedance = float(row[1].strip().replace(',', '.'))
                data.append([frequency, impedance])
            except ValueError as e:
                print(f"Erreur de conversion sur la ligne : {row}, erreur: {e}")

    return data
'''
def plot_graphs():
    while True:
        try:
            num_files = int(input("Entrez le nombre de fichiers à analyser : "))
            if num_files <= 0:
                raise ValueError("Le nombre de fichiers doit être positif.")
            break
        except ValueError as e:
            print(f"Entrée invalide: {e}. Veuillez entrer un nombre entier positif.")

    file_names = [input(f"Entrez le nom du fichier {i + 1} : ") for i in range(num_files)]

    fig, axes = plt.subplots(1, num_files, figsize=(num_files * 6, 6), dpi=200)

    if num_files == 1:
        axes = [axes]

    for ax, file_name in zip(axes, file_names):
        data = process_csv(file_name)
        frequencies = [row[0] for row in data]
        impedances = [row[1] for row in data]

        ax.plot(frequencies, impedances, label='Impedance')
        ax.set_title(file_name)
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Impedance')
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.savefig('graphs_mosaic.png', bbox_inches='tight')


