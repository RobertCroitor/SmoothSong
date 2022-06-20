import os
from pytube import YouTube


# DOWNLOAD A SINGLE SONG
def download(title, author, url):
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
    except:
        os.remove(out_file)


# CREATE A NEW DIRECTORY WITH THE NAME GIVEN AND DOWNLOAD ALL THE SONGS IN THERE
def downloadPlaylist(title, author, url, playlistName):
    yt = YouTube(url)
    # CREATE A NEW DIRECTORY AND RENAME EACH INDIVIDUAL FILE TO CHANGE THE PATH TO THIS DIRECTORY
    try:
        video = yt.streams.filter(only_audio=True).first()
        dirPath = playlistName + "/"
        if not os.path.exists(playlistName):
            os.mkdir(playlistName)
        songName = title
        songAuthor = author
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        path = "./musicPlayer/downloads/" + dirPath
        new_file = path + songName + "-" + songAuthor + ext
        new_file = new_file
        os.rename(out_file, new_file)
    # IF SONGS ALREADY EXISTS, DELETE THE WRONGLY PLACED SONGS
    except:
        os.remove(out_file)


# CREATE A NEW DIRECTORY IN DOWNLOADS FOLDER WITH THE GIVEN NAME
def createDir(playlistName):
    if not os.path.exists(playlistName):
        os.mkdir("./musicPlayer/downloads/" + playlistName)
