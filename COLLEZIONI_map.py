#.:: map ::.
# applica una funzione ad ogni item dell'iterable: lists, tuple ecc)
# map(function, iterable)
# restituisce un oggetto Map, quindi bisogna fare il cast con list()

store = [
    ("shirt", 20.00),
    ("jeans", 30.00),
    ("jacket", 100.00),
]

# poniamo che i prezzi delle tuple sopra sono in dollari e li vogliamo convertire inn euro
# applichiamo una funzione con map ad ogni item della list

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)