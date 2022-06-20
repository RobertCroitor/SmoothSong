import tkinter as tk
from gui import player
from functions import listboxManagement
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagement.ListboxManagementClass()


# BACK FUNCTION
def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def downloadedSongsWindow(userID):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 683
    screenHeight = 691
    listBoxWidth = 80
    listBoxHeight = 30
    buttonWidth = 30
    buttonHeight = 30

    # WINDOW CONFIGURATION
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.resizable(False, False)
    window.configure(bg="silver")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Downloaded Songs")
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LISTBOX CREATION
    listbox = tk.Listbox(
        window,
        height=listBoxHeight,
        width=listBoxWidth,
        selectmode='single')
    scrollbar = tk.Scrollbar(listbox)

    # LISTBOX CONFIGURATION
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.configure(justify="center")
    listboxManagement.populateDownloadedListbox(listbox)

    # BUTTON CREATION
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID))
    openSongButton = tk.Button(window, text="Open", width=int(buttonWidth / 2),
                               bg="#5c1a56",
                               fg="silver",
                               font="sans 8 bold",
                               command=lambda: listboxManagement.openSelectedSong(listbox))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LISTBOX PLACING
    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (4 * buttonHeight))

    # BUTTON PLACING
    backButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 1 * buttonHeight)
    openSongButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 2.5 * buttonHeight)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
