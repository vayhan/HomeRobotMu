import tkinter as tk
import os

root = tk.Tk()
root["bg"] = "white"
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print ( screen_width )
print ( screen_height )


leftGAP = 300
topGAP = 300
lineX0 = ( screen_width - leftGAP ) / 2

canvas = tk.Canvas(root)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print ( screen_width )
print ( screen_height )

canvas.config(background='white')
canvas.create_oval(65, 70, 135, 150, fill="black",width=0)
canvas.create_rectangle(50, 70, 150, 120, fill='white',width=0 )
canvas.create_line(50, 120, 150, 120,width=10)

canvas.create_oval(165, 70, 235, 150, fill="black")
canvas.create_rectangle(150, 70, 250, 120, fill='white',width=0 )
canvas.create_line(150, 120, 250, 120,width=10)

canvas.pack()

root.mainloop()
