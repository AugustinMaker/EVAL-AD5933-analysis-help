

import os
from select_data import select_data
from graph import graph
import matplotlib.pyplot as plt


def standard_mosaique(file_list, analysis_name):
    if not file_list or not analysis_name:
        print("Invalid input: file_list and analysis_name must be provided.")
        return []

    data_dict = {}

    def save_graph(data_dict, file_name, title):
        graph(data_dict, file_name, title)
       # plt.savefig(file_name)  # Save the current figure
        plt.close()  # Close the figure to free up memory

    def ensure_png_extension(file_name):
        return file_name if file_name.lower().endswith('.png') else f"{file_name}.png"

    image_files = []

    # Frequency vs Impedance
    for file in file_list:
        file_path = os.path.join('format_data', file)
        freqImp = select_data(file_path, 0, 1)
        data_dict[file] = freqImp
    nameFI = ensure_png_extension(analysis_name + 'FI')
    save_graph(data_dict, nameFI, analysis_name)
    image_files.append(nameFI)

    # Frequency vs Phase
    for file in file_list:
        file_path = os.path.join('format_data', file)
        freqPhase = select_data(file_path, 0, 2)
        data_dict[file] = freqPhase
    nameFP = ensure_png_extension(analysis_name + 'FP')
    save_graph(data_dict, nameFP, analysis_name)
    image_files.append(nameFP)

    # Frequency vs Real
    for file in file_list:
        file_path = os.path.join('format_data', file)
        freqReal = select_data(file_path, 0, 3)
        data_dict[file] = freqReal
    nameFR = ensure_png_extension(analysis_name + 'FR')
    save_graph(data_dict, nameFR, analysis_name)
    image_files.append(nameFR)

    # Frequency vs Imaginary
    for file in file_list:
        file_path = os.path.join('format_data', file)
        freqImm = select_data(file_path, 0, 4)
        data_dict[file] = freqImm
    nameFIm = ensure_png_extension(analysis_name + 'FIm')
    save_graph(data_dict, nameFIm, analysis_name)
    image_files.append(nameFIm)

    print("graph plot")
    return image_files
