"""
Created on Wed Jun  8 14:06 2022

@author: gail romer
"""

import os
from os import listdir
from os.path import isfile, join

# import numpy as np

from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

from tkmacosx import Button


def callback(sv,j,i):
    if bool(svs):
        print("hello",i,j)
        print(svs[j][i].get())
        # if len(svs)==26:
        #     if len(svs[0])==2:









def encrypt():
    # print("something")
    # text = text.get(1.0, 'end-1c')
    plaintext = plaintext_entry.get(1.0, 'end')

    # for i in range(len(plaintext)-1):
    #     print(plaintext[i:len(plaintext)-1])


def decrypt():
    # print("something")
    # text = text.get(1.0, 'end-1c')
    cyphertext = cyphertext_entry.get(1.0, 'end')
    print(cyphertext)
    # if not bool(entries):
    #     if len(entries)>1:
    #         print(entries[0][0].get())
    #     print(entries, len(entries))

    # for i in range(len(cyphertext)-1):
    #     print(cyphertext[i:len(plaintext)-1])

plaintext = []
cyphertext = []

window = Tk()

# Set window size   ===   window.geometry("WidthxHeight")
window.geometry("760x720")

style=ttk.Style()
style.theme_use('classic')
style.configure("Vertical.TScrollbar", troughcolor = "lightblue", background="blue", bordercolor="red", arrowcolor="blue")


# Set the window title
window.title('encript')

#Create a frame for widgets
plaintext_frame = Frame(
    window,
    width=(800*24/28),
    height=(600*9/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )
plain_frequency_frame = Frame(
    window,
    width=(800*24/28),
    height=(600*4/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )



button_frame = Frame(
    window,
    width=(800*24/28),
    height=(600*3/26),
    relief = FLAT,
    background = "green",
    borderwidth = 2
    )
# button_frame.grid_rowconfigure(0, weight=1)
# button_frame.grid_columnconfigure(0, weight=1)


cyphertext_frame = Frame(
    window,
    width=(800*24/28),
    height=(600*9/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )
cypher_frequency_frame = Frame(
    window,
    width=(800*24/28),
    height=(600*4/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )


letter_conversion_frame = Frame(
    window,
    width=(800*4/28),
    height=(620),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )


plaintext_entry_label = Label(
    plaintext_frame,
    text = "Enter plaintext:",
    height = 1,
    fg="black",
    bg="light blue",
    )
plaintext_entry = scrolledtext.ScrolledText(
    plaintext_frame,
    fg="blue",
    bg="light blue",
    width=94,
    height=13
    )
plaintext_entry.insert(END, "plaintext")

plaintext_entry.vbar.config(troughcolor = 'lightblue', activebackground = 'blue', bg = 'blue')
plaintext_entry_label.grid(row = 0, column = 0)
plaintext_entry.grid(row = 1, column = 0)
# scroll = Scrollbar(plaintext_frame)
# plaintext_entry.configure(yscrollcommand=scroll.set)
#
# scroll.config(command=plaintext_entry.yview)
# scroll.grid(row = 1, column = 1)



cyphertext_entry_label = Label(
    cyphertext_frame,
    text = "Enter cyphertext:",
    height = 1,
    fg="black",
    bg="light blue",
    )
cyphertext_entry = scrolledtext.ScrolledText(
    cyphertext_frame,
    fg="blue",
    bg="light blue",
    width=94,
    height=13
    )
cyphertext_entry.insert(END, "cyphertext")

cyphertext_entry.vbar.config(troughcolor = 'lightblue', activebackground = 'blue', bg = 'blue')
cyphertext_entry_label.grid(row = 0, column = 0)
cyphertext_entry.grid(row = 1, column = 0)



encrypt_button = Button(
        button_frame,
        text="encrypt",
        width=80,
        height=600*2/2/26,
        fg="yellow",
        bg = "blue",
        activebackground="lightblue",
        borderwidth=4,
        command = lambda: encrypt()
        )

decrypt_button = Button(
        button_frame,
        text="decrypt",
        width=80,
        height=600*2/2/26,
        fg="yellow",
        bg = "blue",
        activebackground="lightblue",
        borderwidth=4,
        command = lambda: decrypt()
        )

plaintext_button = Button(
        letter_conversion_frame,
        text="pt",
        width=20,
        height=600*2/2/26,
        fg="yellow",
        bg = "blue",
        activebackground="lightblue",
        borderwidth=4,
        command = lambda: encrypt()
        )

cyphertext_button = Button(
        letter_conversion_frame,
        text="CT",
        width=20,
        height=600*2/2/26,
        fg="yellow",
        bg = "blue",
        activebackground="lightblue",
        borderwidth=4,
        command = lambda: decrypt()
        )
# plaintext_button.grid(row = 0, column = 1, padx = (12,0), sticky = "")
encrypt_button.grid(row = 0, column = 2, padx = (263,12), pady=20, sticky = "")
decrypt_button.grid(row = 0, column = 3, sticky = "")
# cyphertext_button.grid(row = 0, column = 4, padx = (206,12), sticky = "")




## Create common english letter frequency table
labelwidth = 3
labelheight = 2
labelborder = 1
#letter frequency from: https://www.researchgate.net/figure/Relative-Frequency-of-Letters-in-the-English-Language_fig2_325714929
common_letters =         ["e",  "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p"] #, "b", "v", "k",  "j",  "x",   "q", "z"]
common_letter_frequency = [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.7, 2.4, 2.3, 2.2, 2.0, 2.1, 1.9] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
xl = 9
for letter in common_letters:

    letter_label = Label(
    plain_frequency_frame,
    text = common_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    plain_frequency_frame,
    text = common_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )

    letter_label.grid(row = 0, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    label.grid(row = 2, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    xl=2
    i = i+1



## Create common english letter frequency table
labelwidth = 3
labelheight = 2
labelborder = 1
#letter frequency from: https://www.researchgate.net/figure/Relative-Frequency-of-Letters-in-the-English-Language_fig2_325714929
common_cypher_letters =         ["e",  "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p"] #, "b", "v", "k",  "j",  "x",   "q", "z"]
common_cypher_letter_frequency = [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.7, 2.4, 2.3, 2.2, 2.0, 2.1, 1.9] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
xl = 9
for letter in common_cypher_letters:

    letter_label = Label(
    cypher_frequency_frame,
    text = common_cypher_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    cypher_frequency_frame,
    text = common_cypher_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )

    letter_label.grid(row = 1, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    label.grid(row = 0, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    xl=2
    i = i+1

plaintext_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cyphertext_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alphabets = [plaintext_alphabet, cyphertext_alphabet]

plaintext_button.grid(row = 0, column = 0, padx = 2 , pady = 2, sticky = "")
cyphertext_button.grid(row = 0, column = 1, padx = 2 , pady = 2, sticky = "")

labelwidth = 2
labelborder = 1
labelheight = 1
yl = 2

entries = []
svs = [[],[]]

for i in range(26):
    new_row = []

    for j in range(2):
        sv = StringVar()
        svs[j].append(sv)

        svs[j][i].trace("w", lambda name, index, mode, sv=svs[j][i], i=i, j=j: callback(sv,j,i))

        letter = Entry(
        letter_conversion_frame,
        relief = FLAT,
        bg = "blue",
        fg = "light blue",
        borderwidth = labelborder,
        width = labelwidth,
        textvariable = svs[j][i]
        # command = decrypt()
        )
        letter.insert(END, alphabets[j][i])

        new_row.append(letter)

        letter.grid(row = i+1, column = j, sticky = "")

    entries.append(new_row)

# plaintext_frame.grid(row = 0, column = 0, padx = 2 , pady = 2, sticky = "")
# plain_frequency_frame.grid(row = 1, column = 0, padx = 2 , pady = 2, sticky = "")
# button_frame.grid(row = 2, column = 0, padx = 2 , pady = 2, sticky = "")
# cypher_frequency_frame.grid(row = 3, column = 0, padx = 2 , pady = 2, sticky = "")
# cyphertext_frame.grid(row = 4, column = 0, padx = 2 , pady = 2, sticky = "")


if len(svs)==26:
    if len(svs[0])==2:
        print(svs[25][1].get())
# # print(len(svs[0]))
#     print(len(svs[0]))


plaintext_frame.grid(row = 0, column = 0, rowspan = 9, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")
plain_frequency_frame.grid(row = 9, column = 0, rowspan = 4, columnspan = 6, padx = 2 , pady = 0, sticky = "nesw")
button_frame.grid(row = 13, column = 0, rowspan = 3, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")
cypher_frequency_frame.grid(row = 16, column = 0, rowspan = 4, columnspan = 6, padx = 2 , pady = 0, sticky = "nesw")
cyphertext_frame.grid(row = 20, column = 0, rowspan = 9, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")
letter_conversion_frame.grid(row = 0, column = 7, rowspan = 26, columnspan = 1, padx = 2 , pady = 2, sticky = "nesw")

window.mainloop()
