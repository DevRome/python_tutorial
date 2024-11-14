from tkinter import *
from tkinter import messagebox # da importare a parte

# istanza window
window = Tk()

# funzione del button, con varie message boxes
def click():

    messagebox.showinfo(
        title="Info box",
        message="C'ho un sonno!!"
    )

    messagebox.showwarning(
        title="Attezione",
        message="Hai un virus!!"
    )

    messagebox.showerror(
        title="Errore di Python",
        message="Qualcosa è andato storto"
    )


    # ask or cancel
    if messagebox.askokcancel(
        title="Ask or cancel",
        message="Domani andiamo lì?"
    ):
        print("Hai premuto ok, domani andiamo lì")
    else:
        print("no, hai premuto cancel!")
    

    # Ask Retry, Cancel
    if messagebox.askretrycancel(
        title="Retry or cancel",
        message="Riproviamo o no?"
    ):
        print("Hai premuto retry, domani riandiamo lì")
    else:
        print("no, hai premuto cancel!")


    # Ask Yes or No
    if messagebox.askyesno(
        title="Yes or No",
        message="Ti piace la pasta?"
    ):
        print("Ti piace la pasta")
    else:
        print("Non ti piace la pasta")

    
    # Ask question - restituisce una string: yes / no
    answer = messagebox.askquestion(
        title="Ask question",
        message="Ti piace ballare?"
    )
    print(answer)


    # Ask Yes, No, Cancel 
    answer = messagebox.askyesnocancel(
        title="Ask Yes No Cancel",
        message="Ti piace programmare?",
        icon="info" # info - error
    )
    if(answer == True): print("Ti piace programmare")
    elif(answer == False): print("Non ti piace programmare")
    else: print("non vuoi rispondere...")


button = Button(window, command=click, text="click me!").pack()


window.mainloop()