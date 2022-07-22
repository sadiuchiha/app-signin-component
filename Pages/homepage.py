from tkinter import *


class HomePage():
    def __init__(self,root,width, height, x, y):
        self.page = Toplevel(root)
        self.page.title("Home")
        self.page.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
        self.page.config(bg="white")
        Label(self.page, text="Home Page!", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
        root.withdraw()
        self.page.mainloop()