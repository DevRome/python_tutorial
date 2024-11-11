
# --- FOR ---

# esempio 1:
cities_list = ["milano", "roma", "napoli", "salerno", "verona", "torino", "bari"]
for city in cities_list : print(city)

# esempio 2:
stringa = "anguria"
for letter in stringa : print(letter)

# esempio 3:
for x in range(6): print(x)

# esempio 4:
for x in range(4):
    if x == 2 : continue
    print(x)
    if x == 3 : break
else:
    print("ciclo for terminato")

# esempio 5 (matrice):
for i in range(3):
    for j in range(4):
        print("(" + str(i) + " : " + str(j) + ")")

# esmepio 6
# stampa i  numeri da 1 a 10
for x in range(1, 11): print(x)

# esmepio 7
# stampa i  numeri da 10 a 1
for x in reversed(range(1, 11)): print(x)

# esmepio 8
# stampa i  numeri da 1 a 10 con lo step indicato nel terzo parametro, in questo caso 2
for x in range(1, 11, 2): print(x)