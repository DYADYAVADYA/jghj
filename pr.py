from tkinter import Tk, Button, Label, Entry,StringVar
root = Tk()
a = {
    'Михайлина':166,
    'Сашко': 178
}
var = StringVar()
entry = Entry(textvariable=var)
entry.pack()
lb = Label()
lb.pack()
Button(text='Отримати',command=lambda:lb.config(text=a[var.get().capitalize()])).pack()
root.mainloop()