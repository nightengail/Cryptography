"""
Created on Wed Jun  8 14:06 2022

@author: gail romer
"""
# KZRNKGJKIPZBOOBXLCRGBXFAUGJBNGRIXRUXAFGJBXRMEMNKNGBURIXKJRXRSBUERISATBUIBNNRTBUMN
# BIGKEBIGROCUBRGLUBNJBGRLSJGLNGJBORISLRSBAFFOAZBUNRFAUSAGGBINGLXMIAZRXRMNVLGEANGCJ
# RUEKISRMBOOAZGLOKWFAUKINGRICBEBRINJAWBOBNNOATBZJKOBRCJKIRRNGBUEBRINKXKBAFQBROALNM
# RGMALUFBBG

import os
from os import listdir
from os.path import isfile, join

import numpy as np
from math import floor, sqrt

import collections
from collections import defaultdict
from collections import Counter


import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

from tkmacosx import Button






def recalculate():
    Mod = int(mod.get())
    Base = int(base.get())
    H = int(h.get())
    [n,N,nframe_labels] = calculate_nframe(Mod,Base)
    calculate_gsframe(Mod,Base,H,n,N)

    # Set window size   ===   window.geometry("WidthxHeight")
    # window_x = 772
    window_y = 100+n*26
    window_geometry = "".join((str(window_x), "x", str(window_y)))
    window.geometry(window_geometry)

def calculate_nframe(Mod,Base):
    for widget in nframe.winfo_children():
        widget.destroy()

    labels1  =  ["i"]
    labels2 =  ["".join([str(Mod),"/i"])]
    labels3 =  ["".join([str(Base),"^i"])]
    labels4 =  ["".join([str(Base),"^i mod",str(Mod)])]

    orders = []

    for i in range(1,Mod):
        if ((Mod-1)/i)%1 == 0:
            labels1.append(i)
            labels2.append(int((Mod-1)/i))
            labels3.append(int((Base**i)))
            labels4.append(int((Base**i)%Mod))
            if ((Base**i)%Mod) == 1:
                orders.append(i)

    the_order = min(orders)

    i = 0
    labelwidth = 3
    labelheight = 1
    labelborder = 1
    list_labels = []
    xl = 2
    for label in labels1: #

        label1 = Label(
        nframe,
        text = labels1[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth,
        height = labelheight
        )
        label2 = Label(
        nframe,
        text = labels2[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth*2,
        height = labelheight
        )
        label3 = Label(
        nframe,
        text = labels3[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth*2,
        height = labelheight
        )
        label4 = Label(
        nframe,
        text = labels4[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth*3,
        height = labelheight
        )

        list_labels.append([label1,label2,label3,label4])

        label1.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
        label2.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
        label3.grid(row = i, column = 2, padx = (xl,2) , pady = 2, sticky = "")
        label4.grid(row = i, column = 3, padx = (xl,2) , pady = 2, sticky = "")
        xl=2
        i = i+1

    the_order_label = Label(
    nframe,
    text = "".join(["The order of ", str(Base),"\n mod ",str(Mod)," is ",str(the_order),"."]),
    relief = FLAT,
    bg = "light blue",
    fg = "blue",
    borderwidth = labelborder,
    width = labelwidth*4,
    height = labelheight*4
    )


    n = floor(sqrt(the_order))+1
    n_label = Label(
    nframe,
    text = "".join(["N = ", str(the_order),"\n n = ",'\u230A\u221A',str(the_order),'\u230B'," + 1 \n n =  ",str(n)]),
    relief = FLAT,
    bg = "light blue",
    fg = "blue",
    borderwidth = labelborder,
    width = labelwidth*4,
    height = labelheight*4
    )

    the_order_label.grid(row = 0, column = 4, rowspan = 3, padx = (xl,2) , pady = 2, sticky = "")
    n_label.grid(row = 3, column = 4, rowspan = 3, padx = (xl,2) , pady = 2, sticky = "")
    return [n, the_order,list_labels]

def calculate_gsframe(Mod,Base,H,n,N):
    for widget in gsframe.winfo_children():
        widget.destroy()

    labels1  =  ["i"]
    labels2  =  ["g^i"]
    labels3 =  ["hg^-jn"]

    g_n = (Base**n)%Mod
    g_negn = (g_n**(Mod-2))%Mod

    for i in range(n+1):

        labels1.append(i)
        labels2.append(int((Base**i)%Mod))
        labels3.append(int((H*(g_negn**i))%Mod))


    i = 0
    labelwidth = 3
    labelheight = 1
    labelborder = 1
    list_labels = []
    xl = 2
    for label in labels1: #

        label1 = Label(
        gsframe,
        text = labels1[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth,
        height = labelheight
        )
        label2 = Label(
        gsframe,
        text = labels2[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth*2,
        height = labelheight
        )
        label3 = Label(
        gsframe,
        text = labels3[i],
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth*2,
        height = labelheight
        )


        list_labels.append([label1,label2,label3])

        label1.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
        label2.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
        label3.grid(row = i, column = 2, padx = (xl,2) , pady = 2, sticky = "")

        xl=2
        i = i+1

    g_n_label = Label(
    gsframe,
    text = "".join(["g^n = ",str(g_n)," mod ",str(Mod),"\n\n g^-n = ",str(g_negn)," mod ",str(Mod)]),
    relief = FLAT,
    bg = "light blue",
    fg = "blue",
    borderwidth = labelborder,
    width = labelwidth*6,
    height = labelheight*4
    )

    match = list(set(labels2).intersection(set(labels3)))[0]

    i = labels2.index(match)
    j = labels3.index(match)

    list_labels[i][1].configure(bg = "green", fg = "lightblue")
    list_labels[j][2].configure(bg = "green", fg = "lightblue")

    x = i-1+(j-1)*n
    x_label = Label(
    gsframe,
    text = "".join(["x = i + jn \n x = ",str(i-1)," + ",str(j-1)," * ",str(n),"\n x =",str(x)]),
    relief = FLAT,
    bg = "light blue",
    fg = "blue",
    borderwidth = labelborder,
    width = labelwidth*6,
    height = labelheight*4
    )

    check_label = Label(
    gsframe,
    text = "".join([str(Base),"^",str(x)," = ",str((Base**x)%Mod)]),
    relief = FLAT,
    bg = "light blue",
    fg = "blue",
    borderwidth = labelborder,
    width = labelwidth*6,
    height = labelheight*4
    )

    g_n_label.grid(row = 0, column = 4, rowspan = 3, padx = (xl,2) , pady = 2, sticky = "")
    x_label.grid(row = 3, column = 4, rowspan = 3, padx = (xl,2) , pady = 2, sticky = "")
    check_label.grid(row = 6, column = 4, rowspan = 3, padx = (xl,2) , pady = 2, sticky = "")
    return

def get_base_stringvar(event):
    base = base_entry.get()
    base_entry.delete(0, END)
    base_entry.insert(0,base)
    # print(base)

def get_h_stringvar(event):
    h = h_entry.get()
    h_entry.delete(0, END)
    h_entry.insert(0,h)
    # print(h)

def get_mod_stringvar(event):
    mod = mod_entry.get()
    mod_entry.delete(0, END)
    mod_entry.insert(0,mod)
    # print(mod)



window = Tk()

# Set window size   ===   window.geometry("WidthxHeight")
window_x = 772
window_y = 400
window_geometry = "".join((str(window_x), "x", str(window_y)))
window.geometry(window_geometry)

style=ttk.Style()
style.theme_use('classic')
style.configure("Vertical.TScrollbar", troughcolor = "lightblue", background="blue", bordercolor="red", arrowcolor="blue")


# Set the window title
window.title('encript')


#Create a frame for widgets
entryframe = Frame(
    window,
    width=(window_x),
    height=(window_y/2),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )

nframe = Frame(
    window,
    width=(window_x/4),
    height=(window_y-60),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )

gsframe = Frame(
    window,
    width=(window_x/4),
    height=(window_y-60),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )

#Create entries
base = StringVar()
base_entry_label = Label(
    entryframe,
    text = "Base:",
    height = 1,
    fg="black",
    bg="light blue",
    )
base_entry = Entry(
entryframe,
relief = FLAT,
bg = "blue",
fg = "light blue",
width=10,
textvariable = base
)
base_entry.delete(0, END)
base_entry.insert(0,"156")


h = StringVar()
h_entry_label = Label(
    entryframe,
    text = "H:",
    height = 1,
    fg="black",
    bg="light blue",
    )
h_entry = Entry(
entryframe,
relief = FLAT,
bg = "blue",
fg = "light blue",
width=10,
textvariable = h
)
h_entry.delete(0, END)
h_entry.insert(0,"116")


mod = StringVar()
mod_entry_label = Label(
    entryframe,
    text = "Mod:",
    height = 1,
    fg="black",
    bg="light blue",
    )
mod_entry = Entry(
    entryframe,
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    width=10,
    textvariable = mod
    )
mod_entry.delete(0, END)
mod_entry.insert(0,"593")

recalculate_button = Button(
    entryframe,
    text="recalculate",
    width=80,
    height=600*2/2/26,
    fg="yellow",
    bg = "blue",
    activebackground="lightblue",
    borderwidth=4,
    command = lambda: recalculate()
    )

base_entry.bind('<KeyRelease>', get_base_stringvar)
h_entry.bind('<KeyRelease>', get_h_stringvar)
mod_entry.bind('<KeyRelease>', get_mod_stringvar)





base_entry_label.grid(row = 0, column = 0, padx = (100,2), pady = (20,10))
base_entry.grid(row = 0, column = 1, padx = (2,10), pady = (20,10))

h_entry_label.grid(row = 0, column = 2, padx = (10,2), pady = (20,10))
h_entry.grid(row = 0, column = 3, padx = (2,10), pady = (20,10))

mod_entry_label.grid(row = 0, column = 4, padx = (10,2), pady = (20,10))
mod_entry.grid(row = 0, column = 5, padx = (2,10), pady = (20,10))

recalculate_button.grid(row = 0, column = 6, padx = (10,100), pady = (20,10))

#Pack the entryframe
entryframe.grid(row = 0, column = 0, rowspan = 2, columnspan = 4, padx = 2 , pady = 2, sticky = "nesw")
nframe.grid(row = 2, column = 0, rowspan = 6, columnspan = 2, padx = 2 , pady = 2, sticky = "nesw")
gsframe.grid(row = 2, column = 2, rowspan = 6, columnspan = 2, padx = 2 , pady = 2, sticky = "nesw")

window.mainloop()
