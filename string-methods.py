# --- STRING ---
x = "ciao"
y = 'ciao'
print(x + y) # le stringhe vengono unite così


# Stringa multi-apici
k = """ciao, io sono una
multi riga stringa
scrivo quanto voglio senza usare apici
ad ogni riga """
print(k)


# iterazione su una stringa
for carattere in "computer": print(carattere)


name = input("Enter your full name: ")
print(name)


# accesso ad un carattere della stringa
print(name[1]) # accesso al carattere, essendo una stringa una array di carratteri


# len -> restituisce lunghezza string, in valore integer
result = len(name) 
print(result)


# find -> restituisce la prima occorrenza della lettera che inseiramo come parametro
result = name.find("e") 
print(result)


# rfind -> restituisce l'ultima occorrenza del parametro; -1 = non ha trovato niente
result = name.rfind("e") 
print (result)


# capitalize() -> restituisce la stringa Capitalize
print(name.capitalize())


# upper() -> restituisce la stringa uppercase
print(name.upper())


# lower() -> restituisce la stringa lowercase
print(name.lower())


# isdigit() -> True se la stringa contiene solo numeri
result = name.isdigit()
print(result)


# isalpha() -> restituisce True se la stringa contiene solo caratteri alfabetici
result = name.isalpha()
print(result)


phoneNumber = input("Enter your phone number")

# count(valore_da_contare) -> conta quanti caratteri selezionati abbiamo nella stringa
result = phoneNumber.count("-")
print(result)


# replace(old_value, new_value) -> sostituisce valori nella stringa 
result = phoneNumber.replace("3", "$")
print(result)


#  split -> crea array dividendo la stringa ini base al separatore che gli fornisco
z = " ciao! sono Lorenzo "
print(z.split(",")) 


# strip -> toglie gli spazi
print(z.strip()) # toglie spazi, tipo trim


# string indexing [start : end : step]
credit_number = "1234-5678-9012-3456"
print(credit_number[4])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[5:]) # dalla 5 alla fine
print(credit_number[-1]) # con il negativo parte dalla fine, in questo caso 6
print(credit_number[::3]) # con step ogni 3 caratteri
print(credit_number[::-1]) # reverse string


# ---- FORMAT SPECIFIERS ----
# format (combinare string e numeri)
prova = "ciao sono Lorenzo e sono nato il {}/{}/{}"
print(prova.format(15, 12, 2023))

# posso anche assegnare degli indici con il format
prova = "ciao sono Lorenzo e sono nato il {2}, {1}, {0}"
print(prova.format(2023, 12, 28))

# arrotondare a cifra decimale precisa:
price1 = 1.149
price2 = 1.29
print(f"Price1 = {price1:.2f} Price2 = {price2:.1f}")

# mostrare segni + e - delle cifre, con il flag +
temperature1 = -10
temperature2 = +10
print(f"Temperatura è: {temperature1:+}")
print(f"Temperatura è: {temperature2:+}")

# mostrare segni , per le migliaia
price1 = 1000.99
print(f"Prezzo1 è: {price1:,}")

# indici nominali
prova = "Ciao sono Francesca e ho {eta}, compiuti il {mese} del {anno}"
print(prova.format(eta=33, mese="Giugno", anno=2023))
 
# escapes con \
print('sono alla ricerca dell\'amore')
print("sono alla ricerca dell\"amore\" ")

