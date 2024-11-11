
#.:: Operazioni Sui File ::.

# open file, flags:
    # r - Read: apre il file per leggere, errore se non esiste
    # a - Append: apre il file per appendere, crea il file se non esiste
    # w - Write: apre il file per scrivere, crea il file se non esiste, sovrascrive ciò che c'è dentro
    # x - Create: crea il file, errore se esiste


# --- SCRIVERE SU FILE ---

# scrivo sul testo appendo nuovo testo
f = open("testo.txt", "a") 
f.write("dentro scriviamo quello che vogliamo")
f.close()


# scrivo sul testo, sovrascrivendo tutto
f = open("testo.txt", "w") 
f.write("dentro scriviamo quello che vogliamo")
f.close()


# anche così
text = "Ah belli!!!!!!\n"
with open("testo.txt", "w") as file:
    file.write(text)


# creo file
try:
    f = open("testo.txt", "x") # x genera errore se il file già esiste
    f.write("dentro scriviamo quello che vogliamo")
    f.close()
except:
    print("File già esistente")


