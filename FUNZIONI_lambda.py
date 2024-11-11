#.:: lambda Functions ::.
# sono funzioni scritte in una linea, usando la keyword lambda
# accettano ogni numero di argomenti, ma ha solo una espressione
# utili se usat per un periodo breve


# es1:
def double(x):
    return x * 2
print(double(5))

# la funzione sopra la possiamo riscrivere anche così
double = lambda x: x * 2
print(double(5))


# es2: con 2 parametri
multiply = lambda x, y: x * y
print(multiply(3, 2))


# es2: con 2 parametri
writeName = lambda firstName, lastName : firstName + " " + lastName 
print(writeName("Lorenzo", "Raspa"))


# es3: con 3 parametri
sum = lambda x, y, z: x + y + z
print(sum(3, 2, 5))


# es4:
age_check = lambda age:True if age >=18 else False
print(age_check(16))