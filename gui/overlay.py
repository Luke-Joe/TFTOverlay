from tkinter import *
from Item import *
from RiotAPI import *
from gui.Settings import *


root = Tk()


root.geometry('200x50+0+0')

root.attributes("-topmost", True)
root.configure(background="#b9bfc4")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

user = Label(bottomFrame, text=getUsername())
user.configure(background="#b9bfc4")
user.pack(side=LEFT)

rank = Label(bottomFrame, text=getRank())
rank.configure(background="#b9bfc4")
rank.pack(side=LEFT)

button1 = Button(topFrame, text="Items")
button2 = Button(topFrame, text="Comps")
button3 = Button(topFrame, text="Levels")
button4 = Button(topFrame, text="Settings", command=lambda: sett_click())

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

root.mainloop()

