# input()= una funzione che permette all'utente d inserire dati
# restituisce i dati inseriti come stringa

base = input("Inserisci la base del rettangolo:")
altezza = input("inserisci l'altezza del rettangolo:")
area = 0

try:
    area = base * altezza
except Exception as e:
    print("Errore intercettato:", e)

# restituisce errore che viene intercettato in quanto input() restituisce un dato tipo string che non può essere elaborato come float o integer