from tkinter import *

sett_status = 0
# 0 = off
# 1 = on


def sett_click():
    global sett_status

    if sett_status == 0:
        global sett
        sett_status = 1
        sett = Toplevel()

        sett.geometry('200x300+0+80')
        sett.attributes("-topmost", True)

        sett.mainloop()

    else:
        sett.destroy()
        sett_status = 0
