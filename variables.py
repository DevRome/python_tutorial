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



