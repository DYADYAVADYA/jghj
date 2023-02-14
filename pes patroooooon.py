from tkinter import*

window = Tk()

canvas = Canvas(window, width = 500, height = 500)

canvas.create_rectangle(0,350, 500,500, fill = "green")
canvas.create_rectangle(150,150, 350,370, fill = "white")
canvas.create_polygon(100,150, 250,25, 400,150, fill = "red", outline = "black")
canvas.create_rectangle(210,250, 290,370, fill = "white")
canvas.create_oval(215,305, 235,325)
canvas.create_oval(170,170, 230,230)
canvas.create_oval(330,170, 270,230)
canvas.create_oval(50,50, 100,100, fill = "yellow")
canvas.create_line(30,30, 50,50)
canvas.create_line(75,30, 75,45)
canvas.create_line(105,75, 125,75)
canvas.create_line(75,105, 75,135)
canvas.create_line(50,105, 30, 125)

canvas.pack()

window.mainloop()