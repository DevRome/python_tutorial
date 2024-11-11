
# Method chaining
# più metodi eseguiti sequenzialmente
# bisogna fa rrestituire self ad ogni metodo
# return self 


class Car:
    def turn_on(self):
        print("start engine")
        return self

    def drive(self):
        print("drive car")
        return self

    def brake(self):
        print("you stepped on the brakes")
        return self

    def turn_off(self):
        print("turn off engine")
        return self
# end class Car


# istanza dell'oggetto
car1 = Car()
car1.turn_on().drive().brake().turn_off()