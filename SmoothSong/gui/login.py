import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from gui import player, register
from postgres import songTableClass as songClass
from postgres import userTableClass as userClass
from postgres import downloadedTableClass as downloadedClass
from utils import crypt

user = userClass.Users()
song = songClass.Songs()
downloaded = downloadedClass.Downloaded()


def goToRegister(window):
    window.destroy()
    register.registerFormWindow()


def goToMainWindow(window, userID):
    confirmation = downloadedClass.initialiseDownloadedTable()
    if confirmation:
        window.destroy()
        player.mainWindow(userID)
    else:
        tk.messagebox.showwarning(title="Error", message="Initialising downloaded table failed")


def login(nameEntry, passwordEntry, window):
    inputUsername = (nameEntry.get())
    inputPassword = (passwordEntry.get())
    if inputUsername == "" and inputPassword == "":
        tk.messagebox.showwarning(title="Error", message="Username and Password cannot be empty")
    else:
        if inputUsername == "":
            passwordEntry.delete(0, tk.END)
            tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
        else:
            if inputPassword == "":
                tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
            else:

                count = user.getCountUserByUsername(inputUsername)[0][0]
                if count == 0:
                    passwordEntry.delete(0, tk.END)
                    tk.messagebox.showwarning(title="Error", message="Wrong Username")

                else:
                    cryptedInputPassword = crypt.encrypt(inputPassword)
                    dbPassword = user.getUserByUsername(inputUsername)[0][2]
                    if dbPassword != cryptedInputPassword:
                        passwordEntry.delete(0, tk.END)
                        tk.messagebox.showwarning(title="Error", message="Wrong Password")

                    else:
                        userID = user.getUserByUsername(inputUsername)[0][0]
                        goToMainWindow(window, userID)


def loginFormWindow():
    # Login Window
    loginWindow = tk.Tk()
    loginWindow.top_bar = tk.Frame(loginWindow, bg="Red", cursor="sizing")
    loginWindow.title("Login")
    loginWindow.configure(bg="#5a5b5e")
    loginWindow.resizable(False, False)

    # SCREEN SIZE
    screenWidth = round(loginWindow.winfo_screenwidth() * 0.3)
    screenHeight = round(loginWindow.winfo_screenheight() * 0.3)
    loginWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    # BUTTON SIZE
    imgURL = "assets/bg2.jpg"

    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    bg = tk.Label(
        loginWindow,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)

    buttonWidth = 30

    # FORM

    loginWindow.configure(background="grey")
    nameLabel = tk.Label(loginWindow, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )

    passwordLabel = tk.Label(loginWindow, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    nameEntry = tk.Entry(loginWindow, width=50)

    passwordEntry = tk.Entry(loginWindow, show="\u2022", width=50)

    loginButton = tk.Button(loginWindow, width=int(buttonWidth / 2), text='Login', bg="#5c1a56",
                            fg="silver", font="sans 8 bold",
                            command=lambda: login(nameEntry, passwordEntry, loginWindow))

    # BUTTON
    registerButton = tk.Button(loginWindow, text="Register", width=int(buttonWidth / 2),
                               bg="#5c1a56",
                               fg="silver",
                               font="sans 8 bold",
                               command=lambda: goToRegister(loginWindow))

    # PACKING

    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 2)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 4)
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 2)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 4)
    loginButton.place(x=150, y=screenHeight / 10 * 6)
    registerButton.place(x=150, y=screenHeight / 10 * 8)
    loginWindow.mainloop()
