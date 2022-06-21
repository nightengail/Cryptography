import os
from os import listdir
from os.path import isfile, join

from tkinter import *
from tkmacosx import Button

############ my stuff
def doTheThing():
    print(entry.get())


window = Tk()


greeting = Label(
    window,
    text="Hello, Tkinter"
    )

# button = Button(
#     window,
#     text='Mac OSX',
#     bg='black',
#     fg='green',
#     borderless=1
#     )

button = Button(
    window,
    text="Click me!",
    width=100,
    height=50,
    fg="yellow",
    bg = "blue",
    activebackground="lightblue",
    borderwidth=0,
    command = doTheThing
    )

entry = Entry(
    window,
    fg="blue",
    bg="light blue",
    width=20
    )

frame1 = Frame(
    window,
    relief = FLAT,
    bg = "light blue",
    borderwidth = 2
    )

labelwidth = 3
labelheight = 2
labelborder = 1

labele = Label(
    frame1,
    text = "E",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labelt = Label(
    frame1,
    text = "T",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labela = Label(
    frame1,
    text = "A",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labelo = Label(
    frame1,
    text = "O",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labeli = Label(
    frame1,
    text = "I",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labeln = Label(
    frame1,
    text = "N",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labels = Label(
    frame1,
    text = "S",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
labelh = Label(
    frame1,
    text = "H",
    relief = FLAT,
    bg = "blue",
    fg = "yellow",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )

labele.grid(row = 0, column = 0, padx = 2 , pady = 2, sticky = "")
labelt.grid(row = 0, column = 1, padx = 2 , pady = 2, sticky = "")
labela.grid(row = 0, column = 2, padx = 2 , pady = 2, sticky = "")
labelo.grid(row = 0, column = 3, padx = 2 , pady = 2, sticky = "")
labeli.grid(row = 0, column = 4, padx = 2 , pady = 2, sticky = "")
labeln.grid(row = 0, column = 5, padx = 2 , pady = 2, sticky = "")
labels.grid(row = 0, column = 6, padx = 2 , pady = 2, sticky = "")
labelh.grid(row = 0, column = 7, padx = 2 , pady = 2, sticky = "")

greeting.grid(row = 0, column = 0, sticky = "", columnspan = 2)
entry.grid(row = 1, column = 0)
button.grid(row = 1, column = 1)
frame1.grid(row = 2, column = 0, sticky = "", columnspan = 2)


window.mainloop()
############ my stuff




# #####vv From https://realpython.com/python-gui-tkinter/#assigning-widgets-to-frames-with-frame-widgets vv#####
# import tkinter as tk
#
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# window = tk.Tk()
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
#
# window.mainloop()

# #####^^ From https://realpython.com/python-gui-tkinter/#assigning-widgets-to-frames-with-frame-widgets ^^#####



# #####vv From https://www.geeksforgeeks.org/python-grid-method-in-tkinter/ vv######
# # creating main tkinter window/toplevel
# master = Tk()
#
# # this will create a label widget
# l1 = Label(master, text = "Height")
# l2 = Label(master, text = "Width")
#
# # grid method to arrange labels in respective
# # rows and columns as specified
# l1.grid(row = 0, column = 0, sticky = W, pady = 2)
# l2.grid(row = 1, column = 0, sticky = W, pady = 2)
#
# # entry widgets, used to take entry from user
# e1 = Entry(master)
# e2 = Entry(master)
#
# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)
#
# # checkbutton widget
# c1 = Checkbutton(master, text = "Preserve")
# c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)
#
# # adding image (remember image should be PNG and not JPG)
# img = PhotoImage(file = os.path.expanduser("~/Documents/Personal/Dante/DanteGail.png"))
# img1 = img.subsample(2, 2)
#
# # setting image with the help of label
# Label(master, image = img1).grid(row = 0, column = 2,
#        columnspan = 2, rowspan = 2, padx = 5, pady = 5)
#
# # button widget
# b1 = Button(master, text = "Zoom in")
# b2 = Button(master, text = "Zoom out")
#
# # arranging button widgets
# b1.grid(row = 2, column = 2, sticky = E)
# b2.grid(row = 2, column = 3, sticky = E)
#
# # infinite loop which can be terminated
# # by keyboard or mouse interrupt
# mainloop()
# #####^^ From https://www.geeksforgeeks.org/python-grid-method-in-tkinter/ ^^######

#####vv From https://realpython.com/python-gui-tkinter/ vv######
# window1 = Tk()
# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
# btn_decrease   =   Button ( window1 ,   text = "-" ,   command = decrease )
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = Label(window1, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase   =   Button ( window1 ,   text = "+" ,   command = increase )
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# window1.mainloop()
#####^^ From https://realpython.com/python-gui-tkinter/ ^^######
