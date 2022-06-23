import tkinter as tk
from gui import addSong, searchSong, downloadedSongs, adminPage, quizzGame
from functions import canvasManagement
from functions import downloadManagement
from functions import listboxManagement
from functions import windowManagement
from functions import dataManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagement.ListboxManagementClass()
downloadManagement = downloadManagement.DownloadManagementClass
dataManagement = dataManagement.DataManagementClass()
canvasManagement = canvasManagement.CanvasManagementClass()


# SWAP PAGE FUNCTIONS
def changeWindowToAddSong(window, userID, mode):
    window.destroy()
    addSong.addSongWindow(userID, mode)


def changeWindowToQuizzGame(window, userID, mode):
    window.destroy()
    quizzGame.quizzGameWindow(userID, mode)


def changeWindowToSearch(window, userID, mode):
    window.destroy()
    searchSong.searchSongWindow(userID, mode)


def changeWindowToDownloaded(window, userID, mode):
    window.destroy()
    downloadedSongs.downloadedSongsWindow(userID, mode)


def changeWindowToPanel(window, userID, mode):
    window.destroy()
    adminPage.adminPanelWindow(userID, mode)


def mainWindow(userID, mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 1229
    screenHeight = 691
    buttonWidth = 30
    buttonHeight = 30
    listBoxWidth = 55
    listBoxHeight = 10
    canvasWidth = 350
    canvasHeight = 400
    labelWidth = 50

    # WINDOW CONFIGURATION
    if mode == "WHITE":
        bgColor = "#f5faf5"
        widgetColor = "#fffffa"
        textColor = "#000000"
    else:
        bgColor = "#3d3d3d"
        widgetColor = "#9c9c9c"
        textColor = "black"

    window.geometry("1229x691+30+30")
    window.configure(bg=bgColor)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Smooth Song")
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    window.resizable(False, False)

    # CREATION
    # LABEL CREATION
    artistName = tk.StringVar()
    labelArtist = tk.Label(window, textvariable=artistName, relief=tk.RAISED, bg=widgetColor,
                           fg=textColor, width=labelWidth)
    songName = tk.StringVar()
    labelSong = tk.Label(window, textvariable=songName, relief=tk.RAISED, bg=widgetColor,
                         fg=textColor, width=labelWidth)
    genreName = tk.StringVar()
    labelGenre = tk.Label(window, textvariable=genreName, relief=tk.RAISED, bg=widgetColor,
                          fg=textColor, width=labelWidth)
    favoritesListboxString = tk.StringVar()
    favoritesListboxString.set("Favorite Songs")
    favoritesListboxLabel = tk.Label(window, textvariable=favoritesListboxString, relief=tk.RAISED, bg=widgetColor,
                                     fg=textColor, width=47, borderwidth=0, font="sans 8 bold",
                                     highlightthickness=0, )
    playlistListBoxString = tk.StringVar()
    playlistListBoxString.set("Playlist Creation")
    playlistListBoxLabel = tk.Label(window, textvariable=playlistListBoxString, relief=tk.RAISED, bg=widgetColor,
                                    fg=textColor, width=47, borderwidth=0, font="sans 8 bold",
                                    highlightthickness=0, )
    playlistNameLabel = tk.Label(window, text='Playlist Name', width=12, height=1, bg=widgetColor,
                                 fg=textColor, font="sans 8 bold", borderwidth=1,
                                 highlightthickness=0, )
    # ENTRY CREATION
    playlistNameEntry = tk.Entry(window, width=40, borderwidth=1, bg=widgetColor, font="sans 8 bold",
                                 highlightthickness=0, )

    # CANVAS CREATION

    canvas = tk.Canvas(window, width=canvasWidth, height=canvasHeight, borderwidth=0,
                       highlightthickness=0, )
    image_container = canvas.create_image(0, 0, anchor=tk.NW, image="")
    canvasManagement.initialiseCanvas(image_container, canvas)
    # LISTBOX CREATION
    favoritesListbox = tk.Listbox(window, height=listBoxHeight, width=listBoxWidth, selectmode='multiple',
                                  font="sans 8 bold",
                                  borderwidth=1,
                                  highlightthickness=0, )
    scrollbarFavorites = tk.Scrollbar(favoritesListbox)
    playlistListBox = tk.Listbox(window, height=listBoxHeight, width=listBoxWidth, selectmode='multiple',
                                 font="sans 8 bold",
                                 borderwidth=1,
                                 highlightthickness=0, )
    scrollbarPlaylist = tk.Scrollbar(playlistListBox)

    # BUTTON CREATION
    downloadPlaylistButton = tk.Button(window, text="Download", height=buttonHeight, width=buttonWidth * 2.5,
                                       image=pixelVirtual,
                                       bg=widgetColor,
                                       fg=textColor,
                                       compound="c", font="sans 8 bold",
                                       command=lambda: [
                                           downloadManagement.downloadPlaylist(playlistListBox, playlistNameEntry)]
                                       )
    removePlaylistButton = tk.Button(window, text="Remove", height=buttonHeight, width=buttonWidth * 2.5,
                                     image=pixelVirtual,
                                     bg=widgetColor,
                                     fg=textColor,
                                     compound="c", font="sans 8 bold", )

    clearPlaylistButton = tk.Button(window, text="Clear", height=buttonHeight, width=buttonWidth * 2.5,
                                    image=pixelVirtual,
                                    bg=widgetColor,
                                    fg=textColor,
                                    compound="c", font="sans 8 bold",
                                    command=lambda: [
                                        listboxManagement.clearPlaylistListbox(playlistListBox, playlistListBoxLabel,
                                                                               playlistNameLabel, playlistNameEntry,
                                                                               downloadPlaylistButton,
                                                                               removePlaylistButton,
                                                                               clearPlaylistButton)]
                                    )

    removePlaylistButton.configure(command=lambda: [listboxManagement.removeItemsFromPlaylistListbox
                                                    (playlistListBox, playlistListBoxLabel,
                                                     playlistNameLabel, playlistNameEntry,
                                                     downloadPlaylistButton, removePlaylistButton,
                                                     clearPlaylistButton)])

    removeFavoritesButton = tk.Button(window, text="Remove", height=buttonHeight, width=buttonWidth * 2.5,
                                      image=pixelVirtual,
                                      bg=widgetColor,
                                      fg=textColor,
                                      compound="c", font="sans 8 bold",
                                      command=lambda: [
                                          listboxManagement.removeItemsFromFavoritesListbox(favoritesListbox)]
                                      )
    clearFavoritesButton = tk.Button(window, text="Clear", height=buttonHeight, width=buttonWidth * 2.5,
                                     image=pixelVirtual,
                                     bg=widgetColor,
                                     fg=textColor,
                                     compound="c", font="sans 8 bold",
                                     command=lambda: [
                                         listboxManagement.clearFavoritesListbox(favoritesListbox)]
                                     )
    downloadFavoritesButton = tk.Button(window, text="Download", height=buttonHeight, width=buttonWidth * 2.5,
                                        image=pixelVirtual,
                                        bg=widgetColor,
                                        fg=textColor,
                                        compound="c", font="sans 8 bold",
                                        command=lambda: [
                                            downloadManagement.downloadSelectedSongs(favoritesListbox)])
    addPlayListButton = tk.Button(window, text="Add Playlist", height=buttonHeight, width=buttonWidth * 2.5,
                                  image=pixelVirtual,
                                  bg=widgetColor,
                                  fg=textColor,
                                  compound="c", font="sans 8 bold",
                                  command=lambda: [
                                      listboxManagement.addSongToPlaylist(favoritesListbox, playlistListBox,
                                                                          playlistListBoxLabel, playlistNameLabel,
                                                                          playlistNameEntry, downloadPlaylistButton,
                                                                          removePlaylistButton, clearPlaylistButton)]
                                  )
    swapToAdminPageButton = tk.Button(window, text="Admin", height=buttonHeight, width=50, image=pixelVirtual,
                                      bg=widgetColor,
                                      fg=textColor,
                                      compound="c", font="sans 8 bold",
                                      command=lambda: [changeWindowToPanel(window, userID, mode)])
    swapToAddSongFormButton = tk.Button(window, text="Add Song", height=buttonHeight, width=buttonWidth * 2.5,
                                        image=pixelVirtual,
                                        bg=widgetColor,
                                        fg=textColor,
                                        compound="c", font="sans 8 bold",
                                        command=lambda: [changeWindowToAddSong(window, userID, mode)])
    swapToSearchPageButton = tk.Button(window, text="Song Library", height=buttonHeight, width=buttonWidth * 2.5,
                                       image=pixelVirtual,
                                       bg=widgetColor,
                                       fg=textColor,
                                       compound="c", font="sans 8 bold",
                                       command=lambda: [
                                           changeWindowToSearch(window, userID, mode)])
    swapToDownloadedButton = tk.Button(window, text="Downloaded", height=buttonHeight, width=buttonWidth * 2.5,
                                       image=pixelVirtual,
                                       bg=widgetColor,
                                       fg=textColor,
                                       compound="c", font="sans 8 bold",
                                       command=lambda: [
                                           changeWindowToDownloaded(window, userID, mode)])
    swapToQuizzGame = tk.Button(window, text="Quizz Game", height=buttonHeight, width=buttonWidth * 2.5,
                                image=pixelVirtual,
                                bg=widgetColor,
                                fg=textColor,
                                compound="c", font="sans 8 bold",
                                command=lambda: [
                                    changeWindowToQuizzGame(window, userID, mode)])
    donateButton = tk.Button(window, text="Donate", height=buttonHeight, width=50,
                             image=pixelVirtual,
                             bg=widgetColor,
                             fg=textColor,
                             compound="c", font="sans 8 bold",
                             command=lambda: [
                                 windowManagement.openPayPal()])
    exitButton = tk.Button(window, text="Leave", height=buttonHeight, width=50, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    resetCanvasButton = tk.Button(window, text="Reset", height=round(buttonHeight * 0.7), width=buttonWidth * 2.5,
                                  image=pixelVirtual,
                                  bg=widgetColor,
                                  fg=textColor,
                                  compound="c", font="sans 8 bold",
                                  command=lambda: [
                                      canvasManagement.resetCanvas(image_container, canvas, resetCanvasButton,
                                                                   labelSong,
                                                                   labelArtist,
                                                                   labelGenre)])
    loadDetailsButton = tk.Button(window, text="Load Song Details", height=round(buttonHeight * 0.7),
                                  width=buttonWidth * 3.5,
                                  image=pixelVirtual,
                                  bg=widgetColor,
                                  fg=textColor,
                                  compound="c", font="sans 8 bold",
                                  command=lambda: [canvasManagement.loadSongDetails
                                                   (favoritesListbox, image_container, canvas,
                                                    songName, artistName, genreName, labelSong,
                                                    labelArtist,
                                                    labelGenre, window, resetCanvasButton)])

    # CREATION END

    # CONFIGURATION
    # LISTBOX CONFIGURATION
    favoritesListbox.config(yscrollcommand=scrollbarFavorites.set)
    favoritesListbox.configure(justify="center")
    favoritesListbox.configure(bg=widgetColor, fg=textColor)
    scrollbarFavorites.config(command=favoritesListbox.yview)
    listboxManagement.populateFavoritesListbox(favoritesListbox, userID)

    playlistListBox.config(yscrollcommand=scrollbarPlaylist.set)
    playlistListBox.configure(justify="center")
    playlistListBox.configure(bg=widgetColor, fg=textColor)
    scrollbarPlaylist.config(command=playlistListBox.yview)
    # CONFIGURATION END

    # PLACING
    # CANVAS PLACING
    canvas.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=0 + 3 * buttonHeight)

    # LISTBOX PLACING
    favoritesListbox.place(x=screenWidth - 435, y=0 + 3 * buttonHeight)
    favoritesListboxLabel.place(x=screenWidth - 435, y=0 + 3 * buttonHeight - 17)
    if playlistListBox.size() > 0:
        playlistListBox.place(x=screenWidth - 435, y=0 + 13 * buttonHeight)
        playlistListBoxLabel.place(x=screenWidth - 435, y=0 + 13 * buttonHeight - 17)
        playlistNameLabel.place(x=screenWidth - 435, y=0 + 19 * buttonHeight)
        playlistNameEntry.place(x=screenWidth - 350, y=0 + 19 * buttonHeight)
        downloadPlaylistButton.place(x=screenWidth - 1.5 * (buttonWidth * 9.5) + 7.5, y=0 + 20 * buttonHeight + 10)
        removePlaylistButton.place(x=screenWidth - 1.5 * (buttonWidth * 7) + 7.5, y=0 + 20 * buttonHeight + 10)
        clearPlaylistButton.place(x=screenWidth - 1.5 * (buttonWidth * 4.5) + 7.5, y=0 + 20 * buttonHeight + 10)

    # BUTTON PLACING
    # PAGE BUTTONS
    swapToDownloadedButton.place(x=screenWidth - 540, y=5)
    swapToAddSongFormButton.place(x=screenWidth - 340, y=5)
    swapToSearchPageButton.place(x=screenWidth - 440, y=5)
    swapToQuizzGame.place(x=screenWidth - 640, y=5)
    if dataManagement.isUserAdmin(userID)[0][0]:
        swapToAdminPageButton.place(x=screenWidth - 200, y=5)

    # LISTBOX BUTTONS
    downloadFavoritesButton.place(x=screenWidth - 1.5 * (buttonWidth * 11) + 7.5, y=0 + 9 * buttonHeight)
    removeFavoritesButton.place(x=screenWidth - 1.5 * (buttonWidth * 8.5) + 7.5, y=0 + 9 * buttonHeight)
    clearFavoritesButton.place(x=screenWidth - 1.5 * (buttonWidth * 6) + 7.5, y=0 + 9 * buttonHeight)
    addPlayListButton.place(x=screenWidth - 1.5 * (buttonWidth * 3.5) + 7.5, y=0 + 9 * buttonHeight)

    # OTHER BUTTONS
    loadDetailsButton.place(x=screenWidth / 4 - buttonWidth - 15, y=screenHeight - 2.5 * buttonHeight)
    donateButton.place(x=screenWidth - 130, y=5)
    exitButton.place(x=screenWidth - 60, y=5)
    # CREATION END

    window.mainloop()
