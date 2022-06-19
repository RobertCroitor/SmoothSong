import tkinter as tk
import webbrowser

import requests
from PIL import ImageTk, Image
from gui import addSong, searchSong, downloadedSongs, adminPage

from postgres import favoriteTableClass as favoritesClass
from postgres import songTableClass as songClass
from postgres import userTableClass as userClass
from postgres import downloadedTableClass as downloadedClass

from tkinter.messagebox import showinfo
from musicPlayer import downloadSong

user = userClass.Users()
song = songClass.Songs()
downloaded = downloadedClass.Downloaded()
favorite = favoritesClass.Favorites()


def changeWindowToAddSong(window, userID):
    window.destroy()
    addSong.addSongWindow(userID)


def changeWindowToSearch(window, userID):
    window.destroy()
    searchSong.searchSongWindow(userID)


def changeWindowToDownloaded(window, userID):
    window.destroy()
    downloadedSongs.downloadedSongsWindow(userID)


def changeWindowToPanel(window, userID):
    window.destroy()
    adminPage.adminPanelWindow(userID)


def openPayPal():
    url = "https://www.paypal.com/ro/business"
    webbrowser.open(url, new=1)


def exitApp(root):
    root.destroy()


def playlistDownload(playlistListbox, playlistEntry):
    for i in range(playlistListbox.size()):
        playlist = (playlistEntry.get())
        selectedOption = playlistListbox.get(i).split("-")
        title = selectedOption[0].strip()
        author = selectedOption[1].strip()
        rows = downloaded.getSongData(title, author)
        songTitle = rows[0][1]
        songAuthor = rows[0][2]
        songURL = rows[0][5]
        downloadSong.createDir(playlist)
        downloadSong.downloadPlaylist(songTitle, songAuthor, songURL, playlist)


def clearFavoritesFunction(favoritesListbox):
    confirmation = favorite.deleteTable()
    if confirmation:
        confirmation = favorite.createTable()
        if confirmation:
            favoritesListbox.delete(0, tk.END)


def clearPlaylistFunction(playlistListBox):
    playlistListBox.delete(0, tk.END)


def removeItemPLaylistFunction(playlistListBox):
    if len(playlistListBox.curselection()) > 0:
        for i in reversed(playlistListBox.curselection()):
            playlistListBox.delete(i)

    else:
        tk.messagebox.showwarning(title="Error", message="Nothing selected to delete")


def addToPlaylist(favoritesListbox, playlistListBox):
    if len(favoritesListbox.curselection()) > 0:
        for i in favoritesListbox.curselection():
            playlistListBox.insert(tk.END, favoritesListbox.get(i))
    else:
        tk.messagebox.showwarning(title="Error", message="Nothing selected to add")


def getSelectedItemFromListbox(listbox):
    if len(listbox.curselection()) > 0:
        for i in listbox.curselection():
            selectedOption = listbox.get(i)
            selectedOption = selectedOption.split("-")
            title = selectedOption[0].strip()
            author = selectedOption[1].strip()
            rows = downloaded.getSongData(title, author)
            songTitle = rows[0][1]
            songAuthor = rows[0][2]
            songGenre = rows[0][3]
            songImage = rows[0][4]
            songURL = rows[0][5]

            downloaded.insertDownloaded(songTitle, songAuthor, songGenre, songImage, songURL)
            downloadSong.download(songTitle, songAuthor, songURL)
    else:
        tk.messagebox.showwarning(title="Error", message="Nothing selected to download")


def updateCanvas(listbox, imageId, canvas, canvasWidth, canvasHeight, titleName, authorName, genreName, labelSong,
                 labelArtist, labelGenre, root):
    if len(listbox.curselection()) == 1:
        selectedOption = listbox.get(listbox.curselection())
        selectedOption = selectedOption.split("-")
        title = selectedOption[0].strip()
        author = selectedOption[1].strip()
        rows = downloaded.getSongData(title, author)
        songTitle = rows[0][1]
        songAuthor = rows[0][2]
        songGenre = rows[0][3]
        songImage = rows[0][4]
        titleName.set(songTitle)
        authorName.set(songAuthor)
        genreName.set(songGenre)
        response = requests.get(songImage)
        file = open("assets/image.png", "wb")
        file.write(response.content)
        file.close()
        imgURL = "assets/image.png"
        img = (Image.open(imgURL))
        resized_image = img.resize((canvasWidth, canvasHeight), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        canvas.imgref = new_image
        canvas.itemconfig(imageId, image=new_image)
        screenWidth = round(root.winfo_screenwidth() * 0.9)
        buttonHeight = 30
        labelSong.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=canvasHeight + (4 * buttonHeight))
        labelArtist.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=canvasHeight + (5 * buttonHeight))
        labelGenre.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=canvasHeight + (6 * buttonHeight))
        canvas.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=0 + 3 * buttonHeight)
    else:
        tk.messagebox.showwarning(title="Error", message="You need to select exactly one item to load details!")


def mainWindow(userID):
    # Functions

    # ROOT CONFIGURE
    root = tk.Tk()

    root.top_bar = tk.Frame(root, bg="Red", cursor="sizing")
    root.title("Music App")
    root.configure(bg="#5a5b5e")
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    root.resizable(False, False)

    # SCREEN SIZE
    screenWidth = round(root.winfo_screenwidth() * 0.9)
    screenHeight = round(root.winfo_screenheight() * 0.9)
    root.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        root,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)
    # BUTTON SIZE
    buttonWidth = 30
    buttonHeight = 30

    # LIST SIZE
    listBoxWidth = 55
    listBoxHeight = 10

    # CANVAS SIZE
    canvasWidth = 350
    canvasHeight = 400

    # LABEL SIZE
    labelWidth = 50

    artistName = tk.StringVar()
    labelArtist = tk.Label(root, textvariable=artistName, relief=tk.RAISED, bg="#5c1a56",
                           fg="silver", width=labelWidth)
    artistName.set("Song title placeholder")

    songName = tk.StringVar()
    labelSong = tk.Label(root, textvariable=songName, relief=tk.RAISED, bg="#5c1a56",
                         fg="silver", width=labelWidth)
    songName.set("Author name placeholder")
    genreName = tk.StringVar()
    labelGenre = tk.Label(root, textvariable=genreName, relief=tk.RAISED, bg="#5c1a56",
                          fg="silver", width=labelWidth)
    genreName.set("Genre name placeholder")

    # IMAGE

    imgURL = "assets/placeholder.png"
    img = (Image.open(imgURL))
    resized_image = img.resize((canvasWidth, canvasHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight, borderwidth=0,
                       highlightthickness=0, )
    image_container = canvas.create_image(0, 0, anchor=tk.NW, image=new_image)
    # LABEL

    # LIST BOX
    favoritesListboxString = tk.StringVar()
    favoritesListboxString.set("Favorite Songs")
    favoritesListboxLabel = tk.Label(root, textvariable=favoritesListboxString, relief=tk.RAISED, bg="#5c1a56",
                                     fg="silver", width=47, borderwidth=0,
                                     highlightthickness=0, )
    favoritesListbox = tk.Listbox(root, height=listBoxHeight, width=listBoxWidth, selectmode='multiple', borderwidth=0,
                                  highlightthickness=0, )
    scrollbar = tk.Scrollbar(favoritesListbox)
    favoritesListbox.config(yscrollcommand=scrollbar.set)
    favoritesListbox.configure(justify="center")
    favoritesListbox.configure(background="#260033", foreground="white")
    scrollbar.config(command=favoritesListbox.yview)
    songRow = favorite.getSongsByUserID(userID)
    for row in songRow:
        title = row[2]
        singer = row[3]
        favoritesListbox.insert(tk.END, title + "  -  " + singer)

    playlistListBoxString = tk.StringVar()
    playlistListBoxString.set("Favorite Songs")
    playlistListBoxLabel = tk.Label(root, textvariable=playlistListBoxString, relief=tk.RAISED, bg="#5c1a56",
                                    fg="silver", width=47, borderwidth=0,
                                    highlightthickness=0, )
    playlistListBox = tk.Listbox(root, height=listBoxHeight, width=listBoxWidth, selectmode='multiple', borderwidth=0,
                                 highlightthickness=0, )
    scrollbar = tk.Scrollbar(playlistListBox)
    playlistListBox.config(yscrollcommand=scrollbar.set)
    playlistListBox.configure(justify="center")
    playlistListBox.configure(background="#260033", foreground="white")
    scrollbar.config(command=playlistListBox.yview)
    playlistNameLabel = tk.Label(root, text='Playlist Name', width=12, bg="#5c1a56",
                                 fg="silver", font="sans 8 bold", borderwidth=1,
                                 highlightthickness=0, )
    playlisteNameEntry = tk.Entry(root, width=40, borderwidth=0,
                                  highlightthickness=0, )
    downloadPlaylist = tk.Button(root, text="Download", height=buttonHeight, width=buttonWidth * 2.5,
                                 image=pixelVirtual,
                                 bg="#5c1a56",
                                 fg="silver",
                                 compound="c", font="sans 8 bold",
                                 command=lambda: [
                                     playlistDownload(playlistListBox, playlisteNameEntry)]
                                 )
    removeSongPlaylist = tk.Button(root, text="Remove", height=buttonHeight, width=buttonWidth * 2.5,
                                   image=pixelVirtual,
                                   bg="#5c1a56",
                                   fg="silver",
                                   compound="c", font="sans 8 bold",
                                   command=lambda: [
                                       removeItemPLaylistFunction(playlistListBox)]
                                   )

    clearPlaylist = tk.Button(root, text="Clear", height=buttonHeight, width=buttonWidth * 2.5,
                              image=pixelVirtual,
                              bg="#5c1a56",
                              fg="silver",
                              compound="c", font="sans 8 bold",
                              command=lambda: [
                                  clearPlaylistFunction(playlistListBox)]
                              )
    # BUTTON
    adminButton = tk.Button(root, text="Admin", height=buttonHeight, width=50, image=pixelVirtual,
                            bg="#5c1a56",
                            fg="silver",
                            compound="c", font="sans 8 bold", command=lambda: [changeWindowToPanel(root, userID)])

    detailsButton = tk.Button(root, text="Load Details", height=buttonHeight, width=buttonWidth * 2.5,
                              image=pixelVirtual,
                              bg="#5c1a56",
                              fg="silver",
                              compound="c", font="sans 8 bold",
                              command=lambda: [updateCanvas(favoritesListbox, image_container, canvas, canvasWidth,
                                                            canvasHeight,
                                                            songName, artistName, genreName, labelSong, labelArtist,
                                                            labelGenre, root)])

    addButton = tk.Button(root, text="Add Song", height=buttonHeight, width=buttonWidth * 2.5, image=pixelVirtual,
                          bg="#5c1a56",
                          fg="silver",
                          compound="c", font="sans 8 bold",
                          command=lambda: [changeWindowToAddSong(root, userID)])
    searchButton = tk.Button(root, text="Search Panel", height=buttonHeight, width=buttonWidth * 2.5,
                             image=pixelVirtual,
                             bg="#5c1a56",
                             fg="silver",
                             compound="c", font="sans 8 bold",
                             command=lambda: [
                                 changeWindowToSearch(root, userID)])
    downloadedButton = tk.Button(root, text="Downloaded", height=buttonHeight, width=buttonWidth * 2.5,
                                 image=pixelVirtual,
                                 bg="#5c1a56",
                                 fg="silver",
                                 compound="c", font="sans 8 bold",
                                 command=lambda: [
                                     changeWindowToDownloaded(root, userID)])
    donateButton = tk.Button(root, text="Donate", height=buttonHeight, width=50,
                             image=pixelVirtual,
                             bg="#5c1a56",
                             fg="silver",
                             compound="c", font="sans 8 bold",
                             command=openPayPal)

    downloadButton = tk.Button(root, text="Download", height=buttonHeight, width=buttonWidth * 2.5, image=pixelVirtual,
                               bg="#5c1a56",
                               fg="silver",
                               compound="c", font="sans 8 bold",
                               command=lambda: [
                                   getSelectedItemFromListbox(favoritesListbox)])

    exitButton = tk.Button(root, text="Leave", height=buttonHeight, width=50, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [exitApp(root)])

    removeButton = tk.Button(root, text="Remove", height=buttonHeight, width=buttonWidth * 2.5, image=pixelVirtual,
                             bg="#5c1a56",
                             fg="silver",
                             compound="c", font="sans 8 bold",
                             )
    clearButton = tk.Button(root, text="Clear", height=buttonHeight, width=buttonWidth * 2.5, image=pixelVirtual,
                            bg="#5c1a56",
                            fg="silver",
                            compound="c", font="sans 8 bold",
                            command=lambda: [
                                clearFavoritesFunction(favoritesListbox)]
                            )
    addPlayListButton = tk.Button(root, text="Add Playlist", height=buttonHeight, width=buttonWidth * 2.5,
                                  image=pixelVirtual,
                                  bg="#5c1a56",
                                  fg="silver",
                                  compound="c", font="sans 8 bold",
                                  command=lambda: [
                                      addToPlaylist(favoritesListbox, playlistListBox)]
                                  )
    # PACKING

    favoritesListbox.place(x=screenWidth - 435, y=0 + 3 * buttonHeight)
    favoritesListboxLabel.place(x=screenWidth - 435, y=0 + 3 * buttonHeight - 17)

    if playlistListBox.size() >= 0:
        playlistListBox.place(x=screenWidth - 435, y=0 + 13 * buttonHeight)
        playlistListBoxLabel.place(x=screenWidth - 435, y=0 + 13 * buttonHeight - 17)
        playlistNameLabel.place(x=screenWidth - 435, y=0 + 19 * buttonHeight)
        playlisteNameEntry.place(x=screenWidth - 350, y=0 + 19 * buttonHeight)
        downloadPlaylist.place(x=screenWidth - 1.5 * (buttonWidth * 9.5) + 7.5, y=0 + 20 * buttonHeight + 10)
        removeSongPlaylist.place(x=screenWidth - 1.5 * (buttonWidth * 7) + 7.5, y=0 + 20 * buttonHeight + 10)
        clearPlaylist.place(x=screenWidth - 1.5 * (buttonWidth * 4.5) + 7.5, y=0 + 20 * buttonHeight + 10)

    # INTERACTIVE BUTTONS
    isUserAdmin = user.getAdminByID(userID)
    if isUserAdmin[0][0]:
        adminButton.place(x=screenWidth - 200, y=5)
    exitButton.place(x=screenWidth - 60, y=5)
    donateButton.place(x=screenWidth - 130, y=5)

    # PAGE BUTTONS
    downloadedButton.place(x=screenWidth - 540, y=5)
    addButton.place(x=screenWidth - 340, y=5)
    searchButton.place(x=screenWidth - 440, y=5)

    # FUNCTIONAL BUTTONS
    detailsButton.place(x=screenWidth / 4 - buttonWidth, y=screenHeight - 1.5 * buttonHeight)
    downloadButton.place(x=screenWidth - 1.5 * (buttonWidth * 11) + 7.5, y=0 + 9 * buttonHeight)
    removeButton.place(x=screenWidth - 1.5 * (buttonWidth * 8.5) + 7.5, y=0 + 9 * buttonHeight)
    clearButton.place(x=screenWidth - 1.5 * (buttonWidth * 6) + 7.5, y=0 + 9 * buttonHeight)
    addPlayListButton.place(x=screenWidth - 1.5 * (buttonWidth * 3.5) + 7.5, y=0 + 9 * buttonHeight)
    root.mainloop()
