#writed by moein
from tkinter import *
import os

win = Tk()
win.title("writed by moein")
win.geometry("200x70")
win.resizable(0,0)

def shut():
		os.system("shutdown /s /t 1")
def res():
		os.system("shutdown /r /t 1")

l = Label(win,text="click on button:")
l.grid()

b = Button(win,text="shutdown",command=shut,bg="yellow")
b.grid(ipadx=10)

b2 = Button(win,text="restart",command=res,bg="red")
b2.grid(ipadx=10,column=2,row=1)

win.mainloop()
#thise is python's power