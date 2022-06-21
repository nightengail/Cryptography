# from tkinter import *
#
# window = Tk()
# window.title("test for scrollbar")
# window.config(pady=50, padx=50, bg="blue")
#
#
# text_box = Text(width=49, height=5, bg="lightblue", highlightthickness=1, foreground="black",
#                     insertbackground="purple", wrap="word")
# tex_scroll = Scrollbar(orient=VERTICAL,)
#
# tex_scroll.config(command=text_box.yview, )
# text_box["yscrollcommand"] = tex_scroll.set
#
# text_box.grid(column=1, row=4, columnspan=2, sticky="w")
# tex_scroll.grid(column=2, row=4, sticky="nse")
#
# window.mainloop()


# from tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root, troughcolor = "blue")
# scrollbar.pack( side = RIGHT, fill = Y )
#
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
#
# mainloop()
# ##https://www.tutorialspoint.com/python/tk_scrollbar.htm

# import tkinter as tk
#
# win = tk.Tk()
#
# win.configure(background="#808000")
#
# frame1 = tk.Frame(win,width=80, height=80,bg = '#ffffff',
#                   borderwidth=1, relief="sunken")
# scrollbar = tk.Scrollbar(frame1)
# editArea = tk.Text(frame1, width=10, height=10, wrap="word",
#                    yscrollcommand=scrollbar.set,
#                    borderwidth=0, highlightthickness=0)
# scrollbar.config(command=editArea.yview)
# scrollbar.pack(side="right", fill="y")
# editArea.pack(side="left", fill="both", expand=True)
# frame1.place(x=10,y=30)
#
# win.mainloop()

# Import the required library
from tkinter import*
# Create an instance of tkinter
framewin=Tk()
# Set the size of the Tkinter window
framewin.geometry("700x350")
# Add a frame to set the size of the window
frame=Frame(framewin,relief='sunken')
frame.grid(sticky="we")
# Make the frame sticky for every case
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)
# Make the window sticky for every case
framewin.grid_rowconfigure(0,weight=1)
framewin.grid_columnconfigure(0,weight=1)
# Add a label widget
label=Label(frame,text="Hey Folks! Welcome to Tutorialspoint",
    font=('Helvetica 15 bold'),
    bg="white")

label.grid(row=3,column=0)
label.grid_rowconfigure(1,weight=1)
label.grid_columnconfigure(1,weight=1)

def callback(sv):
    print (sv.get())

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(framewin, textvariable=sv)
e.pack()

framewin.mainloop()



# import tkinter as tk
# import tkinter.scrolledtext as tkst
#
# win = tk.Tk()
# frame1 = tk.Frame(
#     master = win,
#     bg = '#808000'
# )
# frame1.pack(fill='both', expand='yes')
# editArea = tkst.ScrolledText(
#     master = frame1,
#     wrap   = tk.WORD,
#     width  = 20,
#     height = 10
# )
# # Don't use widget.place(), use pack or grid instead, since
# # They behave better on scaling the window -- and you don't
# # have to calculate it manually!
# editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# # Adding some text, to see if scroll is working as we expect it
# editArea.insert(tk.INSERT,
# """\
# Integer posuere erat a ante venenatis dapibus.
# Posuere velit aliquet.
# Aenean eu leo quam. Pellentesque ornare sem.
# Lacinia quam venenatis vestibulum.
# Nulla vitae elit libero, a pharetra augue.
# Cum sociis natoque penatibus et magnis dis.
# Parturient montes, nascetur ridiculus mus.
# """)
# win.mainloop()
#

# # Import the required libraries
# from tkinter import *
# from tkinter import ttk
#
# # Create an instance of Tkinter Frame
# win = Tk()
#
# # Set the geometry of Tkinter Frame
# win.geometry("700x250")
#
# style=ttk.Style()
# style.theme_use('classic')
# style.configure("Vertical.TScrollbar", troughcolor = "lightblue", background="blue", bordercolor="red", arrowcolor="blue")
#
# # Create a vertical scrollbar
# scrollbar = ttk.Scrollbar(win, orient='vertical')
# scrollbar.pack(side=RIGHT, fill=BOTH)
#
# # Add a Text Widget
# text = Text(win, width=15, height=15, wrap=CHAR,
# yscrollcommand=scrollbar.set)
#
# for i in range(1000):
#    text.insert(END, i)
#
# text.pack(side=TOP, fill=X)
#
# # Configure the scrollbar
# scrollbar.config(command=text.yview)
#
# win.mainloop()
# ##https://www.tutorialspoint.com/changing-the-appearance-of-a-scrollbar-in-tkinter-using-ttk-styles




# from tkinter import *
# import tkinter as tk
# root = tk.Tk()
# root.geometry('1000x800')
# root.configure(bg='blue')
# TextArea = Text(root, width=20,bg='#373B3F')
# TextArea.place(x=350, y=40, width=250, height=250)
# sscrollbar = tk.Scrollbar(TextArea, orient='vertical')
# sscrollbar.pack(side=RIGHT, fill=Y)
# TextArea.configure(yscrollcommand=sscrollbar.set)
# sscrollbar.configure(command=TextArea.yview)
# sscrollbar.configure(activebackground='red',bg='red')
#
# root.mainloop()



# import tkinter as tk
# from tkinter import ttk
#
# class Gui:
#     def __init__(self,mainframe):
#
#         #set the style
#         style = ttk.Style()
#         style.configure('Horizontal.TScrollbar',background = "blue" )
#
#         #Create a mainframe
#         self.mainframe = mainframe
#         self.mainframe.title("example")
#
#
#         #creating scrollbar frame
#         scrl_attr_frame = ttk.Frame(self.mainframe)
#         scrl_attr_frame.grid(column=0,row=5,sticky="ns")
#         scrl_attr_frame.rowconfigure(0, weight=1)
#         attr_canvas = tk.Canvas(scrl_attr_frame)
#         h_scroll = ttk.Scrollbar(scrl_attr_frame,orient="horizontal", command=attr_canvas.xview)
#         attr_canvas.configure(xscrollcommand=h_scroll.set)
#         attr_canvas.grid(column=0,row=0,sticky="ns")
#         h_scroll.grid(column=0, row=1,sticky="we")
#         attr_frame = ttk.Frame(attr_canvas)
#         attr_frame.grid(column=0,row=0,sticky="ns")
#         attr_canvas.create_window((0,0),window=attr_frame, anchor='nw')
#         attr_frame.bind("<Configure>",lambda event, canvas=attr_canvas : canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200,takefocus=False,highlightthickness=0))#attribute_frame.winfo_height()/20,highlightthickness=0))
#
#         #setup treeview widget
#         tree_columns = ("c1", "c2", "c3")
#
#         self.tree = ttk.Treeview(attr_frame,columns=tree_columns, show="headings",takefocus=False)
#         self.tree.grid(column=0, row=0, sticky='nsew')
#
#         for head in tree_columns:
#             self.tree.heading(head,text=head,anchor="w")
#
#
# root = tk.Tk()
# myapp = Gui(root)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# def main():
#     app = Tk()
#     style = Style()
#
#     # import the 'trough' element from the 'default' engine.
#     style.element_create("My.Vertical.Scrollbar.trough", "from", "default")
#
#     # Redefine the horizontal scrollbar layout to use the custom trough.
#     # This one is appropriate for the 'vista' theme.
#     style.layout("My.Vertical.TScrollbar",
#         [('My.Vertical.Scrollbar.trough', {'children':
#             [('Vertical.Scrollbar.uparrow', {'side': 'top', 'sticky': ''}),
#              ('Vertical.Scrollbar.downarrow', {'side': 'bottom', 'sticky': ''}),
#              ('Vertical.Scrollbar.thumb', {'unit': '1', 'children':
#                  [('Vertical.Scrollbar.grip', {'sticky': ''})],
#             'sticky': 'nswe'})],
#         'sticky': 'ns'})])
#     # Copy original style configuration and add our new custom configuration option.
#     # style.configure("My.Horizontal.TScrollbar", *style.configure("Horizontal.TScrollbar"))
#     style.configure("My.Vertical.TScrollbar", troughcolor="lightblue")
#
#     # Create and show a widget using the custom style
#     hs = Scrollbar(app, orient="vertical", style="My.Vertical.TScrollbar")
#     hs.place(x=5, y=5, width=200, height=200)
#     hs.set(0.4,0.6)
#
#     app.mainloop()
#
# if __name__ == '__main__':
#     main()
