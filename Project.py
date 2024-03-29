from tkinter import *
from math import factorial
from tkinter import messagebox
from Common.Var import *
from Common.Utils import *

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)

        border = LabelFrame(self, text='Home', bg=BACKGROUND, bd = 5, font=FONT_H2)
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label("MY TOOLS", 0.5, 0.2, border, FONT_H1)
        buttonPlace(border, 30, 0.5, 0.358, "Factorial Calc", lambda: controller.show_frame(FactorialPage))
        buttonPlace(border, 30, 0.5, 0.460, "Divisors Calc", lambda: controller.show_frame(DivisorsPage))
        buttonPlace(border, 30, 0.5, 0.563, "Check Major/Minor", lambda: controller.show_frame(MajorMinorPage))
        buttonPlace(border, 30, 0.5, 0.666, "About Me", lambda: controller.show_frame(AboutMePage))

class FactorialPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT = StringVar()

        def onPress():
            try:
                if INPUT.get() == "":
                    messagebox.showerror("Error", "Please fill a number")
                elif int(INPUT.get()) < 0:
                    messagebox.showerror("Error", "A number must be large than 0") 
                elif int(INPUT.get()) > 40:
                    messagebox.showerror("Error", "The max number is 40")   
                else:
                    num = int(INPUT.get())       
                    fact = factorial(num)
                    result['text'] = f"The factorial of {num} is {formatRibuan(fact)}"
            except ValueError:
                messagebox.showerror("Error", "Only a number are allowed in N")

        border = LabelFrame(self, text='Factorial Calc', bg=BACKGROUND, bd = 5, font=FONT_H2)
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label("Enter value of integer N (Max 40) : ", 0.5, 0.4, border)
        input(INPUT, 0.5, 0.5, border)
        buttonPlace(border, 8, 0.5, 0.7, "Validate", onPress)
        buttonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

        result = Label(border, text="Enter a number first!", bg=BACKGROUND, font=FONT_BODY1)
        result.place(relx=0.5, rely=0.2, anchor=CENTER)

class DivisorsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT = StringVar()

        def onPress():
            div = []
            try:
                if INPUT.get() == "":
                    messagebox.showerror("Error", "Please fill a number")
                elif int(INPUT.get()) < 0:
                    messagebox.showerror("Error", "A number must be large than 0")   
                elif int(INPUT.get()) > 1000:
                    messagebox.showerror("Error", "The max number is 1000")   
                else:
                    numb = int(INPUT.get())
                    for i in range(1, numb+1):
                        if (numb % i) == 0:
                            div.append(i)
                    divisors['text'] = f"The divisors of {numb} : " + ', '.join(str(x) for x in div)
            except ValueError:
                messagebox.showerror("Error", "Only a number are allowed in N")

        border = LabelFrame(self, text='Divisors Calc', bg=BACKGROUND, bd = 5, font=FONT_H2)
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label("Enter the value of N (Max 1000) :", 0.5, 0.4, border)
        input(INPUT, 0.5, 0.5, border)
        buttonPlace(border, 8, 0.5, 0.7, "Validate", onPress)
        buttonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

        divisors = Label(border, text="The divisors of N : none", anchor="w", bg=BACKGROUND, font=FONT_BODY1)
        divisors.place(relx=0.5, rely=0.2, anchor=CENTER)

class MajorMinorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg=BACKGROUND)
        INPUT_NAME = StringVar()
        INPUT_AGE = StringVar()

        def onPress():
            if INPUT_AGE.get() == "" or INPUT_NAME.get() == "":
                messagebox.showerror("Error", "Please fill all data")
            else:
                try:
                    age = int(INPUT_AGE.get())
                    if age < 0:
                        age = None
                        messagebox.showerror("Error", "A number must be large than 0")
                    elif age >= 18: 
                        age = "major!"
                    else: 
                        age = "minor!"    
                    result['text'] = f"Welcome: {INPUT_NAME.get()} you are {age}"
                except ValueError:
                    messagebox.showerror("Error", "Only a number are allowed in age")

        border = LabelFrame(self, text="Check Major/Minor", bg=BACKGROUND, bd = 5, font=FONT_H2)
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label("Enter your name :", 0.37, 0.38, border)
        label("The your age   :", 0.37, 0.48, border)
        input(INPUT_NAME, 0.59, 0.38, border)
        input(INPUT_AGE, 0.59, 0.48, border)
        buttonPlace(border, 8, 0.5, 0.7, "Validate", onPress)
        buttonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

        result = Label(border, text="Enter a data first!", bg=BACKGROUND, font=FONT_BODY1)
        result.place(relx=0.5, rely=0.2, anchor=CENTER)

class AboutMePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg=BACKGROUND)

        border = LabelFrame(self, text='About Me', bg=BACKGROUND, bd = 5, font=FONT_H2)
        border.pack(fill="both", expand="yes", padx = 250, pady=(140, 200))

        label = Label(border, text="Galang Sumantri", bg = BACKGROUND, font=FONT_H1)
        label.place(relx=0.35, rely=0.45, anchor=CENTER)

        buttonPlace(border, 8, 0.58, 0.45, "Linkedin", lambda: OpenUrl(URL1))
        buttonPlace(border, 8, 0.7, 0.45, "Instagram", lambda: OpenUrl(URL2))
        buttonPlace(border, 5, 0.935, 0.9, "Home", lambda: controller.show_frame(HomePage))

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
        for F in (HomePage, AboutMePage, DivisorsPage, FactorialPage, MajorMinorPage):
            frame = F(page, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(HomePage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


if __name__=="__main__":
    app = Window()
    app.mainloop()
