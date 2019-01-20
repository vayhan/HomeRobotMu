from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont

root = Tk()
#root.attributes("-fullscreen", True)
base = Image.open("TTT.png")
img = ImageTk.PhotoImage(base)

txt = Image.new('RGBA', base.size, (255,255,255,0))
# get a drawing context
d = ImageDraw.Draw(txt)
d.ellipse((20, 30, 30, 20), fill = 'blue', outline ='blue')

panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()

