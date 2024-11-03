
# --- WHILE ---

x = ["milano", "roma", "napoli", "salerno", "verona", "torino", "bari"]

i = 0 # variabile contatore
while i < 7:
    
    # continue esce dall'iterazione e va alla successiva
    if i ==2:
        i+=1
        continue

    # break esce proprio da un ciclo
    if i == 4:
        print("Verona merda!")
        break

    print(x[i])
    i+=1

    # else svolge una operazione alla fine del ciclo
    # visto che c'è un break, in questo esempio esle non funziona
else:
    print("ciclo terminato")

    
    
    