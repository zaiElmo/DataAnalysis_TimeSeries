#Hallo Felix
#Hallo Zaizai
import earthaccess
import pprint
import os

auth = earthaccess.login(strategy="environment")

bounding_box=(-18.0, 12.0, 35.0, 20.0)  # Sahel-Zone Bounding Box: [West, South, East, North]



# Zeitspanne
temporal = ("2022-01-01", "2022-12-31")

# Suche z.B. nach MODIS Vegetation Index
results = earthaccess.search_data(
    short_name="MOD13A2",  # MODIS NDVI 16-Day product
    bounding_box=bounding_box,
    temporal=temporal,
    cloud_hosted=True
)


earthaccess.download(results[:3], local_path="modis_sahel")  # lädt in diesen Ordner

