from tkinter import *


window = Tk() # istanza di una window
# window.geometry("800x420") # WidthxHeight


# funzioni dei pulsanti
def submit():
    username = entry.get()
    print(f"Hello {username}")

def delete():
    entry.delete(0, END) # carattere iniziale -> carattere finale

def cancel():
    entry.delete(len(entry.get())-1, END) # carattere iniziale -> carattere finale


# creiamo la entry (textbox)
entry = Entry(window,
              font=("Arial", 20),
              fg="#e0e0e0",
              bg="#2e2e2e",
            )

entry.insert(0, "Default text") # defaultText
entry.config(state="normal")    # disabled, normal, readonly
entry.config(show="*")

entry.pack()


# creiamo il submit button
submit_button = Button(window,
                       text="submit",
                       command=submit
                       )

submit_button.pack(side=RIGHT)


# creiamo il delete button
delete_button = Button(window,
                       text="delete",
                       command=delete
                       )

delete_button.pack(side=RIGHT)


# creiamo il cancel button
cancel_button = Button(window,
                       text="cancel",
                       command=cancel
                       )

cancel_button.pack(side=RIGHT)


window.mainloop() # visualizza la window e ascolta per eventi
