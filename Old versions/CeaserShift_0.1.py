"""
Created on Wed Jun  8 14:06 2022

@author: gail romer
"""

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


commonLetters = ["E","T","A","O","I","N","S","H","R","D"]
commonLetterFrequency = [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3]
i = 0

for letter in commonLetters:

    letterLabel = Label(
        frame1,
        text = commonLetters[i],
        relief = FLAT,
        bg = "blue",
        fg = "yellow",
        borderwidth = labelborder,
        width = labelwidth,
        height = labelheight
        )
    label = Label(
        frame1,
        text = commonLetterFrequency[i],
        relief = FLAT,
        bg = "blue",
        fg = "yellow",
        borderwidth = labelborder,
        width = labelwidth,
        height = labelheight
        )

    letterLabel.grid(row = 0, column = i, padx = 2 , pady = 2, sticky = "")
    label.grid(row = 2, column = i, padx = 2 , pady = 2, sticky = "")

    i = i+1




greeting.grid(row = 0, column = 0, sticky = "", columnspan = 2)
entry.grid(row = 1, column = 0)
button.grid(row = 1, column = 1)
frame1.grid(row = 2, column = 0, sticky = "", columnspan = 2)


window.mainloop()


# #### User input for cypher text ####
# CypherText = str(input("Please enter the text you wish to encript"))
#
#
# CypherText_List = []
#
# for i in range(len(CypherText)):
#      CypherText_List.append(CypherText[i])
#
#
# print(CypherText_List)
