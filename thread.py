# Thread
# Thread è una suddivisione di un processo in due o più istanze (o sottoprocessi)

# con il multithreading, i thread vengono eseguiti concorrentemente, quindi non veramente in parallelo, i thread si eseguono a turno, quando lo stato degli altri thread sta in idle

# con il multiprocessing, i thread vengono eseguiti realmente in parallelo

# quindi, possiamo avere più d un thread, come ad esempio uno che gestisce un timer di un gioco, un altro che accetta l'input di un utente, ecc.
# Ogni thread può avere un ordine separato di istruzioni

# qui sotto facciamo un programma che usa il multithreading, ogni thread gestirà una parte del programma
import threading
import time

def eat_breakfats(cibo1, cibo2):
    time.sleep(3)
    print("hai finito colazione")

def drink_coffee():
    time.sleep(4)
    print("hai finito il caffé")

def study():
    time.sleep(5)
    print("hai finito di studiare")

# impostiamo un thread per ogni funzione, in modo da non farle eseguire sequenzialmente, in quanto solo un thread gestisce tutto al momento
# il tempo totale di esecuzione sarà solo 5 secondi, quello impostato più a lungo
x = threading.Thread(target=eat_breakfats, args=("pane", "nutella"))
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# se avessi richiamato le funzioni così, solo il main thread sarebbe stato in carico a gestire tutto, ed avrebbe impiegato complessivamente 12 secondi per terminare
# eat_breakfats()
# drink_coffee()
# study()

print(threading.active_count()) 
print(threading.enumerate())
print(time.perf_counter())