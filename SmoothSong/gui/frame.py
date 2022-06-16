import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
import webbrowser
from postgres import selectAllSongs as getSongs
from postgres import insertTableSongs as postSongs
from utils import crypt
from postgres import getUserByUsername as getUsername
from postgres import getCountUserByUsername as getCountUsername
from postgres import insertUserTable as postUser


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
        postSongs.insertSong(songName, authorName, genreName, songImage, songURL)
        songEntry.delete(0, tk.END)
        authorEntry.delete(0, tk.END)
        genreEntry.delete(0, tk.END)
        songImageEntry.delete(0, tk.END)
        songFileEntry.delete(0, tk.END)


def register(nameEntry, passwordEntry, rePasswordEntry, window):
    inputUsername = (nameEntry.get())
    inputPassword = (passwordEntry.get())
    inputRePassword = (rePasswordEntry.get())
    if inputUsername == "":
        passwordEntry.delete(0, tk.END)
        rePasswordEntry.delete(0, tk.END)
        tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
    else:
        count = getCountUsername.getUserByUsername(inputUsername)[0][0]
        if count == 1:
            passwordEntry.delete(0, tk.END)
            rePasswordEntry.delete(0, tk.END)
            tk.messagebox.showwarning(title="Error", message="Username is already used")
        else:
            if inputPassword == "":
                rePasswordEntry.delete(0, tk.END)
                tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
            else:
                if inputRePassword == "":
                    tk.messagebox.showwarning(title="Error", message="Password confirmation cannot be empty")
                else:
                    if len(inputPassword) < 8:
                        passwordEntry.delete(0, tk.END)
                        rePasswordEntry.delete(0, tk.END)
                        tk.messagebox.showwarning(title="Error", message="Password must be at least 8 characters")
                    else:
                        if inputPassword != inputRePassword:
                            rePasswordEntry.delete(0, tk.END)
                            tk.messagebox.showwarning(title="Error", message="Passwords do not match")
                        else:
                            confirmation = postUser.insertUser(inputUsername, inputPassword)
                            if confirmation:
                                tk.messagebox.showwarning(title="Error",
                                                          message="Register Succesfully")
                                goToLogin(window)
                            else:
                                tk.messagebox.showwarning(title="Error",
                                                          message="Register Failed")


def login(nameEntry, passwordEntry, window):
    inputUsername = (nameEntry.get())
    inputPassword = (passwordEntry.get())
    if inputUsername == "" and inputPassword == "":
        tk.messagebox.showwarning(title="Error", message="Username and Password cannot be empty")
    else:
        if inputUsername == "":
            passwordEntry.delete(0, tk.END)
            tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
        else:
            if inputPassword == "":
                tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
            else:
                cryptedInputPassword = crypt.encrypt(inputPassword)
                count = getCountUsername.getUserByUsername(inputUsername)[0][0]
                if count == 0:
                    passwordEntry.delete(0, tk.END)
                    tk.messagebox.showwarning(title="Error", message="Wrong Username")

                else:
                    dbPassword = getUsername.getUserByUsername(inputUsername)[0][2]
                    if dbPassword != cryptedInputPassword:
                        passwordEntry.delete(0, tk.END)
                        tk.messagebox.showwarning(title="Error", message="Wrong Password")

                    else:
                        goBackToMainWindow(window)


def changeWindowToAddSong(window):
    window.destroy()
    addSongWindow()


def changeWindowToSearch(window):
    window.destroy()
    searchFrame()


def goToRegister(window):
    window.destroy()
    registerWindow()


def goToLogin(window):
    window.destroy()
    loginWindow()


def goBackToMainWindow(window):
    window.destroy()
    mainWindow()


def registerWindow():
    # Login Window
    registerWindow = tk.Tk()
    registerWindow.top_bar = tk.Frame(registerWindow, bg="Red", cursor="sizing")
    registerWindow.title("Register")
    registerWindow.configure(bg="#5a5b5e")
    registerWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(registerWindow.winfo_screenwidth() * 0.3)
    screenHeight = round(registerWindow.winfo_screenheight() * 0.5)
    registerWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    # BUTTON SIZE
    buttonWidth = 30

    # LIST SIZE
    listBoxWidth = 80
    listBoxHeight = 35

    # FORM

    registerWindow.configure(background="grey")
    nameLabel = tk.Label(registerWindow, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )

    passwordLabel = tk.Label(registerWindow, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    rePasswordLabel = tk.Label(registerWindow, text='Re-Password', width=10, bg="#5c1a56",
                               fg="silver", font="sans 8 bold", )

    nameEntry = tk.Entry(registerWindow, width=50)

    passwordEntry = tk.Entry(registerWindow, show="\u2022", width=50)
    rePasswordEntry = tk.Entry(registerWindow, show="\u2022", width=50)

    registerButton = tk.Button(registerWindow, width=int(buttonWidth / 2), text='Register', bg="#5c1a56",
                               fg="silver", font="sans 8 bold",
                               command=lambda: register(nameEntry, passwordEntry, rePasswordEntry, registerWindow))

    # BUTTON
    loginButton = tk.Button(registerWindow, text="Login", width=int(buttonWidth / 2),
                            bg="#5c1a56",
                            fg="silver",
                            font="sans 8 bold",
                            command=lambda: goToLogin(registerWindow))

    # PACKING

    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 1.5)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 3.5)
    rePasswordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 5.5)
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 1.5)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 3.5)
    rePasswordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 5.5)
    registerButton.place(x=150, y=screenHeight / 10 * 7)
    loginButton.place(x=150, y=screenHeight / 10 * 8.5)
    registerWindow.mainloop()


def loginWindow():
    # Login Window
    loginWindow = tk.Tk()
    loginWindow.top_bar = tk.Frame(loginWindow, bg="Red", cursor="sizing")
    loginWindow.title("Login")
    loginWindow.configure(bg="#5a5b5e")
    loginWindow.resizable(False, False)
    # SCREEN SIZE
    screenWidth = round(loginWindow.winfo_screenwidth() * 0.3)
    screenHeight = round(loginWindow.winfo_screenheight() * 0.3)
    loginWindow.geometry("%dx%d" % (screenWidth, screenHeight))
    # BUTTON SIZE
    buttonWidth = 30

    # LIST SIZE
    listBoxWidth = 80
    listBoxHeight = 35

    # FORM

    loginWindow.configure(background="grey")
    nameLabel = tk.Label(loginWindow, text='Name', width=10, bg="#5c1a56",
                         fg="silver", font="sans 8 bold", )

    passwordLabel = tk.Label(loginWindow, text='Password', width=10, bg="#5c1a56",
                             fg="silver", font="sans 8 bold", )

    nameEntry = tk.Entry(loginWindow, width=50)

    passwordEntry = tk.Entry(loginWindow, show="\u2022", width=50)

    loginButton = tk.Button(loginWindow, width=int(buttonWidth / 2), text='Login', bg="#5c1a56",
                            fg="silver", font="sans 8 bold",
                            command=lambda: login(nameEntry, passwordEntry, loginWindow))

    # BUTTON
    registerButton = tk.Button(loginWindow, text="Register", width=int(buttonWidth / 2),
                               bg="#5c1a56",
                               fg="silver",
                               font="sans 8 bold",
                               command=lambda: goToRegister(loginWindow))

    # PACKING

    nameLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 2)
    passwordLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 4)
    nameEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 2)
    passwordEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 4)
    loginButton.place(x=150, y=screenHeight / 10 * 6)
    registerButton.place(x=150, y=screenHeight / 10 * 8)
    loginWindow.mainloop()


def addSongWindow():
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
    # BUTTON SIZE
    buttonWidth = 30

    # LIST SIZE
    listBoxWidth = 80
    listBoxHeight = 35

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
                           command=lambda: goBackToMainWindow(addWindow))

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


def searchFrame():
    def items_selected(event):
        selectedIndex = listbox.curselection()
        selectedItems = ",".join([listbox.get(index) for index in selectedIndex])
        msg = f'You selected: {selectedItems}'
        showinfo(
            title='Information',
            message=msg)

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
        selectmode='extended')

    for i in range(100):
        listbox.insert(tk.END, "Song " + str(i))

    scrollbar = tk.Scrollbar(listbox)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.bind('<<ListboxSelect>>', items_selected)

    # SEARCH BAR
    searchFrame = tk.Frame(searchWindow, bg='red')
    searchLabel = tk.Label(searchFrame, text='Search Song', width=10, bg="#5c1a56",
                           fg="silver")
    modify = tk.Entry(searchFrame, width=68)

    modify.focus_set()

    searchAuthor = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Search Author', bg="#5c1a56",
                             fg="silver")

    searchSong = tk.Button(searchWindow, width=int(buttonWidth / 2), text='Search Song', bg="#5c1a56",
                           fg="silver")

    # BUTTON
    buttonBack = tk.Button(searchWindow, text="Music App", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(searchWindow))

    # PACKING
    searchLabel.pack(side=tk.LEFT)
    modify.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    listbox.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=0 + (4 * buttonHeight))
    buttonBack.place(x=screenWidth / 2 - (buttonWidth * 2), y=screenHeight - 1.5 * buttonHeight)
    searchAuthor.place(x=screenWidth / 2 + (buttonWidth * 2), y=1.5 * buttonHeight)
    searchSong.place(x=screenWidth / 2 - (buttonWidth * 5), y=1.5 * buttonHeight)
    searchFrame.place(x=screenWidth / 2 - listBoxWidth / 2 * 6, y=10)
    searchWindow.mainloop()


def mainWindow():
    # Functions

    def items_selected(event):
        selectedIndex = listbox.curselection()
        selectedItems = ",".join([listbox.get(index) for index in selectedIndex])
        msg = f'You selected: {selectedItems}'
        showinfo(
            title='Information',
            message=msg)

    def startPB():
        pb.start()

    def stopPB():
        pb.stop()

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

    # SONG DATA
    # songLenght = 180
    # stepPB = 900 / songLenght

    # BUTTON SIZE
    buttonWidth = 30
    buttonHeight = 30

    # LIST SIZE
    listBoxWidth = 80
    listBoxHeight = 35

    # CANVAS SIZE
    canvasWidth = 350
    canvasHeight = 400
    imgURL = "C:\\Users\\Adoranah\\PycharmProjects\\Bachelors\\gui\\placeholder.png"

    # LABEL SIZE
    labelWidth = 50
    labelHeight = 10

    # PROGRESS BAR
    pb = Progressbar(root, orient=tk.HORIZONTAL, length=500, mode='determinate')

    # LIST BOX
    listbox = tk.Listbox(root, height=listBoxHeight, width=listBoxWidth, selectmode='extended')
    scrollbar = tk.Scrollbar(listbox)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.bind('<<ListboxSelect>>', items_selected)
    songRow = getSongs.getAllSongs()
    for row in songRow:
        title = row[1]
        singer = row[2]
        listbox.insert(tk.END, "  " * 3 + title + "  -  " + singer)

    # BUTTON
    playButton = tk.Button(root, text="Play", height=buttonHeight, width=buttonWidth, image=pixelVirtual, bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold")
    nextButton = tk.Button(root, text="Next", height=buttonHeight, width=buttonWidth, image=pixelVirtual, bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", )
    prevButton = tk.Button(root, text="Prev", height=buttonHeight, width=buttonWidth, image=pixelVirtual, bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold")
    stopButton = tk.Button(root, text="Pause", height=buttonHeight, width=buttonWidth, image=pixelVirtual, bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=stopPB)
    addButton = tk.Button(root, text="Add Song", height=buttonHeight, width=buttonWidth * 4, image=pixelVirtual,
                          bg="#5c1a56",
                          fg="silver",
                          compound="c", font="sans 8 bold",
                          command=lambda: [stopPB(), changeWindowToAddSong(root)])
    searchButton = tk.Button(root, text="Search Panel", height=buttonHeight, width=buttonWidth * 4, image=pixelVirtual,
                             bg="#5c1a56",
                             fg="silver",
                             compound="c", font="sans 8 bold",
                             command=lambda: [stopPB(), changeWindowToSearch(root)])
    donateButton = tk.Button(root, text="Donate", height=buttonHeight, width=buttonWidth * 4, image=pixelVirtual,
                             bg="#5c1a56",
                             fg="silver",
                             compound="c", font="sans 8 bold",
                             command=openPayPal)

    # IMAGE

    img = (Image.open(imgURL))
    resized_image = img.resize((canvasWidth, canvasHeight), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.create_image(0, 0, anchor=tk.NW, image=new_image)

    # LABEL

    artist = tk.StringVar()
    labelArtist = tk.Label(root, textvariable=artist, relief=tk.RAISED, bg="#5c1a56",
                           fg="silver", width=labelWidth)
    artist.set("Song title placeholder")
    songName = tk.StringVar()
    labelSong = tk.Label(root, textvariable=songName, relief=tk.RAISED, bg="#5c1a56",
                         fg="silver", width=labelWidth)
    songName.set("Author name placeholder")

    # PACKING
    labelSong.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=canvasHeight + (2 * buttonHeight))
    labelArtist.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=canvasHeight + (3 * buttonHeight))
    listbox.place(x=screenWidth - 500, y=0 + buttonHeight)
    canvas.place(x=screenWidth / 4 - (canvasWidth / 2 - 5), y=0 + buttonHeight)
    pb.place(x=screenWidth / 4 - 250, y=screenHeight - 3 * buttonHeight)
    playButton.place(x=screenWidth / 4 - buttonWidth, y=screenHeight - 1.5 * buttonHeight)
    stopButton.place(x=screenWidth / 4 + buttonWidth, y=screenHeight - 1.5 * buttonHeight)
    nextButton.place(x=screenWidth / 2 - 1.5 * buttonWidth, y=screenHeight - 1.5 * buttonHeight)
    prevButton.place(x=10, y=screenHeight - 1.5 * buttonHeight)
    addButton.place(x=screenWidth - 1.5 * (buttonWidth * 10.5), y=screenHeight - 1.5 * buttonHeight)
    donateButton.place(x=screenWidth - 1.5 * (buttonWidth * 7), y=screenHeight - 1.5 * buttonHeight)
    searchButton.place(x=screenWidth - 1.5 * (buttonWidth * 3.5), y=screenHeight - 1.5 * buttonHeight)

    # Second Window Components

    root.mainloop()
