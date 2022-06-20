import tkinter as tk
from gui import login
from functions import authentificationManager
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
authentificationManager = authentificationManager.AuthentificationManagerClass()


# SWAP PAGE FUNCTIONS
def goToLogin(window):
    window.destroy()
    login.loginFormWindow()


# REGISTER FUNCTION
def register(nameEntry, passwordEntry, rePasswordEntry, window):
    confirmation = authentificationManager.register(nameEntry, passwordEntry, rePasswordEntry)
    if confirmation:
        goToLogin(window)


def registerFormWindow():
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 410
    screenHeight = 384
    buttonWidth = 30
    buttonHeight = 30

    # WINDOW CONFIGURATION
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(bg="silver")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Register")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    # CREATION
    # LABEL CREATION
    nameLabel = tk.Label(window, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )

    passwordLabel = tk.Label(window, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    rePasswordLabel = tk.Label(window, text='Re-Password', width=10,
                               bg="#5c1a56",
                               fg="silver", font="sans 8 bold", )

    # ENTRY CREATION
    nameEntry = tk.Entry(window, width=50)
    passwordEntry = tk.Entry(window, show="\u2022", width=50)
    rePasswordEntry = tk.Entry(window, show="\u2022", width=50)

    # BUTTON CREATION
    registerButton = tk.Button(window, width=int(buttonWidth / 2),
                               text='Register', bg="#5c1a56",
                               fg="silver", font="sans 8 bold",
                               command=lambda: register(nameEntry, passwordEntry,
                                                        rePasswordEntry,
                                                        window))
    loginButton = tk.Button(window, text="Login", width=int(buttonWidth / 2),
                            bg="#5c1a56",
                            fg="silver",
                            font="sans 8 bold",
                            command=lambda: goToLogin(window))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LABEL PLACING
    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 1.5)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 3.5)
    rePasswordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 5.5)

    # ENTRY PLACING
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 1.5)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 3.5)
    rePasswordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 5.5)

    # BUTTON PLACING
    registerButton.place(x=150, y=screenHeight / 10 * 7)
    loginButton.place(x=150, y=screenHeight / 10 * 8.5)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
