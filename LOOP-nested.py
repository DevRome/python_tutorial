# nested loop

# ripete 3 volte il loop interno
for x in range(3):
    for y in range(1, 10):
        print(y, end="-")
    print() # cambia riga ad ogni iterazione


# stampiamo un rettangolo
rows = int(input("enter number of rows: "))
cols = int(input("Enter number of columns: "))
symb = input("Enter the symbol to fill the rectangle with")

for x in range(rows):
    for y in range(cols): print(symb, end="")
    print()