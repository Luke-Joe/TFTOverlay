from tkinter import *
from PIL import ImageTk, Image


item_status = 0
# 0 = off
# 1 = on


def item_click():
    global item_status

    if item_status == 0:
        global item
        item_status = 1
        item = Toplevel()

        item.geometry('600x600+0+80')
        sheet = Canvas(item, width=543, height=562)
        sheet.pack()
        img = ImageTk.PhotoImage(Image.open("ItemTFT.PNG"))
        item.attributes("-topmost", True)
        sheet.create_image(0, 0, anchor=NW, image=img)

        item.mainloop()

    else:
        item.destroy()
        item_status = 0
