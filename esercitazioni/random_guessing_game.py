import random

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("-------- INDOVINA IL NUMERO --------")
while is_running:
    guess = input(f"Indovina il numero tra: {lowest_num} e {highest_num}\nQ per uscire\n")
    if guess.isdigit():

        if int(guess) < lowest_num or int(guess) > highest_num:
            print(f"Numero fuori dal range: {lowest_num} - {highest_num}")
        
        if (int(guess) > answer): print("Numero digitato più grande del numero da indovinare")
        
        if (int(guess) < answer): print("Numero digitato più piccolo del numero da indovinare")

        if int(guess) == answer: 
            print("Bravo, hai indovinato!")
            is_running = False
    elif(guess == "q"): break
    else:
        print("Digita un numero, non testo")