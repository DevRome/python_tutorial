# OOP in Python

class Persona:

    # costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    # metodi
    def saluta(self):
        print("ciao, sono " + self.nome)

# // end Persona class

persona1 = Persona("Lorenzo", "Raspa")
persona2 = Persona("Marco", "Columbro")

persona1.saluta()

print(type(persona1))

# cancellare una proprietà
del persona1.nome 

# cancellare un oggetto
del persona2 


# eredità
class Insegnante(Persona): 
    def __init__(self, nome, cognome, materia): # costruttore classe child
        super().__init__(nome, cognome) # riferito al costruttore della classe parent
        self.materia = materia
    
    # override metodo saluta
    def saluta(self):
        print("salve, sono la prof." + self.nome + self.cognome)

# // end Insegnate class


insengnate1 = Insegnante("Carla", "Signorini","Matematica")
insengnate1.saluta()