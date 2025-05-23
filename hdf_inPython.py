from pyhdf.SD import SD, SDC
import pandas as pd

#Mit windows kann pyhdf.SD probleme machen ich epfehle WSL und ein Vitueles python enviorment


# HDF4-Datei öffnen
hdf_file = SD("/mnt/c/Users/josep/Projekte/DataAnalysis_TimeSeries/modis_sahel/MOD13A2.A2021353.h16v07.061.2022005000804.hdf", SDC.READ)

# Datensatz auswählen
dataset_name = list(hdf_file.datasets().keys())[0]
dataset = hdf_file.select(dataset_name)

# Daten auslesen
data = dataset[:, :]

# Attribute auslesen
attrs = dataset.attributes()

# Beispiel: Nutze 'long_name' und 'units' für Header, falls vorhanden
long_name = attrs.get('long_name', dataset_name)
units = attrs.get('units', '')

# Header bauen (Beispiel: "NDVI (units)")
header_name = f"{long_name} ({units})" if units else long_name

# Falls 2D-Daten (z.B. Raster), machen wir generische Spaltennamen:
num_cols = data.shape[1]
headers = [f"{header_name}_col{i}" for i in range(num_cols)]

# DataFrame mit Header
df = pd.DataFrame(data, columns=headers)

# Datei schließen
hdf_file.end()

# CSV-Pfad (anpassen)
csv_path = "/mnt/c/Users/josep/Projekte/DataAnalysis_TimeSeries/ShaelCSV/ndvi_dataset.csv"

# CSV speichern
df.to_csv(csv_path, index=False)

print(f"CSV mit Header gespeichert unter: {csv_path}")
