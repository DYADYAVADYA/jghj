from tkinter import Tk,Menu
root = Tk()
m = Menu(root)
root.config(menu=m)
edit = Menu(root)
debug = Menu(root)
m.add_cascade(label='Debug',menu=debug)
m.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Cut')
edit.add_command(label='Copy')
debug.add_command(label='Configure')
root.mainloop()