
# Semplice programma per inserimento dati da parte utente e manipolazione dati con type casting

item = input("What item would you like to buy?")
price = float(input("What's the price?"))
quantity = int(input("How many items would you like to get?"))

total = quantity * price

print(f"Ypu want to buy {quantity} {item}, the total price is: €{total}")