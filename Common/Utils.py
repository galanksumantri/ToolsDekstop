from tkinter import *
import webbrowser
from .Var import *

def label(text, x, y, border, font=FONT_BODY1):
    name = Label(border, text=text, bg=BACKGROUND, font=font)
    name.place(relx=x, rely=y, anchor=CENTER)

def input(INPUT, x, y, border):
    entry1 = Entry(border, text = INPUT, font=FONT_BODY2)
    entry1.place(relx=x, rely=y, anchor=CENTER, height=30, width=200)

def buttonPlace(border, width, x, y, text, command):
    button = Button(border, text=text, width=width, font=FONT_BODY1, command=command)
    button.place(relx=x, rely=y, anchor=CENTER)

def formatRibuan(x):
    return format(x, ',d').replace(",",".")

def OpenUrl(url):
    webbrowser.open_new(url)