
# ---- PROGRAMMA BASIC ----


# commento su linea (python non ha il commento multilinea)
# dato di partenza
persona = {
    "nome": "Lorenzo",
    "cognome": "Raspa",
    "eta": 37
} 


# operazioni disponibili
operazioni = ("aggiungere", "modificare", "eliminare")


# stampa a video la persona
print(persona)


def start(): 
    # prendi input testo
    action = input("cosa vuoi fare?")
    if action == operazioni[0]:
        x = input("Aggiungi chiave:valore separati da una virgola")
        aggiungi(x.split(","))
    elif action == operazioni[1]:
        x = input("Modifica chiave:valore separati da una virgola")
        modifica(x.split(","))
    elif action == operazioni[2]:
        x = input("Elimina quale chiave?")
        elimina(x)
# end start()


def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)
# end aggiungi()


def modifica(param):
    persona[param[0]] = param[1]
    print(persona)
# end modifica()


def elimina(param):
    del persona[param]
    print(persona)
# end elimina()


while True:
    start()









