import os
import tkinter as tk
from tkinter.messagebox import showinfo
from pytube import YouTube


# DOWNLOAD A SINGLE SONG
def download(title, author, url):
    goodURL = True
    try:
        yt = YouTube(url)
    except(Exception,):
        goodURL = False
        tk.messagebox.showwarning(title="Error", message="This song URL is corrupted")
    if goodURL:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        # RENAME THE SONG AND CHANGE IT'S DIRECTORY
        try:
            songName = title
            songAuthor = author
            out_file = video.download(output_path=".")
            base, ext = os.path.splitext(out_file)
            new_file = "./musicPlayer/downloads/" + songName + "-" + songAuthor + ext
            new_file = new_file
            os.rename(out_file, new_file)
        # IF RENAMING FAILED OR SONG EXISTED ALREADY DELETE THE WRONGLY PLACED FILES
        except (Exception,):
            os.remove(out_file)


# CREATE A NEW DIRECTORY WITH THE NAME GIVEN AND DOWNLOAD ALL THE SONGS IN THERE
def downloadPlaylist(title, author, url, playlistName):
    goodURL = True
    try:
        yt = YouTube(url)
    except (Exception,):
        goodURL = False
        tk.messagebox.showwarning(title="Error", message="This song URL is corrupted")
    # CREATE A NEW DIRECTORY AND RENAME EACH INDIVIDUAL FILE TO CHANGE THE PATH TO THIS DIRECTORY
    if goodURL:
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            dirPath = playlistName + "/"
            songName = title
            songAuthor = author
            out_file = video.download(output_path=".")
            base, ext = os.path.splitext(out_file)
            path = "./musicPlayer/downloads/" + dirPath
            new_file = path + songName + "-" + songAuthor + ext
            new_file = new_file
            os.rename(out_file, new_file)
        # IF SONGS ALREADY EXISTS, DELETE THE WRONGLY PLACED SONGS
        except (Exception,):
            os.remove(out_file)


# CREATE A NEW DIRECTORY IN DOWNLOADS FOLDER WITH THE GIVEN NAME
def createDir(playlistName):
    path = "./musicPlayer/downloads/" + playlistName
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir("./musicPlayer/downloads/" + playlistName)
