# .:: Deamon Thread ::.

# è un thread che viene eseguito in background
# non è importante per l'esecuzione di un progamma
# il nostro programma non aspetterà che il deamon thread venga completato per uscire, come invece fa con i thread normali
# non-deamon threads non possono essere uccisi, restano vivi finché il task è completato

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"logged in for: {count} seconds")

# imposto la funzione come daemon thread
x = threading.Thread(target=timer, daemon=True)
x.start()

# potevo impostare il thread a daemon anche così
# x.setDaemon(True)
# posso anche vedere se un Thread è un daemon
# print(x.isDaemon)

# quando esco dal programma, il thread daemon che gestisce la funzione Timer viene ucciso, cosa che invece non sarebbe accaduta se fosse stato un thread normale
answer = input("Do you want exit?")
