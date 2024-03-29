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

import collections
from collections import defaultdict
from collections import Counter


import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

from tkmacosx import Button

non_text_chars = [" ", "\n", ".", ",", "?", "!", "_", "-"]

def list_duplicates(seq):
    ## From https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items()
                            if len(locs)>1)

def callback(sv,j,i):
    if bool(svs):
        a=0

        if j == 0: ## makes plaintext alphabet entries lowercase
            letter = entries[i][j].get()
            entries[i][j].delete(0,END)
            entries[i][j].insert(0,letter.lower())

            ## change letter in plaintext alphabet
            alphabets[0][i] = letter.lower()

        if j == 1: ## makes cyphertext alphabet entries uppercase
            letter = entries[i][j].get()
            entries[i][j].delete(0,END)
            entries[i][j].insert(0,letter.upper())
            ## change letter in cyphertext alphabet
            alphabets[1][i] = letter.upper()
        check_alphabets()

def check_alphabets():
    one_to_one = False
    letters = []
    for entry in entries:
        for letter in entry:
            letters.append(letter.get())

    duplicate_letters = [item for item, count in collections.Counter(letters).items() if count > 1]

    for index in range(26):
        entries[index][0].configure(bg = "blue", fg = "lightblue")
        entries[index][1].configure(bg = "blue", fg = "lightblue")

    if not bool(duplicate_letters):
        # print("no duplicates")
        # if key exists: key.clear()
        key = {entries[i][0].get(): entries[i][1].get() for i in range(26)}
        #print(key)
        one_to_one = True

    else:
        # print("Duplicated letters:",", ".join(duplicate_letters))

        entered_cypher_letters = [entries[i][1].get() for i in range(26)]
        entered_normal_letters = [entries[i][0].get() for i in range(26)]

        for duplicate in sorted(list_duplicates(entered_cypher_letters)):
            # print(duplicate)
            for index in duplicate[1]:
                entries[index][1].configure(bg = "red", fg = "black")

        for duplicate in sorted(list_duplicates(entered_normal_letters)):
            # print(duplicate)
            for index in duplicate[1]:
                entries[index][0].configure(bg = "red", fg = "black")

    if one_to_one:
        for character in non_text_chars:
            key[character] = character
        return one_to_one, key
    else:
        return one_to_one, 0

def entry_text(text,j):
    if j == 0: ## makes plaintext alphabet lowercase
        text_string = text.get()
        text.delete(0,END)
        text.insert(0,text_string.lower())
    if j == 1: ## makes cyphertext alphabet lowercase
        text_string = text.get()
        text.delete(0,END)
        text.insert(0,text_string.upper())

def encrypt():
    [one_to_one, key] = check_alphabets()
    if one_to_one:
        plaintext = plaintext_entry.get(1.0, 'end')
        plaintext_list = []
        encryptedtext_list = []
        for i in range(len(plaintext)-1):
             plaintext_list.append(plaintext[i])

        for letter in plaintext_list:
            encryptedtext_list.append(key[letter])

        cyphertext_entry.replace(1.0,END,''.join(encryptedtext_list))

def decrypt():
    [one_to_one, key] = check_alphabets()
    if one_to_one:
        cyphertext = cyphertext_entry.get(1.0, 'end')
        decryptedtext_list = []
        cyphertext_list = []
        for i in range(len(cyphertext)-1):
            cyphertext_list.append(cyphertext[i])

        for letter in cyphertext_list:
            for index, value in key.items():
                if value == letter:
                    decryptedtext_list.append(index)

        plaintext_entry.replace(1.0,END,''.join(decryptedtext_list))

def reorder(base_alphabet):
    [one_to_one, key] = check_alphabets()
    plaintext_entries = [entries[i][0] for i in range(len(entries))]
    cyphertext_entries = [entries[i][1] for i in range(len(entries))]

    #print(key)#[plaintext_entries[i].get() for i in range(26)])


def frequency():
    cyphertext = cyphertext_entry.get(1.0, 'end')
    cyphertext_list = []
    cyphertext_bigraph_list = []
    cyphertext_trigraph_list = []

    [one_to_one,key] = check_alphabets()

    backkey = {}
    for pt in key:
        backkey[key[pt]] = pt

    for i in range(len(cyphertext)-1):
         cyphertext_list.append(cyphertext[i])

    for i in range(len(cyphertext)-2):
        if cyphertext[i] not in non_text_chars and cyphertext[i+1] not in non_text_chars:
            cyphertext_bigraph_list.append("".join([cyphertext[i],cyphertext[i+1]]))

    for i in range(len(cyphertext)-3):
        if cyphertext[i] not in non_text_chars and cyphertext[i+1] not in non_text_chars and cyphertext[i+2] not in non_text_chars:
            cyphertext_trigraph_list.append("".join([cyphertext[i],cyphertext[i+1],cyphertext[i+2]]))

    sorted_cyphertext = [item for items, c in Counter(cyphertext_list).most_common() for item in [items] * c] ##https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
    sorted_bigraphs = [item for items, c in Counter(cyphertext_bigraph_list).most_common() for item in [items] * c] ##https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
    sorted_trigraphs = [item for items, c in Counter(cyphertext_trigraph_list).most_common() for item in [items] * c] ##https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/

    cyphertext_frequency = Counter(cyphertext_list)
    cyphertext_bigraph_frequency = Counter(cyphertext_bigraph_list)
    cyphertext_trigraph_frequency = Counter(cyphertext_trigraph_list)

    sorted_cyphertext = [i for n, i in enumerate(sorted_cyphertext) if i not in sorted_cyphertext[:n]]
    sorted_bigraphs = [i for n, i in enumerate(sorted_bigraphs) if i not in sorted_bigraphs[:n]]
    sorted_trigraphs = [i for n, i in enumerate(sorted_trigraphs) if i not in sorted_trigraphs[:n]]

    if " " in sorted_cyphertext: sorted_cyphertext.remove(' '); cyphertext_list.remove(' ')
    if "\n" in sorted_cyphertext: sorted_cyphertext.remove("\n"); cyphertext_list.remove('\n')
    if "," in sorted_cyphertext: sorted_cyphertext.remove(","); cyphertext_list.remove(',')
    if "." in sorted_cyphertext: sorted_cyphertext.remove("."); cyphertext_list.remove('.')



    for i in range(19):
        if len(sorted_cyphertext)>i:
            cyphertext_frequency_labels[i][0].configure(text = sorted_cyphertext[i])
            cyphertext_frequency_labels[i][1].configure(text = round(100*cyphertext_frequency[sorted_cyphertext[i]]/len(cyphertext_list),1))
    if len(sorted_cyphertext)<19:
        for l in range(len(sorted_cyphertext),19):
            cyphertext_frequency_labels[l][0].configure(text = "-")
            cyphertext_frequency_labels[l][1].configure(text =  0)

    for i in range(13):
        if len(sorted_bigraphs)>i:
            # print(sorted_bigraphs[i],len(sorted_bigraphs[i]))
            cyphertext_bigraph_frequency_labels[i][0].configure(text = sorted_bigraphs[i])
            cyphertext_bigraph_frequency_labels[i][1].configure(text = round(100*cyphertext_bigraph_frequency[sorted_bigraphs[i]]/len(cyphertext_bigraph_list),1))
            cyphertext_bigraph_frequency_labels[i][2].configure(text = "".join([backkey[sorted_bigraphs[i][j]] for j in range(len(sorted_bigraphs[i]))]))
        if len(sorted_trigraphs)>i:
            # print(sorted_bigraphs[i],len(sorted_bigraphs[i]))
            cyphertext_trigraph_frequency_labels[i][0].configure(text = sorted_trigraphs[i])
            cyphertext_trigraph_frequency_labels[i][1].configure(text = round(100*cyphertext_trigraph_frequency[sorted_trigraphs[i]]/len(cyphertext_trigraph_list),1))
            cyphertext_trigraph_frequency_labels[i][2].configure(text = "".join([backkey[sorted_trigraphs[i][j]] for j in range(len(sorted_trigraphs[i]))]))
    if len(sorted_bigraphs)<13:
        for l in range(len(sorted_bigraphs),13):
            cyphertext_bigraph_frequency_labels[l][0].configure(text = "-")
            cyphertext_bigraph_frequency_labels[l][1].configure(text =  0)
    if len(sorted_trigraphs)<13:
        for l in range(len(sorted_trigraphs),13):
            cyphertext_trigraph_frequency_labels[l][0].configure(text = "-")
            cyphertext_trigraph_frequency_labels[l][1].configure(text =  0)




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
plain_bigraphfrequency_frame = Frame(
    window,
    width=(800*6/28),
    height=(600*12/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )
plain_trigraphfrequency_frame = Frame(
    window,
    width=(800*6/28),
    height=(600*12/26),
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
cypher_bigraphfrequency_frame = Frame(
    window,
    width=(800*6/28),
    height=(600*12/26),
    relief = FLAT,
    background = "light blue",
    borderwidth = 2
    )
cypher_trigraphfrequency_frame = Frame(
    window,
    width=(800*6/28),
    height=(600*12/26),
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

plaintext = StringVar()
plaintext = "plaintext"
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
    # textvariable = cyphertext,
    font=("Calibri 18"),
    width=60,
    height=8
    )
plaintext_entry.insert(END, plaintext)

plaintext_entry.vbar.config(troughcolor = 'lightblue', activebackground = 'blue', bg = 'blue')
plaintext_entry_label.grid(row = 0, column = 0)
plaintext_entry.grid(row = 1, column = 0)

# scroll = Scrollbar(plaintext_frame)
# plaintext_entry.configure(yscrollcommand=scroll.set)
#
# scroll.config(command=plaintext_entry.yview)
# scroll.grid(row = 1, column = 1)

cyphertext = StringVar()
cyphertext = "CYPHERTEXT"
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
    # textvariable = cyphertext,
    font=("Calibri 18"),
    width=60,
    height=8
    )
cyphertext_entry.insert(END, cyphertext)

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
        command = lambda: reorder("plaintext")
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
        command = lambda: reorder("plaintext")
        )

frequency_button = Button(
        button_frame,
        text="frequency",
        width=80,
        height=600*2/2/26,
        fg="yellow",
        bg = "blue",
        activebackground="lightblue",
        borderwidth=4,
        command = lambda: frequency()
        )


encrypt_button.grid(row = 0, column = 2, padx = (263,12), pady=20, sticky = "")
decrypt_button.grid(row = 0, column = 3, sticky = "")

frequency_button.grid(row = 0, column = 4, padx = (120,12), pady=20, sticky = "")




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

## Create common english bigraph frequency table
labelwidth = 3
labelheight = 1
labelborder = 1
#bigraph frequency from: https://www.researchgate.net/figure/English-bigram-frequencies-in-percent_tbl2_343699517
common_bigraph_letters =         [ "th", "he", "in", "er", "an", "re", "es", "on", "st", "nt", "en", "at", "ed"] #, "b", "v", "k",  "j",  "x",   "q", "z"]
common_bigraph_letter_frequency = [2.71, 2.33, 2.03, 1.78, 1.61, 1.41, 1.32, 1.32, 1.25, 1.17, 1.13, 1.12, 1.08] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
for letter in common_bigraph_letters: # Bigraph Frequency

    letter_label = Label(
    plain_bigraphfrequency_frame,
    text = common_bigraph_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    plain_bigraphfrequency_frame,
    text = common_bigraph_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth+2,
    height = labelheight
    )

    letter_label.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
    label.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
    xl=2
    i = i+1

## Create common english trigraph frequency table
labelwidth = 3
labelheight = 1
labelborder = 1
#trigraph frequency from: https://case.edu/artsci/math/singer/Sage%204/ngram-frequency.html
common_trigraph_letters =         ["the","and","ing","ent","ion","her","for","tha","nth","int","ere","tio","ter"]
common_trigraph_letter_frequency = [1.81, 0.73, 0.72, 0.42, 0.42, 0.36, 0.34, 0.33, 0.33, 0.32, 0.31, 0.31, 0.30] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
common_trigraph_frequency_labels = []

for letter in common_trigraph_letters: # Trigraph Frequency

    letter_label = Label(
    plain_trigraphfrequency_frame,
    text = common_trigraph_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    plain_trigraphfrequency_frame,
    text = common_trigraph_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth+3,
    height = labelheight
    )

    letter_label.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
    label.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
    xl=2
    i = i+1


## Create cyphertext letter frequency table
labelwidth = 3
labelheight = 2
labelborder = 1
#letter frequency from "CYPHERTEXT"

common_cypher_letters =         [ "E",  "T",  "C",  "Y",  "P",  "H",  "R",  "X", "-","-","-","-","-","-","-","-","-","-","-"] #, "b", "v", "k",  "j",  "x",   "q", "z"]
common_cypher_letter_frequency = [20.0, 20.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]

i = 0
xl = 9
cyphertext_frequency_labels = []
for letter in common_cypher_letters: # Letter Frequency

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

    cyphertext_frequency_labels.append([letter_label,label])

    letter_label.grid(row = 1, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    label.grid(row = 0, column = i+1, padx = (xl,2) , pady = 8, sticky = "")
    xl=2
    i = i+1

## Create cyphertext bigraph frequency table
a = round(100/9,2)
cypher_bigraph_letters =         ["CY","YP","PH","HE","ER","RT","TE","EX","XT","-","-","-","-"] #, "b", "v", "k",  "j",  "x",   "q", "z"]
cypher_bigraph_letter_frequency = [ a,   a,   a,   a,   a,   a,   a,   a,   a,  0,  0,  0,  0 ] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
labelwidth = 3
labelheight = 1
labelborder = 1
cyphertext_bigraph_frequency_labels = []
for letter in cypher_bigraph_letters: # Bigraph Frequency

    letter_label = Label(
    cypher_bigraphfrequency_frame,
    text = cypher_bigraph_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    cypher_bigraphfrequency_frame,
    text = cypher_bigraph_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth+2,
    height = labelheight
    )
    letter_label2 = Label(
    cypher_bigraphfrequency_frame,
    text = cypher_bigraph_letters[i].lower(),
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )

    cyphertext_bigraph_frequency_labels.append([letter_label,label,letter_label2])

    letter_label2.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
    letter_label.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
    label.grid(row = i, column = 2, padx = (xl,2) , pady = 2, sticky = "")
    xl=2
    i = i+1


## Create cyphertext trigraph frequency table
a = round(100/8,2)
cypher_trigraph_letters =         ["CYP","YPH","PHE","HER","ERT","RTE","TEX","EXT","-","-","-","-","-"]
cypher_trigraph_letter_frequency = [  a,    a,    a,    a,    a,    a,    a,    a,   0,  0,  0,  0,  0 ] #, 1.5, 0.9, 0.8, 0.153, 0.015, 0.09, 0.07]
i = 0
labelwidth = 3
labelheight = 1
labelborder = 1
cyphertext_trigraph_frequency_labels = []
for letter in cypher_trigraph_letters: # Bigraph Frequency

    letter_label = Label(
    cypher_trigraphfrequency_frame,
    text = cypher_trigraph_letters[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )
    label = Label(
    cypher_trigraphfrequency_frame,
    text = cypher_trigraph_letter_frequency[i],
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth+2,
    height = labelheight
    )
    letter_label2 = Label(
    cypher_trigraphfrequency_frame,
    text = cypher_trigraph_letters[i].lower(),
    relief = FLAT,
    bg = "blue",
    fg = "light blue",
    borderwidth = labelborder,
    width = labelwidth,
    height = labelheight
    )

    cyphertext_trigraph_frequency_labels.append([letter_label,label,letter_label2])

    letter_label2.grid(row = i, column = 0, padx = (xl,2) , pady = 2, sticky = "")
    letter_label.grid(row = i, column = 1, padx = (xl,2) , pady = 2, sticky = "")
    label.grid(row = i, column = 2, padx = (xl,2) , pady = 2, sticky = "")
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

        # svs[j][i].trace("w", lambda name, index, mode, sv=svs[j][i], i=i, j=j: callback(sv,j,i))

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
for i in range(26):
    for j in range(2):
        svs[j][i].trace_add("write", lambda name, index, mode, sv=svs[j][i], i=i, j=j: callback(sv,j,i))


def get_cyphertext_stringvar(event):
    cyphertext = cyphertext_entry.get("1.0", "end-1c").upper()
    cyphertext_entry.replace("1.0", END, cyphertext)


def get_plaintext_stringvar(event):
    plaintext = plaintext_entry.get("1.0", "end-1c").lower()
    plaintext_entry.replace("1.0", END, plaintext)



cyphertext_entry.bind('<KeyRelease>', get_cyphertext_stringvar)
plaintext_entry.bind('<KeyRelease>', get_plaintext_stringvar)



plaintext_frame.grid(row = 0, column = 0, rowspan = 9, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")
plain_frequency_frame.grid(row = 9, column = 0, rowspan = 4, columnspan = 6, padx = 2 , pady = 0, sticky = "nesw")
button_frame.grid(row = 13, column = 0, rowspan = 3, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")
cypher_frequency_frame.grid(row = 16, column = 0, rowspan = 4, columnspan = 6, padx = 2 , pady = 0, sticky = "nesw")
cyphertext_frame.grid(row = 20, column = 0, rowspan = 9, columnspan = 6, padx = 2 , pady = 2, sticky = "nesw")

letter_conversion_frame.grid(row = 0, column = 7, rowspan = 26, columnspan = 1, padx = 2 , pady = 2, sticky = "nesw")

plain_bigraphfrequency_frame.grid(row = 0, column = 8, columnspan = 1, rowspan = 14)
cypher_bigraphfrequency_frame.grid(row = 12, column = 8, columnspan = 1, rowspan = 14)

plain_trigraphfrequency_frame.grid(row = 0, column = 9, columnspan = 1, rowspan = 14)
cypher_trigraphfrequency_frame.grid(row = 12, column = 9, columnspan = 1, rowspan = 14)

window.mainloop()
