import tkinter as tk
import webbrowser
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from gui import login
from postgres import songTableClass as songClass
from postgres import userTableClass as userClass

user = userClass.Users()
song = songClass.Songs()


def goToLogin(window):
    window.destroy()
    login.loginFormWindow()


def openPayPal():
    url = "https://www.paypal.com/ro/business"
    webbrowser.open(url, new=1)


def register(nameEntry, passwordEntry, rePasswordEntry, window):
    inputUsername = (nameEntry.get())
    inputPassword = (passwordEntry.get())
    inputRePassword = (rePasswordEntry.get())
    if inputUsername == "":
        passwordEntry.delete(0, tk.END)
        rePasswordEntry.delete(0, tk.END)
        tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
    else:

        count = user.getCountUserByUsername(inputUsername)[0][0]
        if count == 1:
            passwordEntry.delete(0, tk.END)
            rePasswordEntry.delete(0, tk.END)
            tk.messagebox.showwarning(title="Error", message="Username is already used")
        else:
            if inputPassword == "":
                rePasswordEntry.delete(0, tk.END)
                tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
            else:
                if inputRePassword == "":
                    tk.messagebox.showwarning(title="Error", message="Password confirmation cannot be empty")
                else:
                    if len(inputPassword) < 8:
                        passwordEntry.delete(0, tk.END)
                        rePasswordEntry.delete(0, tk.END)
                        tk.messagebox.showwarning(title="Error", message="Password must be at least 8 characters")
                    else:
                        if inputPassword != inputRePassword:
                            rePasswordEntry.delete(0, tk.END)
                            tk.messagebox.showwarning(title="Error", message="Passwords do not match")
                        else:
                            confirmation = user.insertUser(inputUsername, inputPassword)
                            if confirmation:
                                tk.messagebox.showwarning(title="Error",
                                                          message="Register Successfully")
                                goToLogin(window)
                            else:
                                tk.messagebox.showwarning(title="Error",
                                                          message="Register Failed")


def registerFormWindow():
    # Login Window
    registerWindow = tk.Tk()
    registerWindow.top_bar = tk.Frame(registerWindow, bg="Red", cursor="sizing")
    registerWindow.title("Register")
    registerWindow.configure(bg="#5a5b5e")
    registerWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(registerWindow.winfo_screenwidth() * 0.3)
    screenHeight = round(registerWindow.winfo_screenheight() * 0.5)
    registerWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        registerWindow,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)
    # BUTTON SIZE
    buttonWidth = 30

    # FORM

    registerWindow.configure(background="grey")
    nameLabel = tk.Label(registerWindow, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )

    passwordLabel = tk.Label(registerWindow, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    rePasswordLabel = tk.Label(registerWindow, text='Re-Password', width=10,
                               bg="#5c1a56",
                               fg="silver", font="sans 8 bold", )

    nameEntry = tk.Entry(registerWindow, width=50)

    passwordEntry = tk.Entry(registerWindow, show="\u2022", width=50)
    rePasswordEntry = tk.Entry(registerWindow, show="\u2022", width=50)

    registerButton = tk.Button(registerWindow, width=int(buttonWidth / 2),
                               text='Register', bg="#5c1a56",
                               fg="silver", font="sans 8 bold",
                               command=lambda: register(nameEntry, passwordEntry,
                                                        rePasswordEntry,
                                                        registerWindow))

    # BUTTON
    loginButton = tk.Button(registerWindow, text="Login", width=int(buttonWidth / 2),
                            bg="#5c1a56",
                            fg="silver",
                            font="sans 8 bold",
                            command=lambda: goToLogin(registerWindow))

    # PACKING

    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 1.5)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 3.5)
    rePasswordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 5.5)
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 1.5)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 3.5)
    rePasswordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 5.5)
    registerButton.place(x=150, y=screenHeight / 10 * 7)
    loginButton.place(x=150, y=screenHeight / 10 * 8.5)
    registerWindow.mainloop()
