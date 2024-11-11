
#.:: Copiare file ::.

# copyfile(src, dest) = copia contenuto di un file
# copy()     = copyfile() + permission mode + la destinazione può essere una cartella
# copy2()    = copy() + copia i metadata (creazione file e le volte che è stato modificato)

import shutil

shutil.copyfile("testo.txt", "./file-operations/testo-copy.txt")
