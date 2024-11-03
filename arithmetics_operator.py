import math

# Some Math functions and math operators
# + - * / 
print(1 + 1)
print(1 - 1)
print(2 * 2)
print(6 / 2)

# %
print("2 elevato alla 3: ", 2^3)

# += *= /= -=
print(1 + 1)
print(1 + 1)
print(1 + 1)
print(1 + 1)

# round() abs() pow() 
print(round(3,14))
print(abs(-4))
print(pow(2, 3))

# max() min()
x = 2
y = 3
z = 5
print(max(x,y,z))
print(min(x,y,z))

# funzioni importate da modulo math
print(math.pi)
print(math.e)
print(math.sqrt(121))
print(math.ceil(9.8))
print(math.floor(9.8))
print(math.sin(90))
print(math.cos(90))


# --- operatori aritmetici: + - * / // % ** += -= *= /=

x = 5
y = 10

print(x // 2) # 5 // 2 = 2 divisione arrotondata
print(x ** 2) # 5^2 = 25 potenza
print(x % 2) # stampa il resto della divisione, 1 in questo caso


# --- funzioni aritmetiche built-in: min, max, abs, pow

x = min(5, 10, 25) #min = valore minimo
print(x) #5

x = max(5, 10, 25) #max = valore max
print(x) #25

x = abs(-5) #abs = valore assoluto, toglie il segno
print(x) #5

x = pow(3, 2) #pow = potenza
print(x) #5

# importo funzioni matematiche
import math

print(math.sqrt(64)) # 8.0
print(math.floor(2.50)) # 2 arrotonda per difetto
print(math.ceil(2.50)) # 3 arrotonda per eccesso