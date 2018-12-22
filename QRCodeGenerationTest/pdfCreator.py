# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

top = Tk()
top.geometry("100x100")
var = StringVar()
var.set("No file selected")
test = "test.png"

def isPNG(msg):
    if(msg[-4:] == ".png"):
        return True
    return False

def helloCallBack():
    msg = askopenfilename()
    if(isPNG(msg)): 
        test = msg;
        var.set(msg)
    else:
        msg = messagebox.showinfo( "Error", "Please only use supported files (PNG)")
        var.set("No file selected")
    print(msg)


img = ImageTk.PhotoImage(file = test)
panel = tk.Label(window, image = img)

B = Button(top, text = "Hello", command = helloCallBack)
W = Message(top, textvariable = var)
panel.pack();
W.pack()
B.place(x = 50,y = 50)

top.mainloop()
