from tkinter import *
win = Tk()
win.geometry("300x200")
def click():
    x= b.get()
    x = int(x)
    b.delete(0, END)
    year = 2023
    age = year - x
    f.insert(END, "We are in the year 2023 and you are \n")
    f.insert(END, str(age) + " years old.")
a = Label(win, text="Welcome and thank you for using my age calculator. \n\n Please what is your year of birth ?")
a.pack()
b = Entry(win, width= 35)
b.pack()
e = Button(win, text="Calculate", command=click)
e.pack()
f = Text(win, height = 5, width = 35)
f.pack()
win.mainloop()
