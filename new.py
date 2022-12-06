from tkinter import *
MyWindow = Tk()
MyWindow.geometry("200x200")

TopFrame = Frame(MyWindow)
TopFrame.pack()

btn1 = Button(TopFrame, text="Submit",fg="red",activebackground = "red")
btn1.pack(side = LEFT)

btn2 = Button(TopFrame, text="Remove",fg="brown",activebackground = "brown")
btn2.pack(side = RIGHT)

RightFrame = Frame(MyWindow)
RightFrame.pack(side = RIGHT)

btn3 = Button(RightFrame, text="Add",fg="blue",activebackground = "blue")
btn3.pack(side = LEFT)

LeftFrame = Frame(MyWindow)
LeftFrame.pack(side = LEFT)

btn4 = Button(LeftFrame, text="Modify",fg="green",activebackground = "green")
btn4.pack(side = RIGHT)
