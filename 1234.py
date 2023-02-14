from tkinter import *
from tkinter.filedialog import *
import fileinput
def func1():
    opn= askopenfilename()
    for l in fileinput.input(opn):
        tex.insert(END,1)
def func2():
    sav= asksaveasfilename() 
    lat= tex.get(1.0,END)
    nk=open(sav,'w')
    nk.write(lat)
    nk.close()
def func3():
    win=Toplevel(root)
    
root=Tk()
m=Menu(root)
root.config(menu=m)
mm1=Menu(m)
m.add_cascade(label='File',menu=mm1)
mm1.add_command(label='Open...',command=func1)
mm1.add_command(label='Save...',command=func2)
tex=Text(root,width=50,height=20,font='12')
tex.pack()
root.mainloop()

    