# in / not in
# controlla se c'è o non c'è e restituisce un boolean


# es 1:
word = "APPLE"
letter = input("Indovina una lettera nella parola segreta: ")

# in
if letter.upper() in word: print(f"Hai indovinato, {letter} è presente nella parola")
else: print(f"{letter} non è presente nella parola")

# not in
if letter.upper() not in word: print(f"{letter} non è presente nella parola")
else: print(f"Hai indovinato, {letter} è presente nella parola")



# es2:
students = {"Lorenzo", "Daniele", "Andrea"}
student = input("Inserisci il nome di uno studente")
if student in students: print(f"{student} è presente nella lista")



# es3:
students = {
    "Lorenzo":"Ingegneria",
    "Andrea":"Fisioterapia",
    "Daniele": "Marketing"
}
student = input("Inserisci il nome dello studente da cercare")
if student in students: 
    print(f"{student} sta studiando: {students[student]}")
else:
    print(f"{student} non è stato trovato")



# es4:
email = "brocode@gmail.com"
if "@" in email and "." in email:
    print("valid mail")
else:
    print("not valid mail")