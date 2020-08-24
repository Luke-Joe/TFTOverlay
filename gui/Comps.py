from tkinter import *

comp_status = 0
# 0 = off
# 1 = on


def sett_click():
    global comp_status

    if comp_status == 0:
        global comp
        comp_status = 1
        comp = Toplevel()

        comp.geometry('200x300+0+80')
        comp.attributes("-topmost", True)

        comp.mainloop()

    else:
        comp.destroy()
        comp_status = 0
