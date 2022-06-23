import tkinter as tk
from gui import player
from functions import listboxManagement
from functions import windowManagement
from musicPlayer import startMusic as openFolder

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagement.ListboxManagementClass()


# BACK FUNCTION
def goBackToMainWindow(window, userID, mode):
    window.destroy()
    player.mainWindow(userID, mode)


def downloadedSongsWindow(userID, mode):
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
    if mode == "WHITE":
        bgColor = "#f5faf5"
        widgetColor = "#fffffa"
        textColor = "#000000"
    else:
        bgColor = "#3d3d3d"
        widgetColor = "#9c9c9c"
        textColor = "black"
    window.configure(bg=bgColor)
    window.geometry("683x691+30+30")
    window.resizable(False, False)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Downloaded Songs")
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LISTBOX CREATION
    listbox = tk.Listbox(
        window,
        height=listBoxHeight,
        width=listBoxWidth, font="sans 8 bold", borderwidth=1,
        highlightthickness=0,
        selectmode='single')
    scrollbar = tk.Scrollbar(listbox)

    # LISTBOX CONFIGURATION
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.configure(justify="center")
    listbox.configure(bg=widgetColor, fg=textColor)
    listboxManagement.populateDownloadedListbox(listbox)

    # BUTTON CREATION
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg=widgetColor,
                           fg=textColor,
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID, mode))
    openSongButton = tk.Button(window, text="Open Song", width=int(buttonWidth / 2),
                               bg=widgetColor,
                               fg=textColor,
                               font="sans 8 bold",
                               command=lambda: listboxManagement.openSelectedSong(listbox))
    openFolderButton = tk.Button(window, text="Open Folder", width=int(buttonWidth / 2),
                                 bg=widgetColor,
                                 fg=textColor,
                                 font="sans 8 bold",
                                 command=lambda: openFolder.startFolder())
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LISTBOX PLACING
    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (3 * buttonHeight))

    # BUTTON PLACING
    backButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 2 * buttonHeight)
    openSongButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 4.5 * buttonHeight)
    openFolderButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 3 * buttonHeight)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
