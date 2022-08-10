from tkinter import *
import webbrowser
from math import factorial
from PIL import ImageTk, Image

BACKGROUND = "lightblue"
FONT = 'Arial'
urlGalangLinkedin = "https://linkedin.com/in/galangsumantri"
urlGalangInstagram = "https://www.instagram.com/galanksumantri/"

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)

        border = LabelFrame(self, text='Home', bg=BACKGROUND, bd = 5, font=(FONT, 20))
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label = Label(border, text="MY TOOLS", bg = BACKGROUND, font=("Arial Bold", 25))
        label.place(relx=0.5, rely=0.2, anchor=CENTER)

        Window.ButtonPlace(border, 30, 0.5, 0.358, "Factorial", lambda: controller.show_frame(FactorialPage))
        Window.ButtonPlace(border, 30, 0.5, 0.460, "Divisors", lambda: controller.show_frame(DivisorsPage))
        Window.ButtonPlace(border, 30, 0.5, 0.563, "Grouping", lambda: controller.show_frame(GroupingPage))
        Window.ButtonPlace(border, 30, 0.5, 0.666, "Tentangku", lambda: controller.show_frame(AboutMePage))

        load= Image.open("IMG_20190716_135354.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(border, image=render)
        img.photo = img
        img.place(x=100, y=100)

class AboutMePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg=BACKGROUND)

        border = LabelFrame(self, text='Tentangku', bg=BACKGROUND, bd = 5, font=(FONT, 20))
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label = Label(border, text="Galang Sumantri", bg = BACKGROUND, font=("Arial Bold", 25))
        label.place(relx=0.35, rely=0.2, anchor=CENTER)

        Window.ButtonPlace(border, 8, 0.58, 0.2, "Linkedin", lambda: controller.OpenUrl(urlGalangLinkedin))
        Window.ButtonPlace(border, 8, 0.7, 0.2, "Instagram", lambda: controller.OpenUrl(urlGalangInstagram))
        Window.ButtonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

class DivisorsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT = StringVar()

        def onPress():
            div = []
            num = int(INPUT.get())
            for i in range (1, num+1):
                if (num % i) == 0:
                    div.append(i)
            divisors['text'] = ', '.join(str(x) for x in div)

        border = LabelFrame(self, text='Divisors', bg=BACKGROUND, bd = 5, font=(FONT, 20))
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        inputFrame = Frame(border, bg=BACKGROUND)
        inputFrame.pack(padx=10, pady=10)

        Window.Label("Enter the value of N", 0, 0, inputFrame)
        Window.Label("The divisors of N   :", 1, 0, inputFrame)
        Window.Input(INPUT, 0, 1, inputFrame)

        divisors = Label(inputFrame, text="none", anchor="w", bg=BACKGROUND)
        divisors.grid(row=1, column=1, sticky="w")

        Window.ButtonGrid("Validate", 2, 1, inputFrame, onPress)
        Window.ButtonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

class FactorialPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT = StringVar()

        def onPress():
            num = int(INPUT.get())       
            fact = factorial(num)
            result['text'] = f"The factorial of {num} is {num}! = {fact}"

        border = LabelFrame(self, text='Tentang', bg=BACKGROUND, bd = 5, font=(FONT, 20))
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        inputFrame = Frame(border, bg=BACKGROUND)
        inputFrame.pack(padx=10, pady=10)

        Window.Label("Enter value of integer N :", 0, 0, inputFrame)
        Window.Input(INPUT, 0, 1, inputFrame)

        result = Label(inputFrame, text="Enter a number first!", bg=BACKGROUND)
        result.grid(row=2, column=1, sticky="w")

        Window.ButtonGrid("Validate", 3, 1, inputFrame, command=onPress)
        Window.ButtonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

class GroupingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT_NAME = StringVar()
        INPUT_AGE = StringVar()

        def onPress():
            age = int(INPUT_AGE.get())
            if age >= 18: 
                age = "major !"
            else: 
                age = "minor !"    
            result['text'] = f"Welcome: {INPUT_NAME.get()} you are {age}"

        border = LabelFrame(self, text="Grouping", bg=BACKGROUND, bd = 5, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        inputFrame = Frame(border, bg=BACKGROUND)
        inputFrame.pack(padx=10, pady=10)

        Window.Label("Enter your name", 0, 0, inputFrame)
        Window.Label("The your age   :", 1, 0, inputFrame)
        Window.Input(INPUT_NAME, 0, 1, inputFrame)
        Window.Input(INPUT_AGE, 1, 1, inputFrame)

        result = Label(inputFrame, text="Enter a data first!", bg=BACKGROUND)
        result.grid(row=2, column=1, sticky="w")

        Window.ButtonGrid("Validate", 3, 1, inputFrame, command=onPress)
        Window.ButtonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

class Window(Tk):
    def __init__(self, *args, **kwargs):  
        Tk.__init__(self, *args, **kwargs)
            
        page = Frame(self)
        page.pack()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        page.grid_rowconfigure(0, minsize=height)
        page.grid_columnconfigure(0, minsize=width)
        
        self.state('zoomed')
        
        self.frames = {}
        for F in (HomePage, AboutMePage, DivisorsPage, FactorialPage, GroupingPage):
            frame = F(page, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(HomePage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

    def OpenUrl(self, url):
        webbrowser.open_new(url)

    def Label(text, row, column, inputFrame):
        name = Label(inputFrame, text=text, bg=BACKGROUND)
        name.grid(row=row, column=column, sticky="w")

    def Input(INPUT, row, column, inputFrame):
        entry1 = Entry(inputFrame, text = INPUT)
        entry1.grid(row=row, column=column, sticky="w")

    def ButtonGrid(text, row, column, inputFrame, command):
        button = Button(inputFrame, text=text, command=command)
        button.grid(row=row, column=column, pady=5)

    def ButtonPlace(border, width, x, y, text, command):
        button = Button(border, text=text, width=width, font=(FONT, 15), command=command)
        button.place(relx=x, rely=y, anchor=CENTER)

Window().mainloop()
