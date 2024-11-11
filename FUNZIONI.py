# --- FUNZIONI ---
# una funzione è un blocco di codice riutilizzabile


# dichiaro funzione
def nomeFunzione():
    print("sono una funzione in python")


# invoco funzione
nomeFunzione()


# funzione con parametro
def dicoQualcosa(laMiaParola):
    print("questa è la frase:" + laMiaParola)

dicoQualcosa("Ciao a belli!!!")


# return
def dimmiIlTuoNome(nome):
    return nome.upper()

nome = dimmiIlTuoNome("lorenzo")
print(nome)

#--------------------------------------------------------------------------------------



# .:: arbitrary argumets ::.
# *args - ci permette di passare alla funzione più non-key aruments
# **kwargs - ci permette di passare alla funzione più keyword-arguments

# es1:
def add(*args):
    total = 0
    print(args) # stampo gli argomenti passati per farti vedere
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4,5)) #15

# es2:
# se non sappiamo quanti parametri avremo predisponiamo un array come parametro
def laMiaFunzione(*opzioni):
    print(opzioni[0])
    if opzioni[1]:
        print(opzioni[1])

laMiaFunzione("ciao!!", "secondo argomento")

# es3:
# esempio con kwargs
def print_address(**kwargs):
    
    for value in kwargs.values():
        print(value) # stampa tutti i valori
    
    for key in kwargs.keys():
        print(key) # stampa tutte le chiavi
    
    for key, value in kwargs.items():
        print(f"{key}:{value}") # stampa chiavi - valori

print_address(street="Via Anzio", city="Roma", regione="Lazio", CAP="00149")

#--------------------------------------------------------------------------------------


# .:: Keyword arguments ::.
def laMiaFunzione2(tipo_pasta, sugo):
    if sugo == True: print(tipo_pasta)

laMiaFunzione2(sugo = True, tipo_pasta="Pennette") # l'ordine dei parametri non incide, in quanto sono specificatii valori ed il nome dei parametri sono gli stessi della signature della funzione

#--------------------------------------------------------------------------------------


# .:: parametri di default ::.
# questi parametri di default che impostiamo nella signature sono usati quando in fase di inocazione della funzione non dichiariamo il parametro
# es1:
def faiPasta(tipoPasta = "spaghetti"):
    print(tipoPasta)

faiPasta()

# es2:
def calcolaGuadagno(costoStanza, tasse = 21, commPiattaforma = 5):
    tasseDaPagare = (costoStanza / 100) * 21 
    commissioniDaPagare = (costoStanza / 100) * 5
    return costoStanza - tasseDaPagare - commissioniDaPagare

print(f"Guadagno della stanza al netto: {calcolaGuadagno(100)}")

#--------------------------------------------------------------------------------------

# .:: High Order Functions ::.
# sono funzioni che 
# - accettano funzioni come argomento 
# - funzioni che restituiscono una funzione

# es1:
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # questa è la HOF, alla quale passo una funzione come argomento
    text = func("Hello")
    print(text)

hello(loud)

# es2:
def divisore(x):
    def dividendo(y):
        return y / x
    return dividendo

divisione = divisore(2)
print(divisione(10))
