import tkinter as tk
from gui import login
from functions import authentificationManager
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
authentificationManager = authentificationManager.AuthentificationManagerClass()


# SWAP PAGE FUNCTIONS
def goToLogin(window, mode):
    window.destroy()
    login.loginFormWindow(mode)


# REGISTER FUNCTION
def register(nameEntry, passwordEntry, rePasswordEntry, window, mode):
    confirmation = authentificationManager.register(nameEntry, passwordEntry, rePasswordEntry)
    if confirmation:
        goToLogin(window, mode)


def registerFormWindow(mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 410
    screenHeight = 384
    buttonWidth = 30

    # WINDOW CONFIGURATION
    if mode == "WHITE":
        bgColor = "#f5faf5"
        widgetColor = "#fffffa"
        textColor = "#000000"
    else:
        bgColor = "#3d3d3d"
        widgetColor = "#9c9c9c"
        textColor = "black"
    window.geometry("410x384+30+30")
    window.configure(bg=bgColor)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Register")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    # CREATION
    # LABEL CREATION
    nameLabel = tk.Label(window, text='Name', width=10, bg=widgetColor,
                         fg=textColor, font="sans 8 bold", )

    passwordLabel = tk.Label(window, text='Password', width=10, bg=widgetColor,
                             fg=textColor, font="sans 8 bold", )

    rePasswordLabel = tk.Label(window, text='Re-Password', width=10,
                               bg=widgetColor,
                               fg=textColor, font="sans 8 bold", )

    # ENTRY CREATION
    nameEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=50)
    passwordEntry = tk.Entry(window, bg=widgetColor, fg=textColor, show="\u2022", width=50)
    rePasswordEntry = tk.Entry(window, bg=widgetColor, fg=textColor, show="\u2022", width=50)

    # BUTTON CREATION
    registerButton = tk.Button(window, width=int(buttonWidth / 2),
                               text='Register', bg=widgetColor,
                               fg=textColor, font="sans 8 bold",
                               command=lambda: register(nameEntry, passwordEntry,
                                                        rePasswordEntry,
                                                        window, mode))
    loginButton = tk.Button(window, text="Login", width=int(buttonWidth / 2),
                            bg=widgetColor,
                            fg=textColor,
                            font="sans 8 bold",
                            command=lambda: goToLogin(window, mode))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
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
