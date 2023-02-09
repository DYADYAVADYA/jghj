from tkinter import Tk,Menu
root = Tk()
m = Menu(root)
root.config(menu=m)
help = Menu(root)
file = Menu(root)
m.add_cascade(label='File',menu=file)
m.add_cascade(label='Help',menu=help)
file.add_command(label='New',command=lambda:Tk().mainloop())
file.add_command(label='Exit',command=lambda:quit())

root.mainloop()