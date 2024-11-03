# --- Dictionary ---
# rappresentano coppie chiave-valore, sono collezioni di dati ordinate, modificabili ma non permettono duplicati, nel senso che le chiavi non  possono essere duplicate all'interno dello stesso dictionary

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 28
}

print(type(persona))

# visualizzare i dati del dictionary
print(persona.keys) # chiavi di persona
print(persona.get("nome")) # visualizza solo il valore della chiave "nome"
print(persona.items()) # stampa sia chiavi che valori associato
print("nome" in persona) # true, controlla se esiste questa proprietà 

# modificare il dictionary
persona.update({"nome": "anna"})
print(persona)

# aggiugere elementi
persona["colore"] = "blue"
print(persona)

# rimuovere elementi
persona.pop("nome")
persona.popitem() #rimuove ultima chiave
persona.clear() # svuota il contenuto di dictionary
del persona # cancella dictionary

# iterare su persona
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 28,
    "indirizzo": {
        "citta": "Roma",
        "CAP": "00148",
        "civico":"63"
    }
}

# accedere ad una proprietà annidata
print(persona["indirizzo"]["CAP"])

for x in persona: print(x) # stampa le chiavi
for x in persona: print(persona[x]) # stampa i valori delle chiavi
for x in persona.keys(): print(x) # stampa le chiavi
for x in persona.values() : print(x) # stampa i valori delle chiavi

# stampa sia keys che valori
for x, y in persona.items(): print(x, y)

# copiare persona (2 metodi)
newPersona = persona.copy()
newPersona2 = dict(persona)

