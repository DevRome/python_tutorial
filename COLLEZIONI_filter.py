#.:: filter ::.
# crea una collezione di elementi da un iterable, per la quale la funzione applicata restituisce true
# filter(function, iterable)
# restituisce un oggetto Filter, quindi bisogna fare il cast con list()

store = [
    ("shirt", 20.00),
    ("jeans", 30.00),
    ("jacket", 100.00),
    ("sweater", 59.00),
    ("plush", 40.00),
]

# volgiamo creeare una nuova lista selezionando solo articoli che costano meno di 60 euro

price = lambda data:data[1] <= 60
newStore = list(filter(price, store))

for i in newStore:
    print(i)