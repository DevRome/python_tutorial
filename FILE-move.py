
#.:: Spostare file ::.
# lo stesso identico procedimento se vogliamo spostare una cartella anziché un file
import os

source = "testo.txt"
destination = "./file-operations/testo.txt"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} spostato")
except FileNotFoundError:
    print(f"{source} file non trovato")