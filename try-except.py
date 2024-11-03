

# --- Exceptions in Python ---

# try ci permette di tesate un blocco di codice
# except cattura un eventuale errore (ci sono molte tipologie di errore che except intercetta)

try:
    x = 10
    print(x + "ciao") # errore perché non si può unire  stringa con intero
except NameError:
    print("Eccezione di tipo NameError")
except: # exception generica
    print("C'è stato unn errore")
finally:
    print("Il blocco finally viene comunque eseguito")