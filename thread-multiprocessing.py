# .:: Thread - Multiprocessing ::.

# Multiprocessing: sono Thread (quindi tasks) eseguiti realmente in parallelo su più cores del processore
# possiamo quindi creare processi, su più core, che vengono eseguiti in parallelo
# il multiprocessing è utile per CPU bound task, quando c'è un uso di CPU importante

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(500000000,)) # assegnazione di un processo alla funzione counter
    b = Process(target=counter, args=(500000000,)) # assegnazione di un processo alla funzione counter
    
    a.start()
    b.start()

    a.join() # il main process aspetterà che sia finito il child process prima di continuare
    b.join()

    print("finished in: ", time.perf_counter(), " seconds")

if __name__ == "__main__":
    main()