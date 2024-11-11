
#.:: Operazioni Sui File ::.

# open file, flags:
    # r - Read: apre il file per leggere, errore se non esiste
    # a - Append: apre il file per appendere, crea il file se non esiste
    # w - Write: apre il file per scrivere, crea il file se non esiste, sovrascrive ciò che c'è dentro
    # x - Create: crea il file, errore se esiste

# --- LEGGERE FILE ---

# apertura e lettura file
f = open("testo.txt", "r")
print(f.read())
f.close()


# apertura file, con chiusura file automatica
with open("testo.txt") as file:
    print(file.read())


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


# leggere file con gestione Exception
try:
    with open("text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Questo file non è stato trovato!!")

