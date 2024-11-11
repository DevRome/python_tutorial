# Multi Eredità - Multiple Inheritance
# Una classe Child eredità da più classi Parent


# Classi Parent: Prey e Predator
class Prey:
    def flee(self):
        print("Questo animale vola")
# end class Prey


class Predator:
    def hunt(self):
        print("Questo animale caccia")
# end class Predator


# classi child
class Rabbit(Prey):
    pass

class Hwak(Predator):
    pass

# classe Fish ha 2 classi Parent
class Fish(Prey, Predator):
    pass


# creiamo delle istanze
rabbit = Rabbit()
hawk = Hwak()

fish = Fish() # fish eredita sia da entrambe le classi Parent: Prey e Predator
fish.flee()
fish.hunt()
