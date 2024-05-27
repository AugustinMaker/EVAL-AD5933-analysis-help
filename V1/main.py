
from analyse import visualize_results
from interface import interface
from mosaique import plot_graphs
from graph import graph
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


