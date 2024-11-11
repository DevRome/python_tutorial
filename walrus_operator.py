# .:: WALRUS Operator := ::.
# da python 3.8
# assegna valori a variabili come parte di una più grande espressione


# es1:
happy = True
print(happy)

# possiamo scrivere tutto così
print(happy := False) # assegnamo il valore alla variabile e possiamo utilizzarla direttamente nella funzione print()


# es2:
foods = list()
while True:
    food = input("Che cibo ti piace?")
    if food == "quit":
        break
    foods.append(food)

# equivaleva a scrivere
foods = list()
while food := input("Che cibo ti piace?") != "quit":
    foods.append(food)