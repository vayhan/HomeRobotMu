import tkinter as tk
import os

root = tk.Tk()
root["bg"] = "white"
root.attributes('-fullscreen', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

topGAP = 200
lineLenght = 300
ovalGap = 100
canvas = tk.Canvas(root,width=screen_width, height=screen_height)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas.config(background='white')

canvas.create_oval(lineLenght + ovalGap, topGAP - ovalGap, (screen_width/2) - ovalGap, topGAP + ovalGap, fill="black",width=0)
canvas.create_rectangle(lineLenght, 0, screen_width/2, topGAP, fill='white',width=0 )
canvas.create_line(lineLenght, topGAP, screen_width/2, topGAP,width=10)

canvas.create_oval((screen_width/2) + ovalGap, topGAP - ovalGap, screen_width - lineLenght - ovalGap, topGAP + ovalGap, fill="black",width=0)
canvas.create_rectangle(screen_width/2, 0, screen_width - lineLenght, topGAP, fill='white',width=0 )
canvas.create_line(screen_width/2, topGAP, screen_width - lineLenght, topGAP,width=10)

gelenText = 'Merhaba Dünya'
gelenTextUzun = len(gelenText)
canvas.create_text((screen_width/2), topGAP + ovalGap * 3, text=gelenText, font="Arial,30")

canvas.pack()

root.mainloop()
