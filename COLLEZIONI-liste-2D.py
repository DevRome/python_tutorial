
# --- List 2D [] - Matrici ---
# una list è una collezione di dati 
# - ordinata
# - indicizzata
# - modificabile e permette duplicati
# NB: questo concetto si può applicare anche a SET{} e TUPLE()

fruits =     ["apple", "banana", "oranage"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]
grocieries = [fruits, vegetables, meats]


# avrei potuto dichiarare la matrice anche così
grocieries = [
    ["apple", "banana", "oranage"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]

print(grocieries)

# immaginiamo una matrice
# per accedere ad un elemento dovremo indicare riga e poi colonna come indici
print(grocieries[2][0]) # chicken


# iterare su una matrice
for row in grocieries:
    for col in row:
        print(col, end=" ")
    print()


