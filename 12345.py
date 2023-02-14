from tkinter import *
from tkinter.messagebox import *

def func1():
    if askyesno('Exit','закрити головне вікно?'):
        root.destroy()
def func2():
    showinfo('Editor','виконано успішно')
root=Tk()
m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
m.add_cascade(label='File', menu=mm1)
mm1.add_command(label='Exit',command=func1)
mm2=Menu(m)
m.add_cascade(label='Help',menu=mm2)
mm2.add_command(label='about',command=func2)
root.mainloop()

