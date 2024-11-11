# .:: Abstract ::.
# è da considerare come un template, che impedisce all'utente di creare oggetti di quella classe abstract
# impone all'utente di fare l'override dei metodi della classe abstract nelle classi child
# una classe abstract dunque contiene abstract methods
# un metodo astratto contiene la dichiarazione, ma non l'implementazione


# classe abstract:
# mettiamo che vogliamo imporre all'utente di creare oggetti della classe Veicolo perché troppo generica
# la definiamo dunque Abstract, imoprtando il modulo ABC(Abstract Base Classes)
from abc import ABC, abstractmethod
class Veicolo(ABC):
    
    @abstractmethod # dobbiamo mettere questo tag per ogni metodo astratto che creiamo
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
# edn abstract class Veicolo


# classe Child
class Moto(Veicolo):
    def go(self):
        print("Vado in moto")
    
    def stop(self):
        print("Spengo la moto")
# end class Moto


# classe Child
class Macchina(Veicolo):
    def go(self):
        print("Vado in machina")
    
    def stop(self):
        print("Spengo la macchina")
# end class Macchina


veicolo1 = Veicolo() # genera errore: Can't instantiate abstract class Veicolo with abstract method go
