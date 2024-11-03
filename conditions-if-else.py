# Condizioni con if, elif, else

age = 18

if(age < 18): print("Sei minorenne")
elif(age >= 18 & age < 21): print("Sei maggiorenne ma non puoi bere")
else: print("sei maggiorenne e puoi fare come ti pare")

# condizioni: if, else if, else
# operatori logici: < > == <= => and or

x = 19

if x < 10 : 
    print("x è minore di 10")
elif x == 10:
    print("x è uguale a 10")
else: 
    print("x è maggiore di 10")

if 10 < x < 20:
    print("x è compreso tra 10 e 20 esclusi")

if 10 <= x <= 20:
    print("x è compreso tra 10 e 20 inclusi")

# and presuppone che entrambe le condizioni siano true
if x > 10 and x < 20:
    print("x è compreso tra 10 e 20 esclusi")

# or presuppone che almeno una condizione sia verificata
if x > 10 or x < 20:
    print("x è compreso tra 10 e 20 esclusi")

# not nega la condizione
if not(x > 10):
    print("condizione non verificata")

# if con shorthand (possiamo fare lo shorthand se a if segue solo una istruzione)
if x > 10 : print("x è maggiore di 10")