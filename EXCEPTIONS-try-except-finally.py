

# --- Exceptions in Python ---

# try ci permette di testare un blocco di codice
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


# il blocco try ci permette non solo di testare, ma anche di prevenire l'errore che si potrebbe generare da un blocco di codice potenzialmente generatore di errore
# per quanto riguarda le Exceptions: è importante cercare di gestire più possibili eccezioni specifiche, evitano di lasciare solo la gestione generica Exception 
# prendiamo ad esempio la divisione per 0
try:
    dividendo = int(input("Inserire un numero da dividere"))
    divisore = int(input("Inserire il divisore"))
    divisione = dividendo / divisore
    print(divisione)
except ZeroDivisionError:
    print("Non puoi dividere per 0")
except ValueError:
    print("Inserisci solo numeri")
except Exception as errore: # as nome_var possiamo anche mandare a video tutto l'errore segnalato in dettaglio 
    print(f"Errore generico {errore}")
finally:
    print("Termine del programma")
