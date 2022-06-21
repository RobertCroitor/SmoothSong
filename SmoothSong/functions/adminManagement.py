import tkinter as tk
from tkinter.messagebox import showinfo
from postgres import songTableClass
from postgres import userTableClass
from postgres import favoriteTableClass

# CLASS INITIALISATION
userTable = userTableClass.Users()
songTable = songTableClass.Songs()
favoritesTable = favoriteTableClass.Favorites()


class AdminManagementClass:
    # DELETE FUNCTIONS
    @staticmethod
    def deleteUserAdmin(userEntry, songEntry):
        userID = (userEntry.get())
        if userID == "":
            tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
        else:
            confirmation = userTable.deleteUser(userID)
            songEntry.delete(0, tk.END)
            userEntry.delete(0, tk.END)
            if confirmation:
                tk.messagebox.showwarning(title="Success", message="Success")
            else:
                tk.messagebox.showwarning(title="Error", message="Failure")

    @staticmethod
    def deleteSongAdmin(userEntry, songEntry):
        songID = (songEntry.get())
        if songID == "":
            tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
        else:
            rows = songTable.getSongByID(songID)
            title = rows[0][1]
            singer = rows[0][2]
            songConfirmation = songTable.deleteSong(songID)
            if songConfirmation:
                favoritesConfirmation = favoritesTable.deleteSongByTitleAndSinger(title, singer)
                if favoritesConfirmation:
                    tk.messagebox.showwarning(title="Success", message="Success")
                    songEntry.delete(0, tk.END)
                    userEntry.delete(0, tk.END)
                else:
                    tk.messagebox.showwarning(title="Error",
                                              message="Failure on deleting the song from favorites table")
            else:
                tk.messagebox.showwarning(title="Error", message="Failure on deleting the song from main table")

    # DELETE FUNCTIONS END

    # GIVE FUNCTIONS
    @staticmethod
    def giveUserAdminRights(userEntry, songEntry):
        userID = (userEntry.get())
        if userID == "":
            tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
        else:
            confirmation = userTable.insertAdmin(userID)
            songEntry.delete(0, tk.END)
            userEntry.delete(0, tk.END)
            if confirmation:
                tk.messagebox.showwarning(title="Success", message="Success")
            else:
                tk.messagebox.showwarning(title="Error", message="Failure")
    # GIVE FUNCTIONS END
