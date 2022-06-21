import requests
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.messagebox import showinfo
from postgres import songTableClass

# CLASS INITIALISATION
songTable = songTableClass.Songs()


class CanvasManagementClass:
    # CANVAS FUNCTIONS
    @staticmethod
    def loadSongDetails(listbox, imageId, canvas, titleName, authorName, genreName, labelSong,
                        labelArtist, labelGenre, root, resetCanvasButton):
        if len(listbox.curselection()) == 1:
            canvasWidth = 350
            canvasHeight = 400
            buttonWidth = 30
            screenHeight = 691
            selectedOption = listbox.get(listbox.curselection())
            selectedOption = selectedOption.split("-")
            title = selectedOption[0].strip()
            author = selectedOption[1].strip()
            rows = songTable.getSongData(title, author)
            songTitle = rows[0][1]
            songAuthor = rows[0][2]
            songGenre = rows[0][3]
            songImage = rows[0][4]
            titleName.set(songTitle)
            authorName.set(songAuthor)
            genreName.set(songGenre)
            try:
                response = requests.get(songImage)
                file = open("assets/image.png", "wb")
                file.write(response.content)
                file.close()
                imgURL = "assets/image.png"
            except(Exception,):
                imgURL = "assets/noImage.png"
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
            resetCanvasButton.place(x=screenWidth / 4 - buttonWidth, y=screenHeight - 1 * buttonHeight - 5)

        else:
            tk.messagebox.showwarning(title="Error", message="You need to select exactly one item to load details!")

    @staticmethod
    def resetCanvas(imageId, canvas, resetCanvasButton, labelSong,
                    labelArtist, labelGenre):
        canvasWidth = 350
        canvasHeight = 400
        imgURL = "assets/smoothLogo.png"
        img = (Image.open(imgURL))
        resized_image = img.resize((canvasWidth, canvasHeight), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        canvas.imgref = new_image
        canvas.itemconfig(imageId, image=new_image)
        resetCanvasButton.place_forget()
        labelSong.place_forget()
        labelArtist.place_forget()
        labelGenre.place_forget()

    @staticmethod
    def initialiseCanvas(imageId, canvas):
        canvasWidth = 350
        canvasHeight = 400
        imgURL = "assets/smoothLogo.png"
        img = (Image.open(imgURL))
        resized_image = img.resize((canvasWidth, canvasHeight), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        canvas.imgref = new_image
        canvas.itemconfig(imageId, image=new_image)
    # CANVAS FUNCTIONS END
