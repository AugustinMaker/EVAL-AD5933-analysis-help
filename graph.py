import os
import matplotlib.pyplot as plt

def graph(data_dict, graph_name, folder_name, horizontal_spacing=0.2, vertical_spacing=0.3):
    # Utiliser le backend TkAgg pour s'assurer que plt.show() fonctionne
    plt.switch_backend('TkAgg')

    # Vérifier si le dossier de sortie existe, sinon le créer
    output_folder = os.path.join("output", folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Nombre de graphiques
    num_graphs = len(data_dict)

    # Déterminer le nombre de lignes et de colonnes pour la mosaïque
    num_cols = 2  # Par exemple, on veut 2 colonnes de graphiques
    num_rows = (num_graphs + num_cols - 1) // num_cols  # Calcul du nombre de lignes nécessaire

    # Créer la figure et les axes pour la mosaïque
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows),
                             gridspec_kw={'wspace': horizontal_spacing, 'hspace': vertical_spacing})
    axes = axes.flatten()  # Aplatir la grille d'axes pour un accès facile

    for idx, (file_name, data) in enumerate(data_dict.items()):
        # Extraire les titres et les données des colonnes
        titles = data[0]
        col1_data = [row[0] for row in data[1:]]
        col2_data = [row[1] for row in data[1:]]

        # Tracer le graphique sur l'axe correspondant
        axes[idx].plot(col1_data, col2_data, marker='o')
        axes[idx].set_title(file_name)
        axes[idx].set_xlabel(titles[0])
        axes[idx].set_ylabel(titles[1])

    # Supprimer les axes inutilisés si num_graphs n'est pas un multiple de num_cols
    for ax in axes[num_graphs:]:
        fig.delaxes(ax)

    # Ajuster la disposition
    plt.tight_layout()

    # Afficher la mosaïque de graphiques
    #plt.show()

    # Assurer que le fichier de sortie a l'extension correcte
    if not graph_name.endswith('.png'):
        graph_name += '.png'

    # Sauvegarder la mosaïque de graphiques dans un fichier PNG
    output_file = os.path.join(output_folder, graph_name)
    fig.savefig(output_file)
    print(f"Graphique sauvegardé sous {output_file}")
