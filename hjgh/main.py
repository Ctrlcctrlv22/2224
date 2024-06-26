from tkinter import *

root = Tk()
root.title("Приложения")
root.geometry("700x500")
root.configure(bg="#0e0326")

txt = Label(root, text='Best App in the world', font=('Comic Sans Ms', 20, 'bold'), bg="#0e0326", fg="#fab905")
txt.pack()

frame= Frame(root, bg="#0e0326")
frame.pack(anchor='center')

btn1 = Button(frame, text='home', bg='#fab100', fg='#0e0', font=('Caslon', 14, 'bold'))
btn2 = Button(frame, text='home', bg='#fab200', fg='#0e0', font=('Caslon', 14, 'bold'))
btn3 = Button(frame, text='home', bg='#fab300', fg='#0e0', font=('Caslon', 14, 'bold'))
btn4 = Button(frame, text='home', bg='#fab400', fg='#0e0', font=('Caslon', 14, 'bold'))


btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=0, column=2, padx=10, pady=10)
btn4.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
