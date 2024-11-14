from tkinter import *


window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight

# funzione bottone
def submit():
    food= []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for index in food:
        print(f"hai ordinato: {index}")

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size()) # resize

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
        listbox.config(height=listbox.size()) # resize della listbox senza 1 elemento



# costruttore della listbox
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12,
                  selectmode=MULTIPLE # possiamo selezionare più elementi della lista
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
