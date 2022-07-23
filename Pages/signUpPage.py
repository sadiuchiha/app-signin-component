from tkinter import *

from Pages.homepage import HomePage


class SignUpPage:
    def __init__(self, root, width, height, x, y):
        self.root = root
        self.page = Toplevel(self.root)
        img = PhotoImage(file="image/register.png")
        Label(self.page, image=img, bg="white").place(x=50, y=50)
        self.page.title("Sign Up")
        self.page.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
        self.page.config(bg="white")
        # Label(self.page, text="Sign Up Page!", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
        # Button(self.page, width=39, pady=7, text="Back to Sign in", bg="#57a1f8", fg="white", border=0, command=self.backToSignIn()).place(x=35,
        #                                                                                                           y=204)
        self.createSignInPage(self.page)
        self.root.withdraw()
        self.page.mainloop()

    def createSignInPage(self,root):
        root.title("Sign Up")
        root.geometry("925x500+300+200")
        root.configure(bg="#fff")
        root.resizable(False, False)

        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft Tahei UI Light", 23, "bold"))
        heading.place(x=100, y=5)

        # #####-------------------------------------------------------------------------------------------------------
        def username_section(label_x, label_y, entry_x, entry_y, entry_width):
            def on_enter(e):
                user.delete((0, 'end'))

            def on_leave(e):
                name = user.get()
                if name == "":
                    user.insert(0, "Enter your username")

            username_label = Label(frame, text="Username", fg="#57a1f8", bg="white",
                                   font=("Microsoft Tahei UI Light", 12, "bold"))
            username_label.place(x=label_x, y=label_y)
            user = Entry(frame, width=entry_width, fg="black", border=2, bg="white",
                         font=("Microsoft Tahei UI Light", 9))
            user.place(x=entry_x, y=entry_y)
            # user.insert(0,"Enter your username")
            user.bind(("<FocusIn>", on_enter))
            user.bind(("<FocusOut>", on_leave))
            return user

        username_entry = username_section(20, 80, 105, 80, 25)

        Frame(frame, width=475, height=1, bg="black").place(x=25, y=110)

        # #####-------------------------------------------------------------------------------------------------------
        def passw_section(label_x, label_y, entry_x, entry_y, entry_width):
            def on_enter(e):
                passwr.delete((0, 'end'))

            def on_leave(e):
                name = passwr.get()
                if name == "":
                    passwr.insert(0, "Enter your password")

            passw_label = Label(frame, text="Password", fg="#57a1f8", bg="white",
                                font=("Microsoft Tahei UI Light", 12, "bold"))
            passw_label.place(x=label_x, y=label_y)
            passwr = Entry(frame, show="*", width=entry_width, fg="black", border=2, bg="white",
                           font=("Microsoft Tahei UI Light", 9))
            passwr.place(x=entry_x, y=entry_y)
            # passwr.insert(0,"Enter your password")
            passwr.bind(("<FocusIn>", on_enter))
            passwr.bind(("<FocusOut>", on_leave))
            return passwr

        password_entry = passw_section(20, 130, 105, 130, 25)

        Frame(frame, width=375, height=1, bg="black").place(x=25, y=160)

        # #####-------------------------------------------------------------------------------------------------------
        def email_section(label_x, label_y, entry_x, entry_y, entry_width):
            def on_enter(e):
                email.delete((0, 'end'))

            def on_leave(e):
                name = email.get()
                if name == "":
                    email.insert(0, "Enter your emailname")

            email_label = Label(frame, text="Email", fg="#57a1f8", bg="white",
                                   font=("Microsoft Tahei UI Light", 12, "bold"))
            email_label.place(x=label_x, y=label_y)
            email = Entry(frame, width=entry_width, fg="black", border=2, bg="white",
                         font=("Microsoft Tahei UI Light", 9))
            email.place(x=entry_x, y=entry_y)
            # email.insert(0,"Enter your email")
            email.bind(("<FocusIn>", on_enter))
            email.bind(("<FocusOut>", on_leave))
            return email

        email_entry = email_section(20, 180, 105, 180, 25)

        Frame(frame, width=475, height=1, bg="black").place(x=25, y=210)

        # #####-------------------------------------------------------------------------------------------------------

        def signup():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            verified = self.verifyUser(username,email,password)
            if verified:
                enterHomePage = HomePage(self.page, 925, 500, 300, 200)
            print(" sign up")

        Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=signup)\
            .place(x=35, y=234)
        label = Label(frame, text="Have an account?", fg="black", bg="white",
                      font=("Microsoft YaHei UI Light", 9))
        label.place(x=75, y=290)

        sign_up_button = Button(frame, width=6, text="Sign In", border=0, bg="white", fg="#57a1f8", cursor="hand2",
                                command=signup, font=("Microsoft YaHei UI Light", 10))
        sign_up_button.place(x=180, y=287)

    def backToSignIn(self):
        self.page.withdraw()
        self.root.mainloop()

    def verifyUser(self,username,email,password):
        pass
