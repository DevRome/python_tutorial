# .:: CHIOSCO CIBI BEVANDE ::.

# utilizzeremo i dictionaries

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "coca": 3.50,
    "lemonade": 1.50,
}

cart = []
total = 0

# display del menu
print("------------ MENU -----------")
for key, values in menu.items():
    print(f"{key:10}: €{values:.2f}")
print("-----------------------------")


# scelta del cliente
while True:
    food = input("Scegli un cibo: (Q per uscire) ").lower()
    if(food == "q"): break

    # inserisce il cibo nel carrello solo se esiste nel menu
    elif menu.get(food) is not None:
        cart.append(food)

# calcola il totale in base al costo del cibo
for food in cart:
    total += menu.get(food)

# stampa articoli acquistati e totale
print("------- IL TUO CARRELLO ------")
print(cart)
print(f"Totale: € {total}")