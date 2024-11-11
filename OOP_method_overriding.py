
# Method overriding
# è la possibilità di una Child class di implementare una versione specifica di un metodo già dichiarato nella classe Parent.


# class Parent
class Animal:
    def eat(self):
        print("This animal is eating")
# end class Animal


# class Child
class Rabbit(Animal):
    def eat(self):
        print("This rabbit eats carrots")
# end class Rabbit


# istanza dell'oggetto
rabbit = Rabbit()
rabbit.eat() # I eat Carrots / override del metodo