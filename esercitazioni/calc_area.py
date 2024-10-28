# calcoliamo l'area di un rettangolo

# in queta esercitazione facciamo il type casting dell'input dell'utente in quanto input() restituisce una string, e per i nostri calcoli dell'area non va bene

print(".:: Calcolo Area Rettangolo ::.")
width = float(input("Inserisci la base: "))
length = float(input("Inserisci l'altezza: "))

area = width * length

print(f"L'area del rettangolo è: {area}cm^2")