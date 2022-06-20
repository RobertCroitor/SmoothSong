from postgres import favoriteTableClass
from postgres import songTableClass
from postgres import userTableClass
from musicPlayer import startMusic
import tkinter as tk
from tkinter.messagebox import showinfo
import random
from functions import dataManagement

# CLASS INITIALISATION
dataManagement = dataManagement.DataManagementClass()
favoriteTable = favoriteTableClass.Favorites()
songTable = songTableClass.Songs()
userTable = userTableClass.Users()


# CLEAR ALL THE FILTERS AND INSERT ALL THE SONGS FROM SONG TABLE INTO SONG COLLECTION LISTBOX
def resetListbox(listbox):
    listbox.delete(0, tk.END)
    songRow = songTable.getAllSongs()
    random.shuffle(songRow)
    for row in songRow:
        title = row[1]
        singer = row[2]
        listbox.insert(tk.END, title + "  -  " + singer)


class ListboxManagementClass:
    # INSERT FUNCTIONS
    # INSERT TO FAVORITES
    @staticmethod
    def saveToFavorites(listbox, userID):
        selectedOption = listbox.get(listbox.curselection())
        selectedOption = selectedOption.split("-")
        title = selectedOption[0].strip()
        author = selectedOption[1].strip()
        rows = songTable.getSongData(title, author)
        title = rows[0][1]
        author = rows[0][2]
        count = favoriteTable.getSongsCountByTitle(title, author, userID)[0][0]

        if count > 0:
            tk.messagebox.showwarning(title="Error", message="Song is already added to favorites")
        else:
            singer = rows[0][2]
            genre = rows[0][3]
            imgURL = rows[0][4]
            songURL = rows[0][5]
            confirmation = favoriteTable.insertSong(userID, title, singer, genre, imgURL, songURL)
            if confirmation:
                tk.messagebox.showwarning(title="Error", message="Song added to favorites successfully")
            else:
                tk.messagebox.showwarning(title="Error", message="Adding the song to favorites failed")

    # ADD SONGS FROM FAVORITES TO PLAYLIST
    @staticmethod
    def addSongToPlaylist(favoritesListbox, playlistListBox):
        if len(favoritesListbox.curselection()) > 0:
            for i in favoritesListbox.curselection():
                playlistListBox.insert(tk.END, favoritesListbox.get(i))
        else:
            tk.messagebox.showwarning(title="Error", message="Nothing selected to add")

    # INITIALISE FAVORITES LISTBOX
    @staticmethod
    def populateFavoritesListbox(favoritesListbox, userID):
        songRow = favoriteTable.getSongsByUserID(userID)
        for row in songRow:
            title = row[2]
            singer = row[3]
            favoritesListbox.insert(tk.END, title + "  -  " + singer)

    # INITIALISE SONG COLLECTION LISTBOX
    @staticmethod
    def populateSearchSongsListbox(searchListbox):
        songRow = songTable.getAllSongs()
        for row in songRow:
            title = row[1]
            singer = row[2]
            searchListbox.insert(tk.END, title + "  -  " + singer)

    # INITIALISE DOWNLOADED SONGS LISTBOX
    @staticmethod
    def populateDownloadedListbox(listbox):
        downloadContent = dataManagement.getFolderContent()
        splitContent = downloadContent.split("#")
        for file in splitContent:
            if file != "":
                title = file.split(".")
                listbox.insert(tk.END, title[0])

    # RESET AND POPULATE SONG COLLECTION LISTBOX WITH SINGER FILTERS
    @staticmethod
    def searchSongsByAuthor(listbox, titleEntry):
        if len(titleEntry.get()) != 0:
            print(len(titleEntry.get()))
            count = 0
            title = (titleEntry.get())
            rows = songTable.getAllSongs()
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
        else:
            tk.messagebox.showwarning(title="Error", message="No keyword typed in order to search")
        # RESET THE SONG COLLECTION LISTBOX

    @staticmethod
    def resetSongCollectionListbox(listbox, titleEntry):
        resetListbox(listbox)
        titleEntry.delete(0, tk.END)

    # RESET AND POPULATE SONG COLLECTION LISTBOX WITH TITLE FILTERS
    @staticmethod
    def searchSongsByTitle(listbox, titleEntry):
        if len(titleEntry.get()) != 0:
            count = 0
            title = (titleEntry.get())
            rows = songTable.getAllSongs()
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
        else:
            tk.messagebox.showwarning(title="Error", message="No keyword typed in order to search")

    # RESET AND POPULATE SONG COLLECTION LISTBOX WITH GENRE FILTERS
    @staticmethod
    def searchSongsByGenre(listbox, titleEntry):
        if len(titleEntry.get()) != 0:
            count = 0
            title = (titleEntry.get())
            rows = songTable.getAllSongs()
            listbox.delete(0, tk.END)
            for row in rows:
                dbGenre = row[3]
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
        else:
            tk.messagebox.showwarning(title="Error", message="No keyword typed in order to search")

    # INSERT FUNCTIONS END

    # REMOVE FUNCTIONS
    # REMOVE ONE ITEM FROM PLAYLIST LISTBOX
    @staticmethod
    def removeItemsFromPlaylistListbox(listbox):
        if len(listbox.curselection()) > 0:
            for i in reversed(listbox.curselection()):
                listbox.delete(i)
        else:
            tk.messagebox.showwarning(title="Error", message="Nothing selected to delete")

    # REMOVE ONE ITEM FROM FAVORITES LISTBOX
    @staticmethod
    def removeItemsFromFavoritesListbox(listbox):
        if len(listbox.curselection()) > 0:
            for i in reversed(listbox.curselection()):
                selectedOption = listbox.get(i)
                selectedOption = selectedOption.split("-")
                title = selectedOption[0].strip()
                author = selectedOption[1].strip()
                rows = favoriteTable.getSongData(title, author)
                songID = rows[0][0]
                favoriteTable.deleteSongByID(songID)
                listbox.delete(i)
        else:
            tk.messagebox.showwarning(title="Error", message="Nothing selected to delete")

    # REMOVE ALL ITEMS FROM FAVORITES LISTBOX
    @staticmethod
    def clearFavoritesListbox(favoritesListbox):
        confirmation = favoriteTable.deleteTable()
        if confirmation:
            confirmation = favoriteTable.createTable()
            if confirmation:
                favoritesListbox.delete(0, tk.END)

    # REMOVE ALL ITEMS FROM PLAYLIST LISTBOX
    @staticmethod
    def clearPlaylistListbox(playlistListBox):
        playlistListBox.delete(0, tk.END)

    # REMOVE FUNCTIONS END

    # GET FUNCTIONS
    # GET ALL SONGS FROM SONG TABLE
    @staticmethod
    def getSongsDataAdminListbox(adminListbox):
        adminListbox.delete(0, tk.END)
        firstRow = "SongID - Title - Singer - Genre"
        adminListbox.insert(tk.END, firstRow)
        adminListbox.insert(tk.END, "")
        rows = songTable.getAllSongs()
        for row in rows:
            songID = row[0]
            title = row[1]
            singer = row[2]
            genre = row[3]
            songsData = str(songID) + " - " + title + " - " + singer + " - " + genre
            adminListbox.insert(tk.END, songsData)

    # GET ALL USERS FROM USER TABLE
    @staticmethod
    def getUsersDataAdminListbox(adminListbox):
        adminListbox.delete(0, tk.END)
        firstRow = "UserID - Username - isAdmin"
        adminListbox.insert(tk.END, firstRow)
        adminListbox.insert(tk.END, "")
        rows = userTable.getAllUsers()
        for row in rows:
            userID = row[0]
            name = row[1]
            isAdmin = row[4]
            songsData = str(userID) + " - " + name + " - " + str(isAdmin)
            adminListbox.insert(tk.END, songsData)

    # GET FUNCTIONS END

    # OTHER FUNCTIONS
    # OPEN THE SELECTED SONG FROM DOWNLOADED LISTBOX WITH A 3RD PARTY APP
    @staticmethod
    def openSelectedSong(listbox):
        if len(listbox.curselection()) > 0:
            for i in listbox.curselection():
                selectedOption = listbox.get(i)
                path = selectedOption + ".mp4"
                startMusic.startMusic(path)
        else:
            tk.messagebox.showwarning(title="Error", message="Nothing selected")
    # OTHER FUNCTIONS END
