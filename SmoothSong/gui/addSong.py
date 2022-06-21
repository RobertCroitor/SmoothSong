from gui import player
import tkinter as tk
from functions import dataManagement
from functions import windowManagement

# CLASS INITIALISATION
dataManagement = dataManagement.DataManagementClass()
windowManagement = windowManagement.WindowManagementClass()


# BACK FUNCTION
def goBackToMainWindow(window, userID, mode):
    window.destroy()
    player.mainWindow(userID, mode)


def addSongWindow(userID, mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 683
    screenHeight = 400
    buttonWidth = 30

    # WINDOW CONFIGURATION
    if mode == "WHITE":
        bgColor = "#f5faf5"
        widgetColor = "#c0c2c0"
        textColor = "#000000"
    else:
        bgColor = "#3d3d3d"
        widgetColor = "#9c9c9c"
        textColor = "black"
    window.geometry("683x400+30+30")
    window.configure(bg=bgColor)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Add Song Form")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    # CREATION
    # LABEL CREATION
    songLabel = tk.Label(window, text='Title', width=10, font="sans 8 bold", bg=widgetColor,
                         fg=textColor)
    authorLabel = tk.Label(window, text='Singer', width=10, font="sans 8 bold", bg=widgetColor,
                           fg=textColor)
    genreLabel = tk.Label(window, text='Genre', width=10, font="sans 8 bold", bg=widgetColor,
                          fg=textColor)
    songImageLabel = tk.Label(window, text='Image URL', font="sans 8 bold", width=10, bg=widgetColor,
                              fg=textColor)
    songFileLabel = tk.Label(window, text='Song URL', font="sans 8 bold", width=10, bg=widgetColor,
                             fg=textColor)

    # ENTRY CREATION
    songEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=70)
    authorEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=70)
    genreEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=70)
    songImageEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=70)
    songFileEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=70)

    # BUTTON CREATION
    submitFormButton = tk.Button(window, width=int(buttonWidth / 2), text='Submit', bg=widgetColor,
                                 fg=textColor, font="sans 8 bold",
                                 command=lambda: dataManagement.insertSongIntoSongTable(songEntry, authorEntry,
                                                                                        genreEntry,
                                                                                        songImageEntry, songFileEntry))
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg=widgetColor,
                           fg=textColor,
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID, mode))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LABEL PLACING
    songLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 2)
    authorLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 3)
    genreLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 4)
    songImageLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 5)
    songFileLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 6)

    # ENTRY PLACING
    songEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 2)
    authorEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 3)
    genreEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 4)
    songImageEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 5)
    songFileEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 6)

    # BUTTON PLACING
    submitFormButton.place(x=281, y=screenHeight / 10 * 7)
    backButton.place(x=281, y=screenHeight / 10 * 8.5)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
