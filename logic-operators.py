
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the conditions (not True = False and viceversa)

temp = 17
is_sunny = False

if temp > 40 or temp < 0:
    print("Extreme temperatures!")
elif temp > 20 and temp < 30:
    print("Ideal climate!")
elif 20 > temp > 5: # sarebbe elif temp > 5 and temp < 20
    print("It's a bit cold")
elif temp > 10 and temp < 18 and not is_sunny:
    print("Really a bad day!")
else:
    print("Nessuno dei casi sopra")