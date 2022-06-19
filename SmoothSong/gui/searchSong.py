import tkinter as tk
from PIL import ImageTk, Image

from postgres import songTableClass as songClass
from postgres import downloadedTableClass as downloadedClass

from postgres import favoriteTableClass as favoritesClass
from gui import player
import random
from tkinter.messagebox import showinfo
from musicPlayer import downloadSong

song = songClass.Songs()
favorite = favoritesClass.Favorites()
downloaded = downloadedClass.Downloaded()


def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def saveToFavorites(listbox, userID):
    selectedOption = listbox.get(listbox.curselection())
    selectedOption = selectedOption.split("-")
    title = selectedOption[0].strip()
    rows = song.getSongsByTitle(title)

    title = rows[0][1]
    count = favorite.getSongsCountByTitle(title, userID)[0][0]
    if count > 0:
        tk.messagebox.showwarning(title="Error", message="Song is already added to favorites")
    else:
        singer = rows[0][2]
        genre = rows[0][3]
        imgURL = rows[0][4]
        songURL = rows[0][5]
        confirmation = favorite.insertSong(userID, title, singer, genre, imgURL, songURL)
        if confirmation:
            tk.messagebox.showwarning(title="Error", message="Song added to favorites successfully")
        else:
            tk.messagebox.showwarning(title="Error", message="Adding the song to favorites failed")


def resetListbox(listbox):
    listbox.delete(0, tk.END)
    songRow = song.getAllSongs()
    random.shuffle(songRow)
    for row in songRow:
        title = row[1]
        singer = row[2]
        listbox.insert(tk.END, title + "  -  " + singer)


def searchByAuthor(listbox, titleEntry):
    count = 0
    title = (titleEntry.get())
    rows = song.getAllSongs()
    listbox.delete(0, tk.END)
    for row in rows:
        dbAuthor = row[2]

        if title.upper() in dbAuthor.upper():
            dbTitle = row[1]
            listbox.insert(tk.END, dbTitle + "  -  " + dbAuthor)
            count += 1
    if count != 0:
        if count == 1:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " match!")
        else:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")
    else:
        resetListbox(listbox)
        tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")


def searchByGenre(listbox, titleEntry):
    count = 0
    title = (titleEntry.get())
    rows = song.getAllSongs()
    listbox.delete(0, tk.END)
    for row in rows:
        dbGenre = row[3]
        print(dbGenre)
        if title.upper() in dbGenre.upper():
            dbTitle = row[1]
            dbAuthor = row[2]
            listbox.insert(tk.END, dbTitle + "  -  " + dbAuthor)
            count += 1
    if count != 0:
        if count == 1:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " match!")
        else:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")
    else:
        resetListbox(listbox)
        tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")


def searchByTitle(listbox, titleEntry):
    count = 0
    title = (titleEntry.get())
    rows = song.getAllSongs()
    listbox.delete(0, tk.END)
    for row in rows:
        dbTitle = row[1]

        if title.upper() in dbTitle.upper():
            dbAuthor = row[2]
            listbox.insert(tk.END, dbTitle + "  -  " + dbAuthor)
            count += 1
    if count != 0:
        if count == 1:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " match!")
        else:
            tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")
    else:
        resetListbox(listbox)
        tk.messagebox.showwarning(title="Success", message="Found " + str(count) + " matches!")


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


def searchSongWindow(userID):
    # Second Window
    searchWindow = tk.Tk()
    searchWindow.top_bar = tk.Frame(searchWindow, bg="Red", cursor="sizing")
    searchWindow.title("Search Song")
    searchWindow.configure(bg="#5a5b5e")

    searchWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(searchWindow.winfo_screenwidth() * 0.5)
    screenHeight = round(searchWindow.winfo_screenheight() * 0.9)
    searchWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        searchWindow,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)
    # BUTTON SIZE
    buttonWidth = 30
    buttonHeight = 30

    # LIST SIZE
    listBoxWidth = 80
    listBoxHeight = 30

    listbox = tk.Listbox(
        searchWindow,
        height=listBoxHeight,
        width=listBoxWidth,
        selectmode='single')

    songs = songClass.Songs()
    songRow = songs.getAllSongs()
    random.shuffle(songRow)
    for row in songRow:
        title = row[1]
        singer = row[2]
        listbox.insert(tk.END, title + "  -  " + singer)

    scrollbar = tk.Scrollbar(listbox)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.configure(justify="center")

    # SEARCH BAR
    searchFrame = tk.Frame(searchWindow, bg='red')
    searchLabel = tk.Label(searchFrame, text='Search Song', width=10, bg="#5c1a56",
                           fg="silver")
    modify = tk.Entry(searchFrame, width=68)

    modify.focus_set()

    searchAuthor = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Search Author', bg="#5c1a56",
                             fg="silver", command=lambda: [
            searchByAuthor(listbox, modify)])

    searchSong = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Search Song', bg="#5c1a56",
                           fg="silver", command=lambda: [
            searchByTitle(listbox, modify)])
    searchGenre = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Search Genre', bg="#5c1a56",
                            fg="silver", command=lambda: [
            searchByGenre(listbox, modify)])
    resetButton = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Reset', bg="#5c1a56",
                            fg="silver", command=lambda: [
            resetListbox(listbox)])
    # BUTTON
    buttonBack = tk.Button(searchWindow, text="Music App", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(searchWindow, userID))
    saveFavorite = tk.Button(searchWindow, text="Add to Favorite", width=int(buttonWidth / 2),
                             bg="#5c1a56",
                             fg="silver",
                             font="sans 8 bold",
                             command=lambda: saveToFavorites(listbox, userID))
    download = tk.Button(searchWindow, text="Download Song", width=int(buttonWidth / 2),
                         bg="#5c1a56",
                         fg="silver",
                         font="sans 8 bold",
                         command=lambda: getSelectedItemFromListbox(listbox))
    # PACKING
    searchLabel.pack(side=tk.LEFT)
    modify.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (4 * buttonHeight))
    buttonBack.place(x=screenWidth / 2 - (buttonWidth * 2) + 15, y=screenHeight - 1 * buttonHeight)
    saveFavorite.place(x=screenWidth / 2 - (buttonWidth * 4), y=screenHeight - 2.5 * buttonHeight)
    download.place(x=screenWidth / 2 + (buttonWidth * 1), y=screenHeight - 2.5 * buttonHeight)
    searchAuthor.place(x=screenWidth / 2 + listBoxWidth / 2 * 6 - buttonWidth * 3.8, y=1.5 * buttonHeight)
    searchSong.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=1.5 * buttonHeight)
    searchGenre.place(x=screenWidth / 2 - (buttonWidth * 2), y=1.5 * buttonHeight)
    resetButton.place(x=screenWidth / 2 - (buttonWidth * 2), y=2.5 * buttonHeight + 5)
    searchFrame.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=10)
    searchWindow.mainloop()
