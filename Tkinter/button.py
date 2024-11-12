from tkinter import *


window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight

# immagine per il pulsante
photo = PhotoImage(file="./Tkinter/snowflakes_icon.png")

count = 0

# funzione collegata come callback al pulsante
def click():
    global count
    count+=1
    print(f"Hai cliccato il bottone {count} volte")

button = Button(window,
                text="Click Me!",
                command=click, # funzione richiamata al click
                font=("Comic Sans", 38),
                fg="#00ff00",
                bg="#222",
                activeforeground="#00ff00",
                activebackground="#222",
                state=ACTIVE, # abilita/ disabilita ACTIVE, DISABLED
                image=photo,
                compound="bottom" # posizione dell'immagine rispetto al tetso
                )
button.pack()

window.mainloop() # visualizza la window e ascolta per eventi
