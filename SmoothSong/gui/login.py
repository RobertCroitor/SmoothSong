import tkinter as tk
from gui import player, register
from functions import authentificationManager
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
authentificationManager = authentificationManager.AuthentificationManagerClass()


# SWAP PAGE FUNCTIONS
def goToRegister(window):
    window.destroy()
    register.registerFormWindow()


def goToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


# LOGIN FUNCTION
def login(nameEntry, passwordEntry, window):
    userID = authentificationManager.login(nameEntry, passwordEntry)
    if userID != -1:
        goToMainWindow(window, userID)


def loginFormWindow():
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 410
    screenHeight = 230
    buttonWidth = 30

    # WINDOW CONFIGURATION
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(bg="silver")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Login")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LABEL CREATION
    nameLabel = tk.Label(window, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )
    passwordLabel = tk.Label(window, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    # ENTRY CREATION
    nameEntry = tk.Entry(window, width=50)
    passwordEntry = tk.Entry(window, show="\u2022", width=50)

    # BUTTON CREATION
    loginButton = tk.Button(window, width=int(buttonWidth / 2), text='Login', bg="#5c1a56",
                            fg="silver", font="sans 8 bold",
                            command=lambda: login(nameEntry, passwordEntry, window))
    registerButton = tk.Button(window, text="Register", width=int(buttonWidth / 2),
                               bg="#5c1a56",
                               fg="silver",
                               font="sans 8 bold",
                               command=lambda: goToRegister(window))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LABEL PLACING
    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 2)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 4)

    # ENTRY PLACING
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 2)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 4)

    # BUTTON PLACING
    loginButton.place(x=150, y=screenHeight / 10 * 6)
    registerButton.place(x=150, y=screenHeight / 10 * 8)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
