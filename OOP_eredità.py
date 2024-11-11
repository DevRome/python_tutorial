# .:: OOP in Python - Eredità ::.
# le classi child ereditano attributi e metodi dalla classe Parent
# 
# vantaggi: 
# non dovremo copiare lo stesso codice della classe Parent in tutte le classi Child
# se modifichiamo un attributo nella classe Parent, la modifica verrà estesa anche alle classi Child, senza dover modificare ogni classe Child

# Classe Parent
class Persona: # Dichiarazione della classe

    # attributi
    eyesColor = None
    hairColor = None
    height = None

    # costruttore
    # self: si riferisce all'oggetto stesso
    def __init__(self, nome, cognome):
        self.name = nome
        self.lastname = cognome
    
    # metodi
    def saluta(self):
        print(f"ciao, sono {self.name} {self.lastname}")

# // end Persona class


# Classe child
# eredita tutti gli attributi e metodi della classe Parent
class Insegnante(Persona): 
    def __init__(self, name, lastname, materia): # costruttore classe child
        super().__init__(name, lastname) # riferito al costruttore della classe parent
        self.materia = materia
    
    # override metodo saluta
    def saluta(self):
        print(f"ciao, sono {self.name} {self.lastname}, insegnate di {self.materia}")

# // end Insegnate class


insengnate1 = Insegnante("Carla", "Signorini","Matematica")
insengnate1.saluta()