from tkinter import *

class SignUpPage:
    def __init__(self, root, width, height, x, y):
        self.root = root
        self.page = Toplevel(self.root)
        self.page.title("Sign Up")
        self.page.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
        self.page.config(bg="white")
        Label(self.page, text="Sign Up Page!", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
        # Button(self.page, width=39, pady=7, text="Back to Sign in", bg="#57a1f8", fg="white", border=0, command=self.backToSignIn()).place(x=35,
        #                                                                                                           y=204)
        self.root.withdraw()
        self.page.mainloop()

    def backToSignIn(self):
        self.page.withdraw()
        self.root.mainloop()


