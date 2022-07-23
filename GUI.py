from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

from Pages.homepage import HomePage
from Pages.signUpPage import SignUpPage

root = Tk()
page = Toplevel(root)
img = PhotoImage(file="image/login.png")
Label(page, image=img, bg="white").place(x=50, y=50)

def createSignInPage(root):
    root.title("Login")
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    # root.resizable(False, False)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text="Sign in", fg="#57a1f8",bg="white",font=("Microsoft Tahei UI Light",23,"bold"))
    heading.place(x=100,y=5)

# #####-------------------------------------------------------------------------------------------------------
    def username_section(label_x,label_y,entry_x,entry_y,entry_width):
        def on_enter(e):
            user.delete((0,'end'))
        def on_leave(e):
            name=user.get()
            if name == "":
                user.insert(0,"Enter your username")
        username_label=Label(frame,text="Username", fg="#57a1f8",bg="white",font=("Microsoft Tahei UI Light",12,"bold"))
        username_label.place(x=label_x,y=label_y)
        user = Entry(frame,width=entry_width,fg="black",border=2,bg="white",font=("Microsoft Tahei UI Light",9))
        user.place(x=entry_x,y=entry_y)
        # user.insert(0,"Enter your username")
        user.bind(("<FocusIn>",on_enter))
        user.bind(("<FocusOut>",on_leave))
        return user
    username_entry = username_section(20,80,105,80,25)

    Frame(frame,width=475,height=1,bg="black").place(x=25,y=110)

# #####-------------------------------------------------------------------------------------------------------
    def passw_section(label_x,label_y,entry_x,entry_y,entry_width):
        def on_enter(e):
            passwr.delete((0,'end'))
        def on_leave(e):
            name=passwr.get()
            if name == "":
                passwr.insert(0,"Enter your password")
        passw_label=Label(frame, text="Password", fg="#57a1f8",bg="white", font=("Microsoft Tahei UI Light", 12,"bold"))
        passw_label.place(x=label_x,y=label_y)
        passwr = Entry(frame,show="*", width=entry_width, fg="black", border=2, bg="white", font=("Microsoft Tahei UI Light", 9))
        passwr.place(x=entry_x,y=entry_y)
        # passwr.insert(0,"Enter your password")
        passwr.bind(("<FocusIn>",on_enter))
        passwr.bind(("<FocusOut>",on_leave))
        return passwr
    password_entry = passw_section(20,130,105,130,25)

    Frame(frame,width=375,height=1,bg="black").place(x=25,y=160)
# #####-------------------------------------------------------------------------------------------------------
    def signin():
        username = username_entry.get()
        password = password_entry.get()
        if username=="admin" and password=="1234":
            print("Admin sign in")
            enterHomePage = HomePage(username,password)
            enterHomePage.showPage(root,925,500,300,200)
        elif username != "admin" and password != "1234":
            messagebox.showerror("Error","Invalid username and password")
        elif password != "1234":
            messagebox.showerror("Error","Wrong password was entered")
        elif username != "admin":
            messagebox.showerror("Error","Wrong username was entered")
    def signup():
        enterHomePage = SignUpPage(root, 925, 500, 300, 200)
        print(" sign up")

    Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
    label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=75,y=270)

    sign_up_button=Button(frame,width=6,text="Sign Up",border=0,bg="white",fg="#57a1f8",cursor="hand2",command=signup,font=("Microsoft YaHei UI Light",10))
    sign_up_button.place(x=215,y=267)
    root.mainloop()
root.withdraw()
createSignInPage(page)





