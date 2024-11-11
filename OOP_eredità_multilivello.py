# Multilevel Inheritance
# una classe Child eredità da un'altra classe Child


# Parent class
class Organism:
    alive = True
# end class Organism


# Child class
class Animal(Organism):
    def eat(self):
        print("Questo animale mangia")
# end class Animal


# Multilevel Inheritance Class
# Dog eredita da Animal e da Organism
class Dog(Animal):
    def abbaia(self):
        print("Questo cane abbaia")
# end class Dog


# istanzio un oggetto
dog = Dog()
print(dog.alive) # attibuto della classe Parent Organism
dog.eat()        # metodo della classe Child Animal
dog.abbaia()     # metodo della classe Dog
