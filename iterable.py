# ITERABLE

# qualsiasi oggetto/collection che può restituire i suoi stessi elementi è cinsiderata iterable
# di conseguenza, un iterable, può essere iterato in un loop.
# List [], Tuple(), Set{}, strings, Dictionary{} 


# iterazione su List
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")

for number in reversed(numbers):
    print(number, end="-")


# iterazione su Tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number, end="_")
  
numbers = (1, 2, 3, 4, 5)
for number in reversed(numbers):
    print(number, end="_")


# iterazione su Set
fruits= {"banana", "arance", "meloni"}
for frut in fruits:
    print(frut, end="@")


# iterazione su strings
myString = "Ciao!"
for char in myString: print(char, end=" ")


# iterazione su dictionary
# dictionary ha un'iterazione leggermente diversa rispetto agli altri, per mostrare key e values
my_dictionary = {
    "A": 1,
    "B": 2,
    "C": 3
}

for key in my_dictionary.keys():
    print(key)

for value in my_dictionary.values():
    print(value)

for key, values in my_dictionary.items():
    print(f"{key} = {value}")