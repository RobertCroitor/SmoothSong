def download(title, author, url):
    global out_file
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
        print(new_file)
        new_file = new_file
        os.rename(out_file, new_file)
    except:
        os.remove(out_file)
