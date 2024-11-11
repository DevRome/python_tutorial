# .:: Duck typing ::.
# la classe di un oggetto è meno importante dei metodi / attributi

class Moto():
    def go(self):
        print("Vado in moto")
    
    def stop(self):
        print("Spengo la moto")
# end class Moto


class Macchina():
    def go(self):
        print("Vado in machina")
    
    def stop(self):
        print("Spengo la macchina")
# end class Macchina


class Veicolo():
    def catch(self, moto):
        moto.go()
        moto.stop()
        print("duck typing!")

moto = Moto()
veicolo = Veicolo()
veicolo.catch(moto)

