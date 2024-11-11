
# --- Tuple () ---
# sono collezioni di dati 
# - ordinate
# - indicizzate, 
# - non modificabili e permettono duplicati
# - una volta create non si possono modificare
# - SONO PIU' VELOCI DELLE LIST

# creo tupla
citta = ("milano", "roma", "napoli", "venezia")

# stampo tipo dato
print(type(citta))

# stampo lunghezza tupla
print(len(citta))

# accedere ad un elemento della tupla
print(citta[0])

# accedo a più dati
print(citta[0:2])

# accedo all'ultimo elemento
print(citta[-1])

# controllo se c'è un dato
if "venezia" in citta : print("ok")

# spacchettare una tupla
(x,y, *z) = citta
print(x)
print(y)
print(z)

# iterare su tupla
for x in citta: print(x)

# iterare su tupla
for i in range(len(citta)): print(citta[i])

# iterare su una tupla
while i < len(citta):
    print(citta[i])
    i+=1

# unire due tuple
lista_citta = ("milano", "roma", "napoli", "venezia", "udine")
lista_citta_2 = ("bari", "cosenza", "cittadella", "udine")
y = lista_citta + lista_citta_2
print(y)

# count: ci permette di contare quante volte un valore c'è nella tupla
x = y.count("udine")
print(x)

# index: ci permette di contare quante volte un valore c'è nella tupla
x = y.index("udine")
print(x)
