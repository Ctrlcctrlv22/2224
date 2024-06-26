import tkinter as tk 

def open_second_window():
    main_window.withdraw()
    second_window.deiconify()

def back_to_main_window():
    second_window.withdraw()
    main_window.deiconify()


main_window = tk.Tk()
main_window.title("Main Window")
main_window.geometry("500x500")
main_window.configure(bg="#0e0326")


txt = tk.Label(main_window, text='Main window', font=('Comic Sans MS', 20,'bold'), bg="#0e0326", fg="#fab905")
txt.pack()


open_button = tk.Button(main_window, text="Open Second Window", command=open_second_window)
open_button.pack(pady=20)


second_window = tk.Toplevel(main_window)
second_window.title("Second Window")
second_window.geometry("500x500")
second_window.configure(bg="#9dfc03")
second_window.withdraw()



txt1 = tk.Label(second_window, text='Second window', font=('Comic Sans MS', 20, 'bold'), bg="#0e0326", fg="#fab905")
txt1.pack()


back_button = tk.Button(second_window, text="Back to Main Window", command=back_to_main_window)
back_button.pack()


main_window.mainloop()