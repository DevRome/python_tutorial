from tkinter import *

window = Tk()
window.geometry("450x300")

# creo un ogg.PhtoImage per l'immagine della label
photo = PhotoImage(file="./Tkinter/snowflakes_icon.png")

# creiamo la ogg.Label e lo mettiamo nella window
# alcune props:
label = Label(
    window, 
    text="Ciaoo!!", 
    font=("Arial", 40, "bold"),
    fg="#eee",
    bg="black",
    relief=RAISED, # tipo bordo: RAISED, SUNKEN
    bd=10, # spessore bordo
    padx=10, # aggiungiamo pad x e y
    pady=30,
    image=photo,
    compound="bottom" # l'immagine sarà sotto la nostra label
    ) 

# pack per inserire la label in window
# di default pack inserisce la label in alto al centro
label.pack() 

# posizioniamo la label dove voglamo
label.place(x=100, y=20)


window.mainloop()