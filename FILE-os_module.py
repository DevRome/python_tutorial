import os

# alcune funzioni del modulo OS, path
# restituiscono un Boolean

# exists() -> controlla se esiste
# isdir(path) -> controlla se il parametro corrisponde ad una cartella
# isfile(path) -> controlla se il parametro è un file

percorsoCartella = "/home/lorenzo/python_projects"
percorsoFile = "prova.txt"

if os.path.exists(percorsoCartella): print("la lacation esiste")
if os.path.exists("testo.txt"): print("il file esiste")
if os.path.isdir(percorsoCartella): print("è una cartella")
if os.path.isfile(percorsoFile): print("è un file")

