from file_choice import file_choice
from conversion import conversion
from mosaique import mosaique

def interface():
    print("analysis aid for data from the EVAL AD5933 software")
    print("___________________________________________________")
    print("1 - Format the data")
    print("2 - Plot impedance graphs ")
    print("3 - Peak analysis ")
    print("4 - Exit ")
    print("___________________________________________________")

    x = input()

    if x == "1" :
        print("Format data")
        conversion()
        return(0)
    if x == "2" :
        mosaique()
        return(0)
    if x == "3" :
        print("plot")
        return(0)
    if x == "4" :
        print("EXIT")
        return(1)
    else:
        print("invalid value")