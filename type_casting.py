# il type casting è il processo di conversione di una variabile in un altro tipo

# str(), int(), float(), bool()

name = "Lorenzo"
age = 38
height = 1.78
is_student = True

# stampare tipo variabile
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#convertiamo

# se convertiamo float in int andiamo a troncare la parte decimale
height = int(height)
print(height) 

# se convertiamo int in float, aggiungiamo una posizione in decimale
age = float(age)
print(age) 

# se convertiamo float o int in string avremo lo stesso valore ma in stringa
height = str(height)
print(height)

# se convertiamo una stringa in boolean avremo True, tranne nel caso in cui la stringa è vuota, allora avremo vaòlore False
stringa1 = "ciao"
print(bool(stringa1))

stringa2 = ""
print(bool(stringa2))