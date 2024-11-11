#.:: reduce() ::.
# applica una funzione ad ogni item dell'iterable: lists, tuple ecc), riducendolo ad un singolo valore cumulativo
# reduce applica una funzione sui primi 2 elementi della lista e poi ripete il processo ino a che rimane solo un valore
# reduce(function, iterable)
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

# la funzione agisce prima sui primi 2 elementi, unendoli HE
# poi unisce HEL
# poi unisce HELL
# infine unisce HELLO