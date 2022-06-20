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
                        labelArtist, labelGenre, root):
        if len(listbox.curselection()) == 1:
            canvasWidth = 350
            canvasHeight = 400
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
            except:
                imgURL = "assets/placeholder.png"
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
    # CANVAS FUNCTIONS END
