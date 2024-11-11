# sort() method   = usato con le Lists, NON con Tuple,Set e Dictionary
# sort() function = usato con gli iterables


# sort in ordine alfabetico
students = ["Andrea", "Daniele", "Michele", "Federico"]
students.sort()

for i in students:
    print(i)


# sort(reverse) in ordine alfabetico inverso
students = ["Andrea", "Daniele", "Michele", "Federico"]
students.sort(reverse=True)

for i in students:
    print(i)


# sort, funzione per le Tuple
students = ("Andrea", "Daniele", "Michele", "Federico")
sorted_students = sorted(students)

for i in sorted_students:
    print(i)


# sort(reverse), funzione per le Tuple 
students = ("Andrea", "Daniele", "Michele", "Federico")
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)


# ordinare una lista di Tuple in base al nome, al voto, all'età:
students = [
    ("Andrea", "A", 55),
    ("Daniele", "D", 35),
    ("Lorenzo", "C", 33),
    ("Michele", "B", 18)
    ]

# ordiniamo in base al parametro che passiamo, che corrisponde ad uno dei campi delle tuple
grade = lambda grades : grades[0]
students.sort(key=grade)
for i in students:
    print(i)

grade = lambda grades : grades[1]
students.sort(key=grade)
for i in students:
    print(i)

grade = lambda grades : grades[2]
students.sort(key=grade)
for i in students:
    print(i)

# possiamo anche passare un parametro reverse all'ordinamento
grade = lambda grades : grades[0]
students.sort(key=grade, reverse= True)
for i in students:
    print(i)


# Ordiniamo una tupla di tuple
students = (
    ("Andrea", "A", 55),
    ("Daniele", "D", 35),
    ("Lorenzo", "C", 33),
    ("Michele", "B", 18)
    )
grade = lambda grades : grades[0]
sorted_students = sorted(students, key=grade)
for i in students:
    print(i)