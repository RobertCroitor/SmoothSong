from postgres import songTableClass
from musicPlayer import downloadSong
import tkinter as tk
from tkinter.messagebox import showinfo

# DATA INITIALISATION
songsTable = songTableClass.Songs()


class DownloadManagementClass:
    # DOWNLOAD INDIVIDUAL SONGS
    @staticmethod
    def downloadSelectedSongs(listbox):
        if len(listbox.curselection()) > 0:
            for i in listbox.curselection():
                selectedOption = listbox.get(i)
                selectedOption = selectedOption.split("-")
                title = selectedOption[0].strip()
                author = selectedOption[1].strip()
                rows = songsTable.getSongData(title, author)
                songTitle = rows[0][1]
                songAuthor = rows[0][2]
                songURL = rows[0][5]

                downloadSong.download(songTitle, songAuthor, songURL)
        else:
            tk.messagebox.showwarning(title="Error", message="Nothing selected to download")

    # DOWNLOAD SONGS AS PLAYLIST
    @staticmethod
    def downloadPlaylist(playlistListbox, playlistEntry):
        if playlistEntry.get():
            for i in range(playlistListbox.size()):
                playlist = (playlistEntry.get())
                selectedOption = playlistListbox.get(i).split("-")
                title = selectedOption[0].strip()
                author = selectedOption[1].strip()
                rows = songsTable.getSongData(title, author)
                songTitle = rows[0][1]
                songAuthor = rows[0][2]
                songURL = rows[0][5]
                downloadSong.createDir(playlist)
                downloadSong.downloadPlaylist(songTitle, songAuthor, songURL, playlist)
        else:
            tk.messagebox.showwarning(title="Error", message="No name given to the playlist!")
