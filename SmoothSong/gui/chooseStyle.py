import tkinter as tk
from gui import login

from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()


# SWAP PAGE FUNCTIONS
def startInDarkMode(window, mode):
    window.destroy()
    login.loginFormWindow(mode)


def startInWhiteMode(window, mode):
    window.destroy()
    login.loginFormWindow(mode)


def styleWindow():
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 400
    screenHeight = 200

    # WINDOW CONFIGURATION
    bgColor = "#3d3d3d"
    widgetColor = "#9c9c9c"
    textColor = "black"

    window.geometry("400x200+30+30")
    window.configure(bg=bgColor)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Smooth Song")
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    window.resizable(False, False)

    # CREATION
    # LABEL CREATION
    styleLabel = tk.Label(window, text='Choose your color style', width=40, height=1, bg=widgetColor,
                          fg=textColor, font="sans 8 bold", borderwidth=1,
                          highlightthickness=0, )

    # BUTTON CREATION

    darkModeButton = tk.Button(window, text="Dark Mode", height=30, width=130,
                               image=pixelVirtual,
                               bg=widgetColor,
                               fg=textColor,
                               compound="c", font="sans 8 bold",
                               command=lambda: [startInWhiteMode(window, "DARK")]
                               )
    whiteModeButton = tk.Button(window, text="White Mode", height=30, width=130,
                                image=pixelVirtual,
                                bg=widgetColor,
                                fg=textColor,
                                compound="c", font="sans 8 bold",
                                command=lambda: [startInWhiteMode(window, "WHITE")]
                                )
    exitButton = tk.Button(window, text="Leave", height=20, width=30, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])

    # CREATION END
    # LABEL CREATION
    styleLabel.place(x=screenWidth / 2 - 138, y=screenHeight / 2 - 40)

    # BUTTON CREATION
    darkModeButton.place(x=screenWidth / 2 - 150, y=screenHeight / 2)
    whiteModeButton.place(x=screenWidth / 2 + 20, y=screenHeight / 2)
    exitButton.place(x=screenWidth - 40, y=3)
    # CREATION END

    window.mainloop()
