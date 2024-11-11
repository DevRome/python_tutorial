#.:: Dictionary Comprehension ::.
# un modo per creare un nuovo dictionary con meno sintassi
# dictionary = {key: expression for (key, value) in iterable}

cities_in_F = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50
}

# vogliamo trasormare queste temperature delle città da Farenheit in Celsius

cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}

print(cities_in_C)