from tkinter import *
from Item import *
from RiotAPI import *


root = Tk()
root.geometry('200x50+0+0')

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

user = Label(bottomFrame, text=getUsername())
user.pack(side=LEFT)

rank = Label(bottomFrame, text=getRank())
rank.pack(side=LEFT)

button1 = Button(topFrame, text="Items", fg="red")
button2 = Button(topFrame, text="Comps", fg="blue")
button3 = Button(topFrame, text="Levels", fg="green")
button4 = Button(topFrame, text="Settings", fg="grey")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop()

