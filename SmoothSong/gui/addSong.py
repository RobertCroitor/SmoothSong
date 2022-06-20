from gui import player
import tkinter as tk
from functions import dataManagement
from functions import windowManagement

# CLASS INITIALISATION
dataManagement = dataManagement.DataManagementClass()
windowManagement = windowManagement.WindowManagementClass()


# BACK FUNCTION
def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def addSongWindow(userID):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 683
    screenHeight = 400
    buttonWidth = 30

    # WINDOW CONFIGURATION
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Add Song Form")
    window.resizable(False, False)
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(bg="silver")
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    # CREATION
    # LABEL CREATION
    songLabel = tk.Label(window, text='Title', width=10, bg="#5c1a56",
                         fg="silver")
    authorLabel = tk.Label(window, text='Singer', width=10, bg="#5c1a56",
                           fg="silver")
    genreLabel = tk.Label(window, text='Genre', width=10, bg="#5c1a56",
                          fg="silver")
    songImageLabel = tk.Label(window, text='Image URL', width=10, bg="#5c1a56",
                              fg="silver")
    songFileLabel = tk.Label(window, text='Song URL', width=10, bg="#5c1a56",
                             fg="silver")

    # ENTRY CREATION
    songEntry = tk.Entry(window, width=70)
    authorEntry = tk.Entry(window, width=70)
    genreEntry = tk.Entry(window, width=70)
    songImageEntry = tk.Entry(window, width=70)
    songFileEntry = tk.Entry(window, width=70)

    # BUTTON CREATION
    submitFormButton = tk.Button(window, width=int(buttonWidth / 2), text='Submit', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: dataManagement.insertSongIntoSongTable(songEntry, authorEntry,
                                                                                        genreEntry,
                                                                                        songImageEntry, songFileEntry))
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
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
