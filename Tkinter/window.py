from tkinter import *

# differenza tra widgets e windows
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = container per i widgets

window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight
window.title("Prima Gui Program") # titolo

# per creare una icona dobbiamo convertire l'icona che abbiamo in PhotoImage, poi la possiamo usare 
icon = PhotoImage(file="./Tkinter/snowflakes_icon.png") 
window.iconphoto(True, icon)

# window background color, valore esadecimale o anche per nome, es: "green"
window.config(background="#222222")

window.mainloop() # visualizza la window e ascolta per eventi
