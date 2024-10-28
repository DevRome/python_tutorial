# input()= una funzione che permette all'utente d inserire dati
# restituisce i dati inseriti come stringa

name = input("What's your name?")

# facciamo un cast int() perché la funzione input restituisce solo string, quindi se vogliamo riusare il dato age come intger, allora lo dobbiamo prima convertre
age = int(input("How old are you?"))

print(f"Hello {name} and you're {age} years old")