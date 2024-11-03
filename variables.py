# ci sono 4 tipi di dati in python
# string, integer, float, boolean

firstName = "Lorenzo"
age = 38
height = 1.78
is_married = False
is_online = True

# stampiamo una stringa
print("Hello", firstName)

# con f possiamo usare la variabile in parentesi graffe (come in JS)
print(f"Hello {firstName}")

print(f"You're {age} years old")

print(f"You're {height}m tall")

if(is_married == False): print("Non sei sposato")
else: print("Sei sposato")

print("Sei online") if is_online else print("Non sei online")



# le variabili in python si inizializzano sempre, altrimenti genera errore
x = 10 # ok

# si possono anche dichiarare più variabili insieme
y, z, w = 10, 20, 30

print(x, y, z, w)


# --- Tipi di dati ---: 
# string, integer, float, boolean, list, tuple, range, dict, set

varString = "ciao"
varInteger = 20
varFloat = 5.5
varBoolean = True
varList = ["roma", "milano", "napoli"] # non sono array!!!
varTuple = ("roma", "milano", "napoli")
varRange = range(6)
varDict = {"nome": "Lorenzo", "anni": "37"}
varSet = {"roma", "milano", "napoli"}

# per visualizzare il tipo di dato usiamo la funzione type()
print(type(varString))
print(type(varInteger))
print(type(varFloat))
print(type(varBoolean))
print(type(varList))
print(type(varTuple))
print(type(varRange))
print(type(varDict))
print(type(varSet))

# --- Casting ---
# in python due tipi diversi di dato non si possono processare aritmicamente (come in javascript che fa casting automatico)
x = "5"
y = 5
# print(x+y) questo genera errore. allora faccio casting
y = str(y)
print(x+y) #55

x= "Lorenzo"
y = "Raspa"
print(x+y) # LorenzoRaspa

w="5"
k="2"
print(float(w) + int(k))


# --- Boolean ---
x = True
y = False
print(bool(1)) # true

# questi valori qui sotto restituiscono tutti un valore vuoto
print(bool(0)) # false
print(bool(False)) # false
print(bool(None)) # false
print(bool("")) # false
print(bool(())) # false
print(bool([])) # false
print(bool({})) # false
