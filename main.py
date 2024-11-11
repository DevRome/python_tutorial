import modulo_prova

print(__name__)
print(modulo_prova.__name__)

if __name__ == "__main__":
    print("eseguiamo questo modulo direttamente, non è importato")
else:
    print("questo modulo non è eseguito direttamente")

