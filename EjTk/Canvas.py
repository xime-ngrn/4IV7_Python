from tkinter import *

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand="yes", fill="both")
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)

canva=Canvas(bg="white", height="200", width="300")
canva.create_arc((5,10,150,200),start = 0,extent = 150, fill= "pink")
canva.pack()

mainloop()