# import os
# from os import listdir
# from os.path import isfile, join
#
# from tkinter import *
# from tkmacosx import Button
# from tkinter import scrolledtext
#
# ############ my stuff
# def doTheThing():
#     print(entry.get(1.0, END))
#
# def pasteText():
#     clipboard = entry.clipboard_get()
#     # clipboard = clipboard.replace("\n", "\\n")
#     entry.insert("insert", clipboard)
#
# window = Tk()
#
#
# paste_button = Button(
#     window,
#     text="Paste from Clipboard",
#     width=100,
#     height=50,
#     fg="yellow",
#     bg = "blue",
#     activebackground="lightblue",
#     borderwidth=0,
#     command = pasteText
#     )
#
#
#
# greeting = Label(
#     window,
#     text="Hello, Tkinter"
#     )
#
# # button = Button(
# #     window,
# #     text='Mac OSX',
# #     bg='black',
# #     fg='green',
# #     borderless=1
# #     )
#
# button = Button(
#     window,
#     text="Click me!",
#     width=100,
#     height=50,
#     fg="yellow",
#     bg = "blue",
#     activebackground="lightblue",
#     borderwidth=0,
#     command = doTheThing
#     )
#
#
#
#
#
# ## one line entry
# # entry = Entry(
# #     window,
# #     fg="blue",
# #     bg="light blue",
# #     width=20
# #     )
#
# ## multi line entry
# # entry = Text(
# #     window,
# #     width=20,
# #     height=3,
# #     fg="blue",
# #     bg="light blue"
# #     )
#
# ## multi line entry with scrol
# entry = scrolledtext.ScrolledText(
# window,
# wrap=WORD,
# width=40,
# height=8,
# font=("Times New Roman", 15)
# )
#
#
#
#
# frame1 = Frame(
#     window,
#     relief = FLAT,
#     bg = "light blue",
#     borderwidth = 2
#     )
#
# labelwidth = 3
# labelheight = 2
# labelborder = 1
#
#
#
#
# commonLetters = ["E","T","A","O","I","N","S","H","R","D"]
# commonLetterFrequency = [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3]
# i = 0
#
# for letter in commonLetters:
#
#     letterLabel = Label(
#         frame1,
#         text = commonLetters[i],
#         relief = FLAT,
#         bg = "blue",
#         fg = "yellow",
#         borderwidth = labelborder,
#         width = labelwidth,
#         height = labelheight
#         )
#     label = Label(
#         frame1,
#         text = commonLetterFrequency[i],
#         relief = FLAT,
#         bg = "blue",
#         fg = "yellow",
#         borderwidth = labelborder,
#         width = labelwidth,
#         height = labelheight
#         )
#
#     letterLabel.grid(row = 0, column = i, padx = 2 , pady = 2, sticky = "")
#     label.grid(row = 2, column = i, padx = 2 , pady = 2, sticky = "")
#
#     i = i+1
#
#
#
#
# greeting.grid(row = 0, column = 0, sticky = "", columnspan = 2)
# entry.grid(row = 1, column = 0)
# button.grid(row = 1, column = 1)
# frame1.grid(row = 2, column = 0, sticky = "", columnspan = 2)
#
#
# window.mainloop()
# ############ my stuff
#
#
# #####vv From: https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20actual%20width%20of%20the,*ipady%20%2B%20Default%20Entry%20height%20. vv#####
# app = Tk()
#
# entryExample1 = Entry(app)
# entryExample2 = Entry(app)
#
# entryExample1.grid(row=0,
#                column=0,
#                padx=10,
#                pady=10,
#                ipady=30)
#
# entryExample2.grid(row=1,
#                column=0,
#                padx=10,
#                pady=10,
#                ipadx=20,
#                ipady=30)
#
# app.geometry("300x300")
#
# app.mainloop()
#####^^ From: https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/#:~:text=The%20actual%20width%20of%20the,*ipady%20%2B%20Default%20Entry%20height%20. ^^#####


# from tkinter import *
#
# def callback(sv):
#     print (sv.get())
#
# root = Tk()
# sv = StringVar()
# sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
# e = Entry(root, textvariable=sv)
# e.pack()
# root.mainloop()
# from tkinter import Tk, Frame, Label, Entry, StringVar
#
# class Fruitlist:
#     def entryupdate(self, sv, i):
#         print(sv, i, self.fruit[i], sv.get())
#
#     def __init__(self, root):
#         cf = Frame(root)
#         cf.pack()
#         self.string_vars = []
#         self.fruit = ("Apple", "Banana", "Cherry", "Date")
#         for f in self.fruit:
#             i = len(self.string_vars)
#             self.string_vars.append(StringVar())
#             self.string_vars[i].trace("w", lambda name, index, mode, var=self.string_vars[i], i=i:
#                               self.entryupdate(var, i))
#             Label(cf, text=f).grid(column=2, row=i)
#             Entry(cf, width=6, textvariable=self.string_vars[i]).grid(column=4, row=i)
#
# root = Tk()
# root.title("EntryUpdate")
# app = Fruitlist(root)
# root.mainloop()

###vv https://stackoverflow.com/questions/10593027/how-can-i-connect-a-stringvar-to-a-text-widget-in-python-tkinter
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def get_stringvar(event):
    SV.set(ST1.get("1.0", END))
    ST2.replace("1.0", END, SV.get())
    print(ST1.get("1.0", "end-1c"))


root = tk.Tk()

SV = StringVar()

ST1 = ScrolledText(root)
ST1.pack()
ST1.bind('<KeyRelease>', get_stringvar)


ST2 = ScrolledText(root)
ST2.pack()

root.mainloop()
###^^

# from tkinter import *
# root = Tk()
#
# height = 5
# width = 5
#
# delta=0
#
# entries = []
#
# for i in range(height): #Rows
#   newrow = []
#   for j in range(width): #Columns
#     b = Entry(root, text="",width=8)
#     b.grid(row=i, column=j)
#     newrow.append(b)
#   entries.append(newrow)
#
# mainloop()
# print(entries)

######vv From https://stackoverflow.com/questions/6950007/pasting-in-the-tkinter-text-widget vv#####
# import tkinter as tk
# from tkinter import TclError
#
# class SampleApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.text = tk.Text(self, width=40, height=8)
#         self.button = tk.Button(self, text="do it!", command=self.doit)
#         self.button.pack(side="top")
#         self.text.pack(side="bottom", fill="both", expand=True)
#         self.doit()
#
#     def doit(self, *args):
#         # get the clipboard data, and replace all newlines
#         # with the literal string "\n"
#         clipboard = self.clipboard_get()
#         clipboard = clipboard.replace("\n", "\\n")
#
#         # delete the selected text, if any
#         try:
#             start = self.text.index("sel.first")
#             end = self.text.index("sel.last")
#             self.text.delete(start, end)
#         except (TclError, E):
#             # nothing was selected, so paste doesn't need
#             # to delete anything
#             pass
#
#         # insert the modified clipboard contents
#         self.text.insert("insert", clipboard)
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
###### ^^ From https://stackoverflow.com/questions/6950007/pasting-in-the-tkinter-text-widget ^^#####

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



#####vv https://www.geeksforgeeks.org/how-to-create-a-multiline-entry-with-tkinter/ vv#####
# import tkinter as tk
# from tkinter import ttk
#
#
# window = tk.Tk()
# window.title("Text Widget Example")
# window.geometry('400x200')
#
# ttk.Label(window, text="Enter your comment :",
#           font=("Times New Roman", 15)).grid(
#   column=0, row=15, padx=10, pady=25)
#
# # Text Widget
# t = tk.Text(window, width=20, height=3)
#
# t.grid(column=1, row=15)
#
# window.mainloop()
#####^^ https://www.geeksforgeeks.org/how-to-create-a-multiline-entry-with-tkinter/ ^^#####

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
