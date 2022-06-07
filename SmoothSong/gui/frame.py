import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
import webbrowser


def openPayPal():
    url = "https://www.paypal.com/ro/business"
    webbrowser.open(url, new=1)


def changeWindowToAddSong(window):
    window.destroy()
    addSongWindow()


def changeWindowToSearch(window):
    window.destroy()
    searchFrame()


def goBackToMainWindow(window):
    window.destroy()
    func()


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
    songLabel = tk.Label(addWindow, text='Search Song', width=10, bg="#5c1a56",
                         fg="silver")
    authorLabel = tk.Label(addWindow, text='Search Song', width=10, bg="#5c1a56",
                           fg="silver")
    songImageLabel = tk.Label(addWindow, text='Search Song', width=10, bg="#5c1a56",
                              fg="silver")
    songFileLabel = tk.Label(addWindow, text='Search Song', width=10, bg="#5c1a56",
                             fg="silver")
    songEntry = tk.Entry(addWindow, width=70)
    authorEntry = tk.Entry(addWindow, width=70)
    songImageEntry = tk.Entry(addWindow, width=70)
    songFileEntry = tk.Entry(addWindow, width=70)
    addButton = tk.Button(addWindow, width=int(buttonWidth / 2), text='Submit', bg="#5c1a56",
                          fg="silver")

    # BUTTON
    buttonBack = tk.Button(addWindow, text="Music App", width=int(buttonWidth / 2),
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(addWindow))

    print(buttonWidth)
    print(screenWidth)
    # PACKING
    songLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 2)
    authorLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 3)
    songImageLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 4)
    songFileLabel.place(x=screenWidth / 2 - 240, y=screenHeight / 10 * 5)
    songEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 2)
    authorEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 3)
    songImageEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 4)
    songFileEntry.place(x=screenWidth / 2 - 165, y=screenHeight / 10 * 5)
    addButton.place(x=281, y=screenHeight / 10 * 6)
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


def func():
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
    pb = Progressbar(root,orient=tk.HORIZONTAL,length=500,mode='determinate')

    # LIST BOX
    listbox = tk.Listbox(root,height=listBoxHeight,width=listBoxWidth,selectmode='extended')
    scrollbar = tk.Scrollbar(listbox)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.bind('<<ListboxSelect>>', items_selected)
    for i in range(100):
        listbox.insert(tk.END, "Song " + str(i))



    # BUTTON
    playButton = tk.Button(root, text="Play", height=buttonHeight, width=buttonWidth, image=pixelVirtual, bg="#5c1a56",
                           fg="silver", command=startPB,
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
