# un modulo è come se fosse una libreria, un insieme di classi, funzioni che vogliamo includere nel nostro progetto per svolgere determinate operazioni 
# i moduli sono usati in programmazione modulare, ossia separare un programma in parti

# esempio di modulo built-in di python
import platform
currentOperatingSystem = platform.system()
print(currentOperatingSystem)

# esempio di modulo built-in di python
import math
print(math.floor(2.90))

# dir è una funzione che ci permette di vedere che abbiamo a disposzione in un modulo
print(dir(math))

# importo il modulo
import modulo_prova

# posso anche importare con un alias
import modulo_prova as mp

# importo una funzione del modulo
modulo_prova.saluta("Lorenzino")

# importo una variabile del modulo
x = modulo_prova.persona1
print(x)

# importare solo una parte di un modulo
# qui sotto abbiamo importato solo la variabile persona1
from modulo_prova import persona1
print(persona1["nome"])

# importo una classe dal file modulo_prova_2.py
from modulo_prova_2 import Car
car1 = Car()
car1.getMaxSpeed()

