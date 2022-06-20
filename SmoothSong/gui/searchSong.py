import tkinter as tk
from gui import player
from functions import listboxManagement as listboxManagementFile
from functions import downloadManagement
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagementFile.ListboxManagementClass()
downloadManagement = downloadManagement.DownloadManagementClass()


# SWAP PAGE FUNCTIONS
def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def searchSongWindow(userID):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 683
    screenHeight = 691
    buttonWidth = 30
    buttonHeight = 30
    listBoxWidth = 80
    listBoxHeight = 30

    # WINDOW CONFIGURATION
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(bg="silver")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Song Collection")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LISTBOX CREATION
    listbox = tk.Listbox(
        window,
        height=listBoxHeight,
        width=listBoxWidth,
        selectmode='single')
    listboxManagement.populateSearchSongsListbox(listbox)
    scrollbar = tk.Scrollbar(listbox)

    # SEARCH BAR CREATION
    searchFrame = tk.Frame(window, bg='red')
    searchLabel = tk.Label(searchFrame, text='Search Song', width=10, bg="#5c1a56",
                           fg="silver")
    searchBarEntry = tk.Entry(searchFrame, width=68)

    # BUTTON CREATION
    searchByAuthorButton = tk.Button(window, width=int(buttonWidth / 2), text='Search Author', bg="#5c1a56",
                                     fg="silver", command=lambda: [
            listboxManagement.searchSongsByAuthor(listbox, searchBarEntry)])

    searchByTitleButton = tk.Button(window, width=int(buttonWidth / 2), text='Search Song', bg="#5c1a56",
                                    fg="silver", command=lambda: [
            listboxManagement.searchSongsByTitle(listbox, searchBarEntry)])
    searchByGenreButton = tk.Button(window, width=int(buttonWidth / 2), text='Search Genre', bg="#5c1a56",
                                    fg="silver", command=lambda: [
            listboxManagement.searchSongsByGenre(listbox, searchBarEntry)])
    resetListboxButton = tk.Button(window, width=int(buttonWidth / 2), text='Reset', bg="#5c1a56",
                                   fg="silver", command=lambda: [
            listboxManagement.resetSongCollectionListbox(listbox, searchBarEntry)])
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID))
    saveToFavoritesButton = tk.Button(window, text="Add to Favorite", width=int(buttonWidth / 2),
                                      bg="#5c1a56",
                                      fg="silver",
                                      font="sans 8 bold",
                                      command=lambda: listboxManagement.saveToFavorites(listbox, userID))
    downloadSongButton = tk.Button(window, text="Download Song", width=int(buttonWidth / 2),
                                   bg="#5c1a56",
                                   fg="silver",
                                   font="sans 8 bold",
                                   command=lambda: downloadManagement.downloadSelectedSongs(listbox))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # CONFIGURATION
    # LISTBOX CONFIGURATION
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.configure(justify="center")

    # SEARCH BAR CONFIGURATION
    searchBarEntry.focus_set()
    # CONFIGURATION END

    # PLACING
    # SEARCH BAR PLACING
    searchLabel.pack(side=tk.LEFT)
    searchBarEntry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    searchFrame.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=10)

    # LISTBOX PLACING
    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (4 * buttonHeight))

    # BUTTON PLACING
    backButton.place(x=screenWidth / 2 - (buttonWidth * 2) + 15, y=screenHeight - 1 * buttonHeight)
    saveToFavoritesButton.place(x=screenWidth / 2 - (buttonWidth * 4), y=screenHeight - 2.5 * buttonHeight)
    downloadSongButton.place(x=screenWidth / 2 + (buttonWidth * 1), y=screenHeight - 2.5 * buttonHeight)
    searchByAuthorButton.place(x=screenWidth / 2 + listBoxWidth / 2 * 6 - buttonWidth * 3.8, y=1.5 * buttonHeight)
    searchByTitleButton.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=1.5 * buttonHeight)
    searchByGenreButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=1.5 * buttonHeight)
    resetListboxButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=2.5 * buttonHeight + 5)
    exitButton.place(x=screenWidth - 50, y=2)
    # CREATION END

    window.mainloop()
