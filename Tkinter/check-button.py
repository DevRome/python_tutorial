from tkinter import *


window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight

def display():
    if(x.get() == 1): # se qualcuno ha fa toggle su x (guarda valori su onvalue e offvalue)
        print("You agree!")
    else:
        print("You don't agree!!")

# x è riferito ai valori del costruttore onvalue e offvalue
# se stanno settati come Boolean -> la variabile deve essere = BooleanVar()
# se stanno settati come stringa -> la variabile deve essere = StringVar()
# in questo caso qui sotto è settata come IntVar
x = IntVar()

# immagine per la checkbox
photo = PhotoImage(file="./Tkinter/snowflakes_icon.png")

check_buttonn = Checkbutton(window,
                            text="Opzione 1",
                            variable=x,
                            onvalue=1, # Boolean, String, Integer
                            offvalue=0, # Boolean, String, Integer
                            command=display,
                            font=("Arial", 20),
                            fg="#4d4d4d",
                            bg="light blue",
                            activeforeground="#4d4d4d",
                            activebackground="light blue",
                            padx=25,
                            pady=10,
                            image=photo,
                            compound="left"
                            )

check_buttonn.pack()

window.mainloop() # visualizza la window e ascolta per eventi
