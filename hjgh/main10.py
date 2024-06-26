from tkinter import *

root = Tk()
root.title("Приложения")
root.geometry("700x500")

ent = Entry(font=('Comic Sans MS', 18, "bold"))
ent.pack()

label = Label(text='')
label.pack()

def click_button():
    val = ent.get()
    label["text"] = val

btn = Button(text='Click meeee', command=click_button)
btn.pack()

root.mainloop()