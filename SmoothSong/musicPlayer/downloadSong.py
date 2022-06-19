def download(title, author, url):
    from pytube import YouTube
    import os

    yt = YouTube(url)

    video = yt.streams.filter(only_audio=True).first()
    try:
        songName = title
        songAuthor = author
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = "./musicPlayer/downloads/" + songName + "-" + songAuthor + ext

        new_file = new_file
        os.rename(out_file, new_file)
    except:
        os.remove(out_file)


def downloadPlaylist(title, author, url, playlistName):
    from pytube import YouTube
    import os

    yt = YouTube(url)
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
    except:
        os.remove(out_file)


def createDir(playlistName):
    import os
    if not os.path.exists(playlistName):
        os.mkdir("./musicPlayer/downloads/" + playlistName)
