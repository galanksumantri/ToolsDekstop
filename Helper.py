from tkinter import *

BACKGROUND = "lightgrey"
FONT = 'Arial'

def label(text, x, y, inputFrame):
    name = Label(inputFrame, text=text, bg=BACKGROUND, font=(FONT, 15))
    name.place(relx=x, rely=y, anchor=CENTER)

def input(INPUT, x, y, inputFrame):
    entry1 = Entry(inputFrame, text = INPUT, font=(FONT, 13))
    entry1.place(relx=x, rely=y, anchor=CENTER, height=30, width=200)

def buttonPlace(border, width, x, y, text, command):
    button = Button(border, text=text, width=width, font=(FONT, 15), command=command)
    button.place(relx=x, rely=y, anchor=CENTER)

def formatRibuan(x):
    return format(x, ',d').replace(",",".")
