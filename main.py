
from analyse import visualize_results
from interface import interface
from mosaique import plot_graphs
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        clear_console()
        resultat = interface()
        if resultat == 1:
            print("programe cloturé")
            break

    # Utilisation de la fonction
    #input_file = 'test.csv'
    #output_file = '_test.csv'
    #conversion(input_file, output_file)
    #interface()
    #print('traitement terminée')

# Appeler la fonction pour visualiser les résultats
#visualize_results()

# Appeler la fonction pour créer et sauvegarder les graphiques
#plot_graphs()