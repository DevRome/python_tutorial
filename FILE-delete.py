
#.:: Cancellare file o cartelle ::.

# eliminare un file e cartella (bisogna importare il modulo os)
import os
if os.path.exists("prova.txt"):
    os.remove("prova.txt")
else:
    print("non esiste un file con questo nome")

if os.path.exists("prova.txt"):
    os.rmdir("nuova_cartella")
else:
    print("non esiste una cartella con questo nome")

# per cancellare cartelle che hanno file (pericoloso!)
# import shutil
# shutil.rmtree(path) rimuove una directory contenente files