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
    print('3 - temporal evolution')
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

    if x == '3' :
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

        def display_files_with_numbers(files):
            """Displays the files with numbers."""
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")

        def ask_user_for_order(num_files):
            """Asks the user to input a new order for the files."""
            while True:
                try:
                    # Read user input
                    order = input(f"Enter the numbers in the desired order (e.g., 2 1 4 3 for {num_files} files): ")
                    # Convert input to a list of integers
                    order_list = [int(num) for num in order.split()]

                    # Check if the numbers are valid
                    if sorted(order_list) == list(range(1, num_files + 1)):
                        return order_list
                    else:
                        print(f"Please enter valid numbers from 1 to {num_files}, without duplicates.")
                except ValueError:
                    print("Invalid input. Make sure to use only numbers separated by spaces.")

        def reorder_files(files, order):
            """Reorders the files according to the user's specified order."""
            return [files[i - 1] for i in order]

        # Display the files with numbers
        display_files_with_numbers(list_file)

        # Ask the user for the new order
        new_order = ask_user_for_order(len(list_file))

        # Reorder the list according to the new order
        reordered_list_file = reorder_files(list_file, new_order)

        # Display the new list
        print("\nNew list of files in the chosen order:")
        display_files_with_numbers(reordered_list_file)