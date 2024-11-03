
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