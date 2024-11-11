
# --- WHILE ---

# esempio 1
x = ["milano", "roma", "napoli", "salerno", "verona", "torino", "bari"]

i = 0 # variabile contatore
while i < 7:
    
    # continue esce dall'iterazione e va alla successiva
    if i == 2:
        i+=1
        continue

    # break esce proprio da un ciclo
    if i == 4:
        print("Verona merda!")
        break

    print(x[i])
    
    i+=1 # incrementa l'indice del loop

    # else svolge una operazione alla fine del ciclo
    # visto che c'è un break, in questo esempio esle non funziona
else:
    print("ciclo terminato")


# esempio2
name = input("Enter your name")
while name == "":  # finché questa condizione è vera ripete il codice sotto
    print("You dind't enter your name")
    name = input("Enter your name")

print(f"Hello {name}!")


# esempio 3:
# qui abbiamo un loop che potenzialmente continua fino all'infinito a meno che non facciamo il break
while True:
    domanda = input("Vuoi uscire dal loop? Y / N")
    if domanda != "Y": print("Loop continua")
    else:
        break
print("Loop terminato")

    
    
    