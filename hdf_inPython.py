from pyhdf.SD import SD, SDC

path= 'C:\\Users\\josep\\Projekte\\DataAnalysis_TimeSeries\\modis_sahel\\MOD13A2.A2021353.h16v07.061.2022005000804.hdf'
 
file = SD(path, SDC.READ)

# Beispiel: Liste der Datasets
datasets = file.datasets()
print(datasets)

    # Zugriff auf ein Dataset
    #data = file.select('DeinDatasetName')[:]
