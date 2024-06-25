from tkinter import *

def finish():
    root.destroy()
    print('приложение закрыто')

root = Tk()
root.title("Приложение")
root.geometry("700x350")
root.minsize(100,100)
#root.maxsize(900, 500)
root.protocol("WM_DELETE_WINDOW", finish)
#root.attributes("-fullscreen", True)
root.attributes("-alpha", 1)

icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

#label = Label(text= 'clicker cabibaraahahhahahahhaahaxd')
#label.pack()

clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn["text"] = f"clicks {clicks}"

btn = Button(text='Click ', command=click_button)
btn.pack()

def click_button1():
    root.attributes("-fullscreen", True)   
    
def click_button2():
    root.attributes("-fullscreen", False)
   
def finish():
    root.destroy()

btn = Button(text='Click me', command=click_button1)
btn.pack()

btn = Button(text='dont click me', command=click_button2)
btn.pack()


btn = Button(text='close', command=finish)
btn.pack()

btn = Button(text='clicks', state=["disabled"])
btn.pack()



root.mainloop()