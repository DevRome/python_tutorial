from tkinter import *


window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight

# funzioni bottons
def submit():
    print(f"hai ordinato: {listbox.get(listbox.curselection())}")

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size()) # resize della listbox senza 1 elemento

def delete():
    listbox.delete(listbox.curselection()) # elimina l'elemento selezionato
    listbox.config(height=listbox.size()) # resize della listbox senza 1 elemento


# costruttore della listbox
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12,
                  )

# setto l'altezza in automatico
listbox.config(height=listbox.size())

# elementi della lista
listbox.insert(1, "pizza")
listbox.insert(1, "pasta carbonara")
listbox.insert(1, "cacio e pepe")
listbox.insert(1, "amatriciana")

listbox.pack()

# textbox
entryBox = Entry(window)
entryBox.pack()

# submit button
submit_button = Button(window, text="Submit", command=submit).pack()

# add button
add_button = Button(window, text="Add", command=add).pack()

# delete button
delete_button = Button(window, text="Delete", command=delete).pack()




window.mainloop() # visualizza la window e ascolta per eventi
