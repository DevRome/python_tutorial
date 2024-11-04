import random


# random() -> genera un random floating point da 0 a 1
number = random.random()
print(number)


# randint() -> genera unn numero random integer
# genera un numero random( da, a )
low = 1
high = 20
number = random.randint(low, high)
print(number)


# choice() -> genera una scelta random in base a quelle che fornimao
opzioni = ("sasso", "forbice", "mano")
print(random.choice(opzioni))



# shuffle -> mischia gli elementi di una lista o tupla a caso
cards = ["2","3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)