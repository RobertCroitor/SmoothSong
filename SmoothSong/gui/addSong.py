import tkinter as tk
import webbrowser
from tkinter.messagebox import showinfo

from gui import player
from postgres import songTableClass as songClass
from PIL import ImageTk, Image

song = songClass.Songs()


def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def openPayPal():
    url = "https://www.paypal.com/ro/business"
    webbrowser.open(url, new=1)


def postSong(songEntry, authorEntry, genreEntry, songImageEntry, songFileEntry):
    songName = (songEntry.get())
    authorName = (authorEntry.get())
    genreName = (genreEntry.get())
    songImage = (songImageEntry.get())
    songURL = (songFileEntry.get())
    if songName == "" or authorName == "" or genreName == "" or songImage == "" or songURL == "":
        tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
    else:
        confirmation = song.insertSong(songName, authorName, genreName, songImage, songURL)
        if confirmation:
            tk.messagebox.showwarning(title="Error", message="Song added successfully")
        else:
            tk.messagebox.showwarning(title="Error", message="Adding the song failed")
        songEntry.delete(0, tk.END)
        authorEntry.delete(0, tk.END)
        genreEntry.delete(0, tk.END)
        songImageEntry.delete(0, tk.END)
        songFileEntry.delete(0, tk.END)


def addSongWindow(userID):
    # Second Window
    addWindow = tk.Tk()
    addWindow.top_bar = tk.Frame(addWindow, bg="Red", cursor="sizing")
    addWindow.title("Add Song")
    addWindow.configure(bg="#5a5b5e")
    addWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(addWindow.winfo_screenwidth() * 0.5)
    screenHeight = round(addWindow.winfo_screenheight() * 0.9)
    addWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        addWindow,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)
    # BUTTON SIZE
    buttonWidth = 30

    # FORM

    addWindow.configure(background="grey")
    songLabel = tk.Label(addWindow, text='Title', width=10, bg="#5c1a56",
                         fg="silver")
    authorLabel = tk.Label(addWindow, text='Singer', width=10, bg="#5c1a56",
                           fg="silver")
    genreLabel = tk.Label(addWindow, text='Genre', width=10, bg="#5c1a56",
                          fg="silver")
    songImageLabel = tk.Label(addWindow, text='Image URL', width=10, bg="#5c1a56",
                              fg="silver")
    songFileLabel = tk.Label(addWindow, text='Song URL', width=10, bg="#5c1a56",
                             fg="silver")
    songEntry = tk.Entry(addWindow, width=70)
    authorEntry = tk.Entry(addWindow, width=70)
    genreEntry = tk.Entry(addWindow, width=70)
    songImageEntry = tk.Entry(addWindow, width=70)
    songFileEntry = tk.Entry(addWindow, width=70)
    addButton = tk.Button(addWindow, width=int(buttonWidth / 2), text='Submit', bg="#5c1a56",
                          fg="silver",
                          command=lambda: postSong(songEntry, authorEntry, genreEntry, songImageEntry, songFileEntry))

    # BUTTON
    buttonBack = tk.Button(addWindow, text="Music App", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(addWindow, userID))

    # PACKING
    songLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 2)
    authorLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 3)
    genreLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 4)
    songImageLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 5)
    songFileLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 6)
    songEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 2)
    authorEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 3)
    genreEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 4)
    songImageEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 5)
    songFileEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 6)
    addButton.place(x=281, y=screenHeight / 10 * 7)
    buttonBack.place(x=281, y=screenHeight / 10 * 9.5)
    addWindow.mainloop()
