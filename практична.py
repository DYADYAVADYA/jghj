from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import fileinput

def func0():
    opn= askopenfilename()
    for l in fileinput.input(opn):
        tex.insert(END,1)

def func1():
    if askyesno('Exit','закрити головне вікно?'):
        root.destroy()
def func3():
    win=Toplevel(root)
root=Tk()
m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
m.add_cascade(label='File', menu=mm1)
mm1.add_command(label='Exit',command=func1)
mm1.add_command(label='Open...',command=func0)
mm2=Menu(m)
m.add_cascade(label='Edit',menu=mm2)
mm2.add_command(label='+1',command=func3)