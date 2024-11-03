# --- Funzioni ---

# dichiaro funzione
def nomeFunzione():
    print("sono una funzione in python")

# invoco funzione
nomeFunzione()


# funzione con parametro
def dicoQualcosa(laMiaParola):
    print("questa è la frase:" + laMiaParola)

dicoQualcosa("Ciao a belli!!!")


# arbitrary argumets:
# se non sappiamo quanti parametri avremo predisponiamo un array come parametro
def laMiaFunzione(*opzioni):
    print(opzioni[0])
    if opzioni[1]:
        print(opzioni[1])

laMiaFunzione("ciao!!", "secondo argomento")


# Keyword arguments
def laMiaFunzione2(tipo_pasta, sugo):
    if sugo == True: print(tipo_pasta)

laMiaFunzione2(sugo = True, tipo_pasta="Pennette")


# parametri di default
def faiPasta(tipoPasta = "spaghetti"):
    print(tipoPasta)

faiPasta()


# return
def dimmiIlTuoNome(nome):
    return nome.upper()

nome = dimmiIlTuoNome("lorenzo")
print(nome)