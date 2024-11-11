# OOP in Python
# una classe è un blueprint che serve a desrivere quali attributi e metodi avrà l'oggetto generato dalla classe stessa
# un oggetto è un'istanza di una classe


class Persona: # Dichiarazione della classe

    # attributi o class variables
    eyesColor = None
    hairColor = None
    height = 1.78

    # costruttore
    # self: si riferisce all'oggetto stesso
    def __init__(self, nome, cognome):
        self.name = nome            # instance variables
        self.lastname = cognome     # instance variables
    
    # metodi
    def saluta(self):
        print(f"ciao, sono {self.name} {self.lastname}")

# // end Persona class


# due istanze della classe Persona
persona1 = Persona("Lorenzo", "Raspa")
persona2 = Persona("Marco", "Columbro")

# richiamo un metodo
persona1.saluta()
persona2.saluta()

# stampo il tipo di dato (restituisce il nome della classe)
print(type(persona1))

# cancellare una proprietà
del persona1.name 

# cancellare un oggetto
del persona2 

