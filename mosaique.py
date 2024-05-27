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
            #print(freqImp)
            data_dict[file] = freqImp
        nameFI = name + 'FI'
        graph(data_dict, nameFI, name)

        for file in list_file:
            file_path = 'format_data/'+ file
            freqPhase = select_data(file_path, 0, 2)
            #print(freqPhase)
            data_dict[file] = freqPhase
        nameFP = name + 'FP'
        graph(data_dict, nameFP, name)

        for file in list_file:
            file_path = 'format_data/'+ file
            freqReal = select_data(file_path, 0, 3)
            #print(freqPhase)
            data_dict[file] = freqReal
        nameFR = name + 'FR'
        graph(data_dict, nameFR, name)

        for file in list_file:
            file_path = 'format_data/'+ file
            freqImm = select_data(file_path, 0, 4)
            #print(freqPhase)
            data_dict[file] = freqImm
        nameFIm = name + 'FIm'
        graph(data_dict, nameFIm, name)

        for file in list_file:
            file_path = 'format_data/'+ file
            freqPhase = select_data(file_path, 0, 2)
            #print(freqPhase)
            data_dict[file] = freqPhase
        nameFP = name + 'FP'
        graph(data_dict, nameFP, name)

    if x == '2' :
        name = input('Enter analysis name ')
        data_dict = {}
        print('______________________________')
        print('0 - Frequency')
        print('1 - Impedance')
        print('2 - Phase')
        print('3 - Real')
        print('4 - Imaginary')
        print('5 - Magnitude')
        print('______________________________')
        x1 = input('Enter abscisse ')
        x2 = input('Enter ordonne ')
        # Remplir le dictionnaire avec les données de select_data
        for file in list_file:
            file_path = 'format_data/'+ file
            freqImp = select_data(file_path, int(x1), int(x2))
            #print(freqImp)
            data_dict[file] = freqImp
        nameFI = name + 'FI'
        graph(data_dict, nameFI, name)

