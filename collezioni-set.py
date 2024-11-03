
# --- Set ---
# collezioni di dati non ordinate, non indicizzate, non modificabili e non permettono duplicati

set1 = {"milano", "roma", "napoli"}
set2 = {"milano", "genova", "montecarlo"}

# stampo i valori: vedrai che ad ogni esecuzione i valori del set saranno mischiati
print(set1)

# controllo se un dato esiste nel set
print("milano" in set1) # true

# stampo tipo dato
print(type(set1))

# stampo lunghezza set
print(len(set1))

# iterare
for city in set1 : print(city)

# aggiungere elementi
set1.add("venezia")

# unire due set
set1.update(set2)
print(set1)

# rimuovere elementi
set1.remove("milano")
set1.discard("venezia") # con discard se l'elemento che vogliamo cancellare non esiste, esso nonn genera errore
set1.pop() # toglie l'ultimo eleemnto del set
set1.clear() # svuota il set ma comunue lo mantiene
del set1 # cancella il set dalla memoria

# unire sets: sia union() e update() ESCLUDONO gli elementi duplicati
set1 = {"milano", "roma", "napoli"}
set2 = {"milano", "genova", "montecarlo"}
set3 = set1.union(set2)
set1.update(set2)

# unire elementi con intersection (include SOLO gli elementi comuni ai due set)
set1 = {"milano", "roma", "napoli"}
set2 = {"milano", "genova", "montecarlo"}
set1.intersection_update(set2) # intersection_update 
set3 = set1.intersection(set2) # include nel nuovo set SOLO gli elementi duplicati

# unire elementi con symmetric_difference, ci tutto, tranne gli elementi che hanno in comune 
# simmetric_difference_update()
set1 = {"milano", "roma", "napoli"}
set2 = {"milano", "genova", "montecarlo"}
set3 = set1.symmetric_difference_update(set2)

# symmetric_difference
set1 = {"milano", "roma", "napoli"}
set2 = {"milano", "genova", "montecarlo"}
set1.symmetric_difference(set2)
print(set1)
