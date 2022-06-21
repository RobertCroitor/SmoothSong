import tkinter as tk
from tkinter.messagebox import showinfo
from postgres import songTableClass
from postgres import userTableClass
import os

# CLASS INITIALISATION
userTable = userTableClass.Users()
songTable = songTableClass.Songs()


class DataManagementClass:
    # INSERT FUNCTIONS
    @staticmethod
    def insertSongIntoSongTable(songEntry, authorEntry, genreEntry, songImageEntry, songFileEntry):
        songName = (songEntry.get()).strip()
        songSinger = (authorEntry.get()).strip()
        songGenre = (genreEntry.get()).strip()
        songImage = (songImageEntry.get())
        songURL = (songFileEntry.get())
        if songName == "" or songSinger == "" or songGenre == "" or songImage == "" or songURL == "":
            tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
        else:
            count = songTable.getSongCountByTitleAndSinger(songName, songSinger)[0][0]
            if count == 0:
                confirmation = songTable.insertSong(songName, songSinger, songGenre, songImage, songURL)
                if confirmation:
                    tk.messagebox.showwarning(title="Success", message="Song added successfully")
                else:
                    tk.messagebox.showwarning(title="Error", message="Adding the song failed")
            else:
                tk.messagebox.showwarning(title="Error", message="This song is already added")
            songEntry.delete(0, tk.END)
            authorEntry.delete(0, tk.END)
            genreEntry.delete(0, tk.END)
            songImageEntry.delete(0, tk.END)
            songFileEntry.delete(0, tk.END)

    # INSERT FUNCTIONS END

    # CHECK FUNCTIONS
    @staticmethod
    def isUserAdmin(userID):
        isUserAdmin = userTable.getAdminByID(userID)
        return isUserAdmin

    # CHECK FUNCTIONS END

    # GET FUNCTIONS
    @staticmethod
    def getFolderContent():
        content = ""
        for path, currentDirectory, files in os.walk("musicPlayer/downloads"):
            for file in files:
                x = os.path.join(path, file).split("/")
                y = x[1].split("\\")
                if len(y) == 2:
                    content = content + "#" + y[1]
                if len(y) == 3:
                    content = content + "#" + y[1] + "/" + y[2]
        return content
    # GET FUNCTIONS END
