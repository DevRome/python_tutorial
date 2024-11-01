# validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. usernae must not contain digits

answer = "Y"

while(answer=="Y"):
    
    # prompt utente
    myString = input("Inserisci qui sotto la stringa:\n")

    # .:: procedo con i controlli ::.

    # numero caratteri in stringa
    if len(myString) > 12 : print("numero caratteri in stringa maggiori di 12")
    
    # numero spaces
    if myString.count(" ") >= 1: print("ci sono degli spazi nella stringa")
    
    if not myString.isalpha(): print("la stringa contiene dei numeri")

    # Y = ricomincio programma, N = Esco
    answer = input("Vuoi inserire un'altra stringa? Y / N \n")

