from tkinter import *


window = Tk() # istanza di una window
window.geometry("800x420") # WidthxHeight

food = ["Pizza", "Hamburger", "Hot Dog", "Ramen"]

# creiamo delle immagini per i nostri radio buttons
pizzaImage = PhotoImage(file="./Tkinter/pizza_icon.png")
hamburgerImage = PhotoImage(file="./Tkinter/hamburger_icon.png")
hotDogImage = PhotoImage(file="./Tkinter/hot-dog_icon.png")
ramenImage = PhotoImage(file="./Tkinter/ramen_icon.png")

foodImages= [pizzaImage, hamburgerImage, hotDogImage, ramenImage]


# variabile che raggruppa i radio buttons
x = IntVar()


# funzione che utilizzeranno i buttons
def order():
    if(x.get()== 0): print("Hai ordinato una pizza")
    elif(x.get()== 1): print("Hai ordinato un hamburger")
    elif(x.get()== 2): print("Hai ordinato un hot dog")
    elif(x.get()== 3): print("Hai ordinato ramen")


# carico i buttons a video
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index], # aggiunge testo ai radio button
                               variable=x, # raggruppa i radio button insieme 
                               value=index, # assegna ad ogni radio button un valore diverso
                               padx=25,
                               pady=10,
                               font=("Sans Seriff", 15),
                               image= foodImages[index], # aggiunge le immagini ai bottoni
                               compound= "left", # posizione delle immagini rispetto al button
                               # indicatoron=0, # elimina il cerchietto
                               width=300, # imposta la width del radio button
                               command=order # funzione collegata ai buttons
                               )
    radio_button.pack(anchor=W)


window.mainloop() # visualizza la window e ascolta per eventi
