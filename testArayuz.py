import tkinter as tk
import time

canvas_width = 190
canvas_height =190

root = tk.Tk()
root["bg"] = "black"
w = tk.Canvas(root, width=canvas_width, height=canvas_height)
w.config(background='black')
w.pack()
points = [40,50,100,100]
blue = w.create_oval(points, outline='black', fill='blue', width=1)
pointse = [110,50,170,100]
bluee = w.create_oval(pointse, outline='black', fill='blue', width=1)
w.after(1000,redraw)
root.mainloop()

def redraw():
   xi=40
   yi=70
   a=1
   b=1
   linx=1
   while(xi>0):
      root.after(1)
      xi+=a
      yi-=b
      w.coords(blue, 40, xi, 100, yi)
      w.coords(bluee, 110, xi, 170, yi)
      w.update()
      if(xi==1):
         a=-1
         b=-1
      elif(xi==40):
         a=+1
         b=+1
         xi=0
      elif(xi==70):
         a=-1
         b=-1
         xi=0
      while(linx<50):
         linx+=1
         linxote=linx*5
         pointlin = [linxote,0,linxote,100]
         linid = w.create_line(pointlin, fill="black", width=2, stipple="gray50")
         w.coords(linid, linxote, 0, linxote, 200)
         linyid = w.create_line(pointlin, fill="black", width=2, stipple="gray50")
         w.coords(linyid, 0, linxote, 200, linxote)
   return
