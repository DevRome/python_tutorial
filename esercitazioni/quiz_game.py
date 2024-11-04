# quiz game utilizzando tuple e list

# elenco delle domande poste al giocatore
questions = ("Quanti elementi ci sono nella tabella periodica?",
             "Quale animali depone le uova più grandi?",
             "Qual è il gas più abbondante nell'atmosfera?",
             "Quante ossa ci sono nel corpo umano?",
             "Qual è il pinaeta più caldo nel sistema solare?"
             )

# risposte disponibili per ogni domanda
options =(
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Balena", "B. Coccodrillo", "C. Elefante", "D. Struzzo"),
    ("A. Nitrogen", "B. Ossigeno", "C. Ossido di Carbonio", "D. Idrogeno"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercurio", "B. Venere", "C. Terra", "D. Marte"),
    )

answers = ("C", "D", "A", "A", "B") # risposte giuste
guesses = [] # list delle risposte date
score = 0 # punteggio che si andrà ad incrementare se le risposte sono giuste
question_num = 0 # contatore della domanda corrente


# display a video le domande
for question in questions:
    print("-------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Inserisci la risposta: A, B, C, D \n").upper()
    guesses.append(guess)

    # se la risposta è giusta incrementa lo score  
    if guess == answers[question_num]: 
        score += 1
        print("Risposta corretta!")
    else:
        print("Risposta errata :(")

    # incrementa l'indice
    question_num += 1

# stampa punteggio finale
print(f"Punteggio totale: {score}")