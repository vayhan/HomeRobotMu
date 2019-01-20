from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.attributes("-fullscreen", True)
img = ImageTk.PhotoImage(Image.open("TTT.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

myCanvas = Canvas(root)
myCanvas.pack()
myCanvas.create_oval(40, 150, 100, 200, outline='black', fill='blue', width=1 )
myCanvas.create_oval(110, 150, 170, 200, outline='black', fill='blue', width=1 )
root.mainloop()
