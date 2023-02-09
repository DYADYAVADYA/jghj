from tkinter import Tk, Button, Label, Entry,StringVar
root = Tk()
goods = [{'Total price':int(input(f'Введіть вартість {i} товару ')),'Name':input(f'Введіть назву {i} товару '),'Weigh':int(input(f'Введіть вагу {i} товару(в кілограмах) '))} for i in range(1,4)]
print(goods)
var = StringVar()
entry = Entry(textvariable=var)
entry.pack()

lb = Label()


def fn():
    l = list(filter(lambda el: el['Name'] == var.get(), goods))[0]
    lb.config(text=l['Total price']/l['Weigh'])

lb.pack()
Button(text='Отримати',command=fn).pack()
root.mainloop()

