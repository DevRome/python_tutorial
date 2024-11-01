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

