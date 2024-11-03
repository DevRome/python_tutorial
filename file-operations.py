
# open file
    # r - Read: apre il file per leggere, errore se non esiste
    # a - Append: apre il file per appendere, crea il file se non esiste
    # w - Write: apre il file per scrivere, crea il file se non esiste, sovrascrive ciò che c'è dentro
    # x - Create: crea il file, errore se esiste


# apertura e lettura file
f = open("testo.txt", "r")
print(f.read())
f.close()


# apertura e lettura file con limite caratteri
f = open("testo.txt", "r")
print(f.read(10))
f.close()


# apertura e lettura file con limite una riga
f = open("testo.txt", "r")
print(f.readline())
f.close()


# visualizza ogni riga
f = open("testo.txt", "r")
for riga in f:
    print(riga)
f.close()


# scrivo sul testo appendo nuovo testo
f = open("testo.txt", "a") 
f.write("dentro scriviamo quello che vogliamo")
f.close()


# scrivo sul testo, sovrascrivendo tutto
f = open("testo.txt", "w") 
f.write("dentro scriviamo quello che vogliamo")
f.close()


# creo file
try:
    f = open("testo.txt", "x") # x genera errore se il file già esiste
    f.write("dentro scriviamo quello che vogliamo")
    f.close()
except:
    print("File già esistente")


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
