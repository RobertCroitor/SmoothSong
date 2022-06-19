import tkinter as tk
from tkinter.messagebox import showinfo

from gui import player
from postgres import songTableClass as songClass
from postgres import userTableClass as userClass
from PIL import ImageTk, Image

song = songClass.Songs()
user = userClass.Users()


def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def printSongs():
    rows = song.getAllSongs()
    print()
    for row in rows:
        print(row)


def printUsers():
    rows = user.getAllUsers()
    print()
    for row in rows:
        print(row)


def deleteUser(userEntry, songEntry):
    userID = (userEntry.get())
    if userID == "":
        tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
    else:
        confirmation = user.deleteUser(userID)
        songEntry.delete(0, tk.END)
        userEntry.delete(0, tk.END)
        if confirmation:
            tk.messagebox.showwarning(title="Error", message="Success")
        else:
            tk.messagebox.showwarning(title="Error", message="Failure")


def giveAdmin(userEntry, songEntry):
    userID = (userEntry.get())
    if userID == "":
        tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
    else:
        confirmation = user.insertAdmin(userID)
        songEntry.delete(0, tk.END)
        userEntry.delete(0, tk.END)
        if confirmation:
            tk.messagebox.showwarning(title="Error", message="Success")
        else:
            tk.messagebox.showwarning(title="Error", message="Failure")


def deleteSong(userEntry, songEntry):
    songID = (songEntry.get())

    if songID == "":
        tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
    else:
        confirmation = song.deleteSong(songID)
        songEntry.delete(0, tk.END)
        userEntry.delete(0, tk.END)
        if confirmation:
            tk.messagebox.showwarning(title="Error", message="Success")
        else:
            tk.messagebox.showwarning(title="Error", message="Failure")


def adminPanelWindow(userID):
    # Second Window
    adminWindow = tk.Tk()
    adminWindow.top_bar = tk.Frame(adminWindow, bg="Red", cursor="sizing")
    adminWindow.title("Add Song")
    adminWindow.configure(bg="#5a5b5e")
    adminWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(adminWindow.winfo_screenwidth() * 0.3)
    screenHeight = round(adminWindow.winfo_screenheight() * 0.3)
    adminWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    imgURL = "assets/bg2.jpg"
    img = (Image.open(imgURL))
    resized_image = img.resize((screenWidth, screenHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    bg = tk.Label(
        adminWindow,
        image=new_image, borderwidth=0,
        highlightthickness=0
    )
    bg.imgref = new_image
    bg.place(x=0, y=0)
    # BUTTON SIZE
    buttonWidth = 30

    # FORM

    adminWindow.configure(background="grey")
    userLabel = tk.Label(adminWindow, text='userID', width=10, bg="#5c1a56",
                         fg="silver")
    songLabel = tk.Label(adminWindow, text='songID', width=10, bg="#5c1a56",
                         fg="silver")

    userEntry = tk.Entry(adminWindow, width=30)
    songEntry = tk.Entry(adminWindow, width=30)

    deleteUserButton = tk.Button(adminWindow, width=int(buttonWidth / 3), text='Delete User', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: deleteUser(userEntry, songEntry))
    deleteSongButton = tk.Button(adminWindow, width=int(buttonWidth / 3), text='Delete Song', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: deleteSong(userEntry, songEntry))
    updateUser = tk.Button(adminWindow, width=int(buttonWidth / 3), text='Update', bg="#5c1a56",
                           fg="silver",
                           command=lambda: giveAdmin(userEntry, songEntry))

    printUsersButton = tk.Button(adminWindow, width=5, text='Users', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: printUsers())
    printSongsButton = tk.Button(adminWindow, width=5, text='Songs', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: printSongs())
    # BUTTON
    buttonBack = tk.Button(adminWindow, text="Back", width=5,
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(adminWindow, userID))

    # PACKING
    songLabel.place(x=screenWidth / 2 - 140, y=screenHeight / 10 * 2)
    userLabel.place(x=screenWidth / 2 - 140, y=screenHeight / 10 * 3)
    songEntry.place(x=screenWidth / 2 - 65, y=screenHeight / 10 * 2)
    userEntry.place(x=screenWidth / 2 - 65, y=screenHeight / 10 * 3)
    deleteSongButton.place(x=screenWidth / 2 - 140, y=screenHeight / 10 * 5)
    deleteUserButton.place(x=screenWidth / 2 - 50, y=screenHeight / 10 * 5)
    updateUser.place(x=screenWidth / 2 + 40, y=screenHeight / 10 * 5)
    buttonBack.place(x=screenWidth - 45, y=screenHeight / 10 * 8.9)
    printSongsButton.place(x=1, y=screenHeight / 10 * 8.9)
    printUsersButton.place(x=50, y=screenHeight / 10 * 8.9)
    adminWindow.mainloop()
