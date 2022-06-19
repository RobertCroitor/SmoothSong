import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

from postgres import songTableClass as songClass
from postgres import downloadedTableClass as downloadedClass

from postgres import favoriteTableClass as favoritesClass
from gui import player
from utils import getDownloads
from musicPlayer import startMusic
from tkinter.messagebox import showinfo

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


def openPayPal():
    url = "https://www.paypal.com/ro/business"
    webbrowser.open(url, new=1)


def getSelectedItemFromListbox(listbox):
    if len(listbox.curselection()) > 0:
        for i in listbox.curselection():
            selectedOption = listbox.get(i)
            path = selectedOption + ".mp4"
            print(path)
            startMusic.startMusic(path)
    else:
        tk.messagebox.showwarning(title="Error", message="Nothing selected")


def downloadedSongsWindow(userID):
    # Second Window
    downloadedWindow = tk.Tk()
    downloadedWindow.top_bar = tk.Frame(downloadedWindow, bg="Red", cursor="sizing")
    downloadedWindow.title("Search Song")
    downloadedWindow.configure(bg="#5a5b5e")

    downloadedWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(downloadedWindow.winfo_screenwidth() * 0.5)
    screenHeight = round(downloadedWindow.winfo_screenheight() * 0.9)
    downloadedWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        downloadedWindow,
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
        downloadedWindow,
        height=listBoxHeight,
        width=listBoxWidth,
        selectmode='single')

    scrollbar = tk.Scrollbar(listbox)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.configure(justify="center")
    downloadContent = getDownloads.getFolderContent()
    for file in downloadContent:
        title = file.split(".")
        listbox.insert(tk.END, title[0])
    # BUTTON
    buttonBack = tk.Button(downloadedWindow, text="Music App", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(downloadedWindow, userID))

    download = tk.Button(downloadedWindow, text="Open", width=int(buttonWidth / 2),
                         bg="#5c1a56",
                         fg="silver",
                         font="sans 8 bold",
                         command=lambda: getSelectedItemFromListbox(listbox))
    # PACKING

    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (4 * buttonHeight))
    buttonBack.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 1 * buttonHeight)
    download.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 2.5 * buttonHeight)

    downloadedWindow.mainloop()
