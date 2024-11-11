#.:: Zip Functions ::.
# aggreghiamo elementi da 2 o più iterables (list, tuple, sets, dictionary) e crea un oggetto zip con gli elementi abbinati in tupla

username = ["Lorenzo", "Andrea", "Daniele"]
passwords = ("pass@word", "pass123", "turk@pass")

users = zip(username, passwords)

for i in users:
    print(i)

# se facciamo un type dell'oggetto ottenuto, vedremo che sarà un oggetto zip, quindi possiamo fare un cast con altri tipi di collections
print(type(users))

user_in_list = list(users)
for i in user_in_list:
    print(i)

user_in_dictionary = dict(users)
for key, value in user_in_dictionary.items():
    print(f"{key}: {value}")