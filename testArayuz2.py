from tkinter import *
import time

root = Tk()
myCanvas = Canvas(root)
myCanvas.config(background='black')
myCanvas.pack()

def eyeBlink(canvasName):
    y0=50
    y1=100
    leftEYE = canvasName.create_oval(40, y0, 100, y1, outline='black', fill='blue', width=1 )
    rightEYE = canvasName.create_oval(110, y0, 170, y1, outline='black', fill='blue', width=1 )
    a=1
    b=1
    while(y0>0):
        root.after(1)
        myCanvas.coords(leftEYE, 40, y0, 100, y1)
        myCanvas.coords(rightEYE, 110, y0, 170, y1)
        myCanvas.update()
        y0+=a
        y1-=b
        print (y0)
        if(y0==1):
            a=+1
            b=-1
        elif(y0==50):
            a=+2
            b=+2
            time.sleep(3)
        elif(y0==70):
            a=-2
            b=-2
    return

eyeBlink(myCanvas)
root.mainloop()
