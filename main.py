
from analyse import visualize_results
from mosaique import plot_graphs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Utilisation de la fonction
    input_file = 'M1_AIR_1.csv'
    output_file = '_M1_AIR_1.csv'
    conversion(input_file, output_file, modification_function)

    print('traitement terminée')

# Appeler la fonction pour visualiser les résultats
#visualize_results()

# Appeler la fonction pour créer et sauvegarder les graphiques
plot_graphs()