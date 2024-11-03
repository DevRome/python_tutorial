name = input("Enter your full name")
print(name)


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


# string indexing [start : end : step]
credit_number = "1234-5678-9012-3456"
print(credit_number[4])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[5:]) # dalla 5 alla fine
print(credit_number[-1]) # con il negativo parte dalla fine, in questo caso 6
print(credit_number[::3]) # con step ogni 3 caratteri
print(credit_number[::-1]) # reverse string

# PRESO DA ALTRO TUTORIAL

# --- STRING ---
x = "ciao"
y = 'ciao'
print(x+y)

k = """ciao, io sono una
multi riga stringa
scrivo quanto voglio senza usare apici
ad ogni riga """
print(k)

print(len(y)) # length
print(y[1]) # accesso al carattere, essendo una stringa una array di carratteri

for carattere in "computer": print(carattere)

z = " ciao, sono Lorenzo "
print(z[:3]) # dal carattere 0 al 3
print(z[9:16]) # dal carattere 9 al 16
print(z[-7]) # 7 caratteri indietro dall'ultimo carattere
print(z[-7:]) # dall'ultimo carattere fino a 7 indietro
print(z.lower())
print(z.upper())
print(z.strip()) # toglie spazi, tipo trim
print(z.replace("L", "#"))
print(z.split(",")) #crea array dividendo la stringa in base al separatore che gli do io

# format (combinare string e numeri)
prova = "ciao sono Lorenzo e sono nato il {}/{}/{}"
print(prova.format(15, 12, 2023))

# posso anche assegnare degli indici con il format
prova = "ciao sono Lorenzo e sono nato il {2}, {1}, {0}"
print(prova.format(2023, 12, 28))

# indici nominali
prova = "Ciao sono Francesca e ho {eta}, compiuti il {mese} del {anno}"
print(prova.format(eta=33, mese="Giugno", anno=2023))
 
# escapes con \
print('sono alla ricerca dell\'amore')
print("sono alla ricerca dell\"amore\" ")

