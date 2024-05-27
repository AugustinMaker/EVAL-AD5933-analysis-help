import os


def file_choice(data_folder):
    # Chemin du sous-dossier 'data'

    # Vérifier si le dossier 'data' existe
    if not os.path.exists(data_folder):
        print(f"Le dossier '{data_folder}' n'existe pas.")
        return

    # Lister les fichiers dans le dossier 'data'
    files = os.listdir(data_folder)
    files = [f for f in files if os.path.isfile(os.path.join(data_folder, f))]

    # Afficher les fichiers
    if not files:
        print(f"Il n'y a aucun fichier dans le dossier '{data_folder}'.")
        return

    print("Fichiers présents dans le dossier 'data' :")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")

    # Demander le nombre de fichiers à modifier
    while True:
        try:
            num_files_to_modify = int(input("Combien de fichiers souhaitez-vous selectionner ? "))
            if num_files_to_modify > len(files):
                print(f"Le nombre entré est supérieur au nombre de fichiers présents ({len(files)}).")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Demander les noms des fichiers à modifier
    files_to_modify = []
    for i in range(num_files_to_modify):
        while True:
            file_name = input(f"Entrez le nom du fichier {i + 1} à selectionner : ")
            if file_name in files:
                files_to_modify.append(file_name)
                break
            else:
                print(f"Le fichier '{file_name}' n'existe pas dans le dossier 'data'. Veuillez entrer un nom valide.")

    print("Les fichiers selectionner sont :")
    for file in files_to_modify:
        print(file)
    return files_to_modify