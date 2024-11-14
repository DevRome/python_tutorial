from tkinter import *

# funzione del pulsante collegato alla barra
def submit():
    print(f"La temperatura è: {scale.get()} °C")

# creazione finestra
window = Tk()

# creo una immagine per la bar
image = PhotoImage(file="./Tkinter/snowflakes_icon.png")
label = Label(image=image)
label.pack()

# costruttore dell'oggetto Scale
scale = Scale(window, 
              from_=100, 
              to=0,
              length=400,
              orient=VERTICAL,
              font=("Consolas", 10),
              tickinterval=10, # aggiunge indicatori numerici per il valore
              showvalue=0, # nascondi il valore attuale
              resolution=5, # incremento per il valore
              troughcolor="#69eaff",
              fg="#00ff00",
              bg="#222"
              )

scale.set(50) # valore iniziale
scale.pack()

# pulsante per inviare dati a video
button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()