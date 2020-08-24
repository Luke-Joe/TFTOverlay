from Item import *
from tkinter import *


def item_click():
    item = Tk()

    item.attributes("-topmost", True)
    item.geometry('200x300+0+80')

    top_frame = Frame(item)
    top_frame.pack()

    bottom_frame = Frame(item)
    bottom_frame.pack(side=BOTTOM)

