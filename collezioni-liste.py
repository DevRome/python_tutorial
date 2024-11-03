
# --- List ---
# una list è una collezione di dati ordinata, indicizzata, modificabile e permette duplicati


# creazione lista metodo 1
listaCitta = ["Milano", "Roma", "Napoli", "Bari"]

# creazione lista metodo 2
listaCitta = list(("Milano", "Roma", "Napoli", "Bari", "Fregene"))

# visualizzo tipo dato
print(type(listaCitta))

# visualizzo grandezza lista
print(len(listaCitta))

# visualizzo il primo ed ultimo elemento della lista
print(listaCitta[0])
print(listaCitta[-1])

# visualizzo un range
print(listaCitta[0:2]) # 2 non  compreso

# riassegno un valore
listaCitta[4] = "Brescia"
print(listaCitta)

# riassegno più valori
listaCitta[0:2] = ["Cosenza", "Piacenza"]
print(listaCitta)

# aggiungo un valore in fondo
listaCitta.append("Catanzaro")

# aggiungo un valore dove indico io
listaCitta.insert(1, "Genova")
print(listaCitta)

# concatenare due liste con extend
cittaSpagnole = ["Madrid", "Barcellona"]
listaCitta.extend(cittaSpagnole)
print(listaCitta)

# remove: eliminare un elemento specifico
listaCitta.remove("Napoli")

# pop: toglie l'elemento in fondo alla lista (contrario di append)
listaCitta.pop()
listaCitta.pop(1) # può anche eliminare un elementoall'indice che specifico

# del: elimina l'elelmto che indico all'indice che indico
del listaCitta[0]

# clear: svuota la lista
listaCitta.clear()

# loop sulle list (4 metodi)
listaCitta = ["Roma", "Madrid", "Londra", "Berlino"]

for city in listaCitta : print(city)

for i in range(len(listaCitta)) : print(listaCitta[i])

while i < len(listaCitta):
    print(listaCitta[i])
    i+=1

# shorthands - forme abbreviate di loop e condizioni su list
[print(city) for city in listaCitta]
[print(city) for city in listaCitta if city != "Roma"]

# sort ordina alfabeticamnete o numeralmente
listaCitta.sort()
print(listaCitta)

listaCitta.sort(reverse=True) # alfabeticamente decrescentere
print(listaCitta)

# copiare una lista 
nuovaListaCitta = listaCitta.copy()

# copiare una lista 
nuovaListaCitta2 = list(listaCitta)

# NB ricorda che se dichiaro una variabile e gli assegno una lista già esistente, sto facendo un riferiemnto a quell'indirizzo
listaCitta = ["Roma", "Madrid", "Londra", "Berlino"]
y = listaCitta # questo è un puntatore a quel dato già esistente, non è una nuova copia

# copio una lista in un altra lista vuota
for city in listaCitta : y.append(city)
print(y)