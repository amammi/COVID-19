import os
import pandas as pd

if __name__ == '__main__':
    pathdir = "./dati-province/"
    print(os.listdir(pathdir))
    for filename in os.listdir(pathdir):

        dati = pd.read_csv(pathdir + filename, encoding="ISO-8859-1")
        print(dati.head())